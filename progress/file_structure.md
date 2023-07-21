# 缘由
由于在执行`fakeroot debian/rules binary`打包时，大概率会出现难以解决的兼容性问题；并且我们实际上只需要获取到所需要安装的文件结构，对应于`spec`文件的`%files`字段，因此只需要找到获取文件结构的方法即可。

# dh binary的展开
根据debian官方文档中有关`debian`目录下文件和打包命令的[介绍](https://www.debian.org/doc/manuals/maint-guide/dreq.zh-cn.html)，可以知道`fakeroot debian/rules binary`实际上是执行了一系列命令，即：
```
dh_testroot
dh_prep
dh_installdirs
dh_auto_install
dh_install
dh_installdocs
dh_installchangelogs
dh_installexamples
dh_installman
dh_installcatalogs
dh_installcron
dh_installdebconf
dh_installemacsen
dh_installifupdown
dh_installinfo
dh_installinit
dh_installmenu
dh_installmime
dh_installmodules
dh_installlogcheck
dh_installlogrotate
dh_installpam
dh_installppp
dh_installudev
dh_installwm
dh_installxfonts
dh_bugfiles
dh_lintian
dh_gconf
dh_icons
dh_perl
dh_usrlocal
dh_link
dh_compress
dh_fixperms
dh_strip
dh_makeshlibs
dh_shlibdeps
dh_installdeb
dh_gencontrol
dh_md5sums
dh_builddeb
```
其中，[dh_installdirs](https://manpages.debian.org/testing/debhelper/dh_installdirs.1.en.html)根据`package.dirs`文件在`debian`目录下创建安装所需要的子文件夹，由于`dh_install*`命令基本都会保证文件夹的创建，因此`dh_installdirs`一般不需要手动执行。

[dh_auto_install](https://manpages.debian.org/jessie/debhelper/dh_auto_install.1.en.html)则自动根据项目中的Makefile或setup.py等进行安装，如果只有一个二进制包，则安装到`debian/package`目录下，如果有多个二进制包，则安装到`debian/tmp`目录下。

# 例子
## dh-di
`dh-di`这个包非常简单，在build之后没有产生任何`.dirs`或`.install`文件，`rules`文件也只有默认的`%:`规则，因此可以认为此时的命令均执行默认行为。

执行`dh_installdirs`后，`debian`目录下会出现`dh-di`文件夹，此时：
```bash
> tree debian/dh-di
debian/dh-di

0 directories, 0 files
```
再执行`dh_auto_install`后，会将对应内容安装到该目录下：
```bash
> tree debian/dh-di
debian/dh-di
└── usr
    ├── bin
    │   ├── dh_di_kernel_gencontrol
    │   ├── dh_di_kernel_install
    │   └── dh_di_numbers
    └── share
        └── perl5
            └── vendor_perl
                └── Debian
                    └── Debhelper
                        └── Sequence
                            └── d_i.pm

8 directories, 4 files
```
可以发现`dh_auto_install`主要是将对应的`bin`文件放入对应文件夹，而文档等内容仍需要执行`dh_installdocs`等命令。

## nghttp2
`dh_di`是单个包的情况，而`nghttp2`含有多个子包，因此在执行dh_auto_install`时会将文件安装到`debian/tmp`目录下：
```bash
> tree debian/tmp  
debian/tmp
└── usr
    ├── bin
    │   ├── deflatehd
    │   ├── h2load
    │   ├── inflatehd
    │   ├── nghttp
    │   ├── nghttpd
    │   └── nghttpx
    ├── include
    │   └── nghttp2
    │       ├── nghttp2.h
    │       └── nghttp2ver.h
    ├── lib
    │   └── x86_64-linux-gnu
    │       ├── libnghttp2.a
    │       ├── libnghttp2.la
    │       ├── libnghttp2.so -> libnghttp2.so.14.24.2
    │       ├── libnghttp2.so.14 -> libnghttp2.so.14.24.2
    │       ├── libnghttp2.so.14.24.2
    │       └── pkgconfig
    │           └── libnghttp2.pc
    └── share
        ├── doc
        │   └── nghttp2
        │       └── README.rst
        ├── man
        │   └── man1
        │       ├── h2load.1
        │       ├── nghttp.1
        │       ├── nghttpd.1
        │       └── nghttpx.1
        └── nghttp2
            └── fetch-ocsp-response

13 directories, 20 files
```

## zip
`zip`包与上述两个包不同，直接执行`dh_installdirs`和`dh_auto_install`只是生成了默认的文件夹，没有安装任何文件：
```bash
> tree debian/zip
debian/zip

0 directories, 0 files
```
经过研究我发现，这是由于在`debian/rules`文件中，`dh_auto_install`命令被重写了，其`debian/rules`文件如下：
```makefile
CC = gcc
CFLAGS := `dpkg-buildflags --get CFLAGS` -Wall -I. -DUNIX
LDFLAGS := `dpkg-buildflags --get LDFLAGS`
CPPFLAGS := `dpkg-buildflags --get CPPFLAGS`

%:
        dh $@

override_dh_auto_clean:
        $(MAKE) -f unix/Makefile clean

override_dh_auto_configure:
        LDFLAGS="$(LDFLAGS)" sh unix/configure "$(CC)" "$(CFLAGS) $(CPPFLAGS)"

override_dh_auto_build:
        $(MAKE) -f unix/Makefile generic

override_dh_auto_install:
        $(MAKE) -f unix/Makefile install prefix=`pwd`/debian/tmp/usr

override_dh_installchangelogs:
        dh_installchangelogs -XCHANGES

override_dh_compress:
        dh_compress -XTODO -XWHATSNEW
```
注意到这里包含有`override_dh_auto_install`字段，尝试手动执行这里的命令：
```bash
> make -f unix/Makefile install prefix=$(pwd)/debian/tmp/usr
```
查看`debian/tmp`目录下的文件结构，发现此时已经完成了这步安装：
```bash
> tree debian/tmp 
debian/tmp
└── usr
    ├── bin
    │   ├── zip
    │   ├── zipcloak
    │   ├── zipnote
    │   └── zipsplit
    └── man
        └── man1
            ├── zip.1
            ├── zipcloak.1
            ├── zipnote.1
            └── zipsplit.1

4 directories, 8 files
```
