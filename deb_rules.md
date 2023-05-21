本篇基于[Debian policy](https://www.debian.org/doc/debian-policy/ch-source.html#main-building-script-debian-rules), 概括了`deb`包中`debian/rules`文件的内容和格式。

该文件一定是一个可执行的makefile，用于编译源包并产生二进制包。以`#!/usr/bin/make -f`为第一行。

## build (required)
`build` target会执行所有的设置(`configuration`)并编译包。
- 如果源文件树会生成多个二进制包，那么可以提供相应数量的`target`（如`build-a`和`build`等等），此时`build`没有任何作用。
- `build`不能需要root权限
- `build`可能需要执行[clean](#clean-required)

## build-arch (required) build-indep (required)
`build-arch`和`build-indep`分别用于编译架构相关和架构无关的包。即`Achitecture`字段不为`all`的包需要`build-arch`，否则需要`build-indep`。
而`biuld` target要么依赖于这两个包，要么执行相同的操作。
- `build-arch`和`build-indep`不能需要root权限

## binary (required) binary-arch (required) binary-indep (required)
`binary`是用户从源包产生二进制包所需要的全部操作。它分为两部分：`binary-arch`用于特定架构，`binary-indep`用于架构无关的包。
`binary`常常只包含`binary-arch`和`binary-indep`的依赖，而不包含任何操作。
所有的`binary-*` target都依赖于`build` target, 或者对应的`build-arch`和`build-indep` target。
- `binary `可能需要root权限

## clean (required)
`clean`用于除去除了`binary`运行时生成的输出文件以外所有`build`和`binary`产生的效果。
- `clean`可能需要root权限

## patch (optional)
额外的操作

## make变量
- `DEB_*_ARCH` Debian architecture
- `DEB_*_ARCH_CPU` Debian CPU name
- `DEB_*_ARCH_BITS` Debian CPU pointer size in bits
- `DEB_*_ARCH_ENDIAN` Debian CPU endianness
- `DEB_*_ARCH_OS` Debian System name
- `DEB_*_GNU_TYPE` GNU style architecture specification string
- `DEB_*_GNU_CPU` CPU part of `DEB_*_GNU_TYPE`
- `DEB_*_GNU_SYSTEM` System part of `DEB_*_GNU_TYPE`

这里`*`可以是`BUILD`,`HOST`或者`TARGET`

## DEB_BUILD_OPTIONS
这个变量包含许多`flag`来改变包是如何编译并建立的。
- `nocheck` 不运行任何由包提供的build-time test
- `nodoc` 跳过所有只生成文档的步骤
- `noopt` 包编译时选择最小优化
- `nostrip` 安装过程中debug标志不会从二进制文件中去除
- `parellel=n` 使用n个并行的进程来建包
- `terse` 输出更加简洁

官方示例：
```Makefile
INSTALL_FILE    = $(INSTALL) -p    -o root -g root  -m  644
INSTALL_PROGRAM = $(INSTALL) -p    -o root -g root  -m  755
INSTALL_SCRIPT  = $(INSTALL) -p    -o root -g root  -m  755
INSTALL_DIR     = $(INSTALL) -p -d -o root -g root  -m  755

ifneq (,$(filter noopt,$(DEB_BUILD_OPTIONS)))
    CFLAGS += -O0
else
    CFLAGS += -O2
endif
ifeq (,$(filter nostrip,$(DEB_BUILD_OPTIONS)))
    INSTALL_PROGRAM += -s
endif
ifneq (,$(filter parallel=%,$(DEB_BUILD_OPTIONS)))
    NUMJOBS = $(patsubst parallel=%,%,$(filter parallel=%,$(DEB_BUILD_OPTIONS)))
    MAKEFLAGS += -j$(NUMJOBS)
endif

build:
        # ...
ifeq (,$(filter nocheck,$(DEB_BUILD_OPTIONS)))
        # Code to run the package test suite.
endif
```

## Rules-Requires-Root
builder(如`dpkg-buildpackage`)在执行`debian/rules`时可能没有给root权限，而这个命令可以使特殊的一些子命令获得(fake)root权限。 
*gain root command*通过`DEB_GAIN_ROOT_CMD`环境变量传递给建包脚本。
官方示例：
```sh
# Command "sudo", with arguments "-nE" and "--"
export DEB_GAIN_ROOT_CMD='sudo -nE --'
# Command "fakeroot" with the single argument "--"
export DEB_GAIN_ROOT_CMD='fakeroot --'
```
使用*gain root command`:
```sh
# sh-syntax (assumes set -e semantics for error handling)
$DEB_GAIN_ROOT_CMD some-cmd --which-requires-root

# perl
my @cmd = ('some-cmd', '--which-requires-root');
unshift(@cmd, split(' ', $ENV{DEB_GAIN_ROOT_CMD})) if $ENV{DEB_GAIN_ROOT_CMD};
system(@cmd) == 0 or die("@cmd failed");
```
