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
## clean (required)

## patch (optional)

