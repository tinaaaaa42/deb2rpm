# dh-di
首先尝试在openEuler环境中打出简单的`deb`包，考虑到要使依赖尽可能的少，我选择先打出`dh-di`包。根据其control文件的说明，这个包只有`debhelper`和`dh-perl`的依赖。
```bash
// 获取源码包
wget https://repo.huaweicloud.com/ubuntu/pool/main/d/dh-di/dh-di_11.dsc
wget https://repo.huaweicloud.com/ubuntu/pool/main/d/dh-di/dh-di_11.tar.xz

// 解压出源码
tar -xJf dh-di_11.tar.xz

// build
cd dh-di-11
fakeroot debian/rules build

// 打包
fakeroot debian/rules binary
```
打包过程中出现了以下错误：
```bash
Can't exec "dh_strip_nondeterminism": No such file or directory at /usr/share/perl5/vendor_perl/Debian/Debhelper/SequencerUtil.pm line 490
make: *** [debian/rules:3: binary] Error 255
```

通过查询资料，我在[https://github.com/scylladb/scylladb/commit/5bf9a03d65dea12ae63bb32c28fa611594d7e9ff](https://github.com/scylladb/scylladb/commit/5bf9a03d65dea12ae63bb32c28fa611594d7e9ff)发现了这个问题的原因和解决方法：
> dist/debian: skip running dh_strip_nondeterminism
On some Fedora environment dh build tries to run
dh_strip_nondeterminism, and fails sice Fedora does not provide such command.

只需如下修改`rules`文件:
```diff
+ override_dh_strip_nondeterminism:
+
%:
	dh $@
```

随后再次执行`fakeroot debian/rules binary`，成功打出deb包。

# nghttp2
再尝试打一个略为复杂的包`nghttp2`。其`control`文件中的依赖如下：
```
Build-Depends: debhelper (>= 13), 
               debhelper-compat (= 13),
               libc-ares-dev, 
               libcunit1-dev <!nocheck>,
               libev-dev, 
               libjansson-dev,
               libjemalloc-dev [!huid-i386],
               libssl-dev, 
               libsystemd-dev, 
               libxml2-dev, 
               pkg-config, 
               zlib1g-dev (>= 1.2.3)
Build-Depends-Indep: python3-sphinx,
                     python3-sphinx-rtd-theme
```
而要在openEuler中安装，名称有少许不同：
```bash
sudo dnf install c-ares-devel libcunit-devel libev-devel jansson-devel jemalloc-devel openssl-devel systemd-devel libxml2-devel zlib-devel
sudo dnf install python3-sphinx python3-sphinx_rtd_theme
```
部分包是通过`oepkgs`源下载的，同样需要添加`--nogpgcheck`参数。

获取源码包：
```bash
wget https://repo.huaweicloud.com/ubuntu/pool/main/n/nghttp2/nghttp2_1.54.0-1.dsc
wget https://repo.huaweicloud.com/ubuntu/pool/main/n/nghttp2/nghttp2_1.54.0.orig.tar.xz
wget https://repo.huaweicloud.com/ubuntu/pool/main/n/nghttp2/nghttp2_1.54.0-1.debian.tar.xz
```
解压缩：
```bash
tar -xJf nghttp2_1.54.0.orig.tar.xz
tar -xJf nghttp2_1.54.0-1.debian.tar.xz -C nghttp2-1.54.0
```
修改`rules`文件：
```diff
...
+ override_dh_strip_nondeterminism:
+
%:
    dh $@
```
随后执行`fakeroot debian/rules build`，成功构建，但在打包时出现了以下错误：
```bash
    dh_strip -a
    dh_makeshlibs -a
    dh_shlibdeps -a
dpkg-shlibdeps: error: no dependency information found for /lib64/libc.so.6 (used by debian/libnghttp2-14/usr/lib/x86_64-linux-gnu/libnghttp2.so.14.24.2)
Hint: check if the library actually comes from a package.
dh_shlibdeps: error: dpkg-shlibdeps -Tdebian/libnghttp2-14.substvars debian/libnghttp2-14/usr/lib/x86_64-linux-gnu/libnghttp2.so.14.24.2 returned exit code 255
dh_shlibdeps: error: Aborting due to earlier error
make: *** [debian/rules:66: binary] 错误 255
```
根据错误提示，是因为没有使用正确的`libc.so`库。
