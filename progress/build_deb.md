# Ubuntu环境
以`sqlite`为例，通过以下命令从源码构建`deb`包：
```bash
apt source sqlite     # 获取源码包
apt build-dep sqlite  # 安装构建依赖
cd sqlite-2.8.17      # 进入源码目录
fakeroot debian/rules build  # 构建
fakeroot debian/rules binary # 打包
```
在构建过程中会出现如下报错：
```bash
collect2: error: ld returned 1 exit status
make[2]: *** [Makefile:366: testfixture] Error 1
make[2]: Leaving directory '/home/young/packages/sqlite/sqlite-2.8.17'
dh_auto_test: error: make -j1 test VERBOSE=1 returned exit code 2
make[1]: Leaving directory '/home/young/packages/sqlite/sqlite-2.8.17'
   create-stamp debian/debhelper-build-stamp
```
但并不影响后续的打包，因此推测可能是安装了构建依赖但未安装测试依赖。

# openEuler环境
## 安装工具
`openEuler`中需要安装有关deb的工具：
```bash
sudo dnf install dpkg dpkg-devel
```
有关`debhelper`的部分需要配置`oepkgs`镜像源，经过尝试，发现需要添加以下源：
```bash
# debhelper
sudo dnf config-manager --add-repo https://repo.oepkgs.net/openeuler/rpm/openEuler-22.03-LTS/extras/aarch64/
# po-debconf
sudo dnf config-manager --add-repo https://repo.oepkgs.net/openeuler/rpm/openEuler-22.03-LTS/compatible/aur/x86_64/
# dpkg-perl
sudo dnf config-manager --add-repo https://repo.oepkgs.net/openeuler/rpm/openEuler-22.03-LTS/compatible/f33/x86_64/

dnf clean all && dnf makecache
dnf install --nogpgcheck debhelper
```

## 获取sqlite3源码
```bash
wget https://repo.huaweicloud.com/ubuntu/pool/main/s/sqlite3/sqlite3_3.22.0-1.dsc
wget https://repo.huaweicloud.com/ubuntu/pool/main/s/sqlite3/sqlite3_3.22.0.orig.tar.xz
wget https://repo.huaweicloud.com/ubuntu/pool/main/s/sqlite3/sqlite3_3.22.0.orig-www.tar.xz
wget https://repo.huaweicloud.com/ubuntu/pool/main/s/sqlite3/sqlite3_3.22.0-1.debian.tar.xz
```
随后解压缩出源码和`debian`目录:
```bash
tar -xJf sqlite3_3.22.0.orig.tar.xz
tar -xJf sqlite3_3.22.0-1.debian.tar.xz -C sqlite3_3.22.0
```

## 安装sqlite3依赖
`sqlite3`的`control`文件的`Build-Depends`有以下内容:
```
Build-Depends: debhelper (>= 10), autoconf (>= 2.59), libtool (>= 1.5.2), automake, chrpath, libreadline-dev, tcl8.6-dev
```
前面四个都已经完成了安装，安装`chrpath`时使用的是先前指定的oepkgs源，因此也需要添加`--nogpgcheck`参数。
`libreadline-dev`和`tcl8.6-dev`需要这样安装:
```bash
sudo dnf install readline-devel tcl-devel
```

## 执行fakeroot debian/rules build
在执行`dh_update_autotools_config`阶段出现了大量的错误。首先是缺少`config.guess`文件。
```bash
dh_update_autotools_config
cp: 无法获取'/usr/share/misc/config.guess'的文件状态(stat): No such file or directory
db_update_autotools_config: error: cp -f /usr/share/misc/config.guess ./config.guess returned exit code 1
```
创建该文件后该错误消失，同理创建`/usr/share/misc/config.sub`。

随后出现了另一个错误:
```bash
dh_update_autotools_config
./configure --prefix=/usr --mandir="/usr/share/man" \
  --build x86_64-linux-gnu --with-tcl=/usr/lib/x86_64-linux-gnu/tcl8.6 --enable-threadsafe \
  --enable-load-extension \
  --enable-json1 \
  --enable-fts4 \
  --enable-fts5 \
  --libdir=\${prefix}/lib/x86_64-linux-gnu \
  --libexecdir=\${libdir}/sqlite3 \
  TCLLIBDIR=/usr/lib/tcltk/sqlite3 \
  `if (echo | grep -q debug) then echo "--enable-debug"; else echo ""; fi`
configure: loading site script /usr/share/config.site
checking build system type...
configure: error: invalid value of canonical build
make: *** [debian/rules:56: configure-stamp] 错误 1
```
首先怀疑是没有tcl的路径，于是利用命令`rpm -ql tcl`查看安装，发现类似的文件`/usr/lib64/tcl8.6`，将该文件夹复制到对应路径后并未解决问题。
后面还有一个`tcltk`文件夹，但通过`find /usr -name tcltk -type d`并未找到该文件夹。