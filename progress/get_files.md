# 获取待安装的文件结构
本阶段计划编写一个`python`脚本，用于通过对源码包执行某些命令，最后提取出待安装的文件结构。

## 设计
尝试发现，在执行`fakeroot debian/rules binary`时，不同的包会执行不同的命令，但如果在中间插入无关的指令实际上并不会产生别的影响。因此，可以先确定一个通用的有序的命令集。

总体实现与手动执行指令的过程类似，主要为以下步骤：
- 对`rules`文件进行解析，获取重载`override`的字段
- 根据上面的解析内容，替换待执行的命令
- 依次执行命令
- 获取文件结构

## 实验
`get_files.py`脚本能够成功提取出大多数包的文件结构，在Ubuntu环境下，对`dh-python`、`nghttp2`、`zip`、`nginx`、`redis`、`tmux`这些包进行了测试，文件结构均完全正确。

## 问题
### 1. 特殊的rules文件
`sqlite3`打包流程与一般的不同，这是由于它的`rules`文件中并不是默认的`dh $@`，而是：
```makefile
...
build-arch: build-stamp
build-indep: build-stamp

build: build-arch build-indep
build-stamp:
...

install: build
...

binary-indep: build install
...

binary-arch: build install
...

binary: binary-indep binary-arch
```
因此在执行`fakeroot debian/rules binary`时，实际上也是在执行重载命令。而要提取出`binary`下的命令，不仅需要解析并筛选执行的命令，还涉及到各个`target`之间的依赖关系，情况更为复杂。

### 2. 执行参数
`fzf`包的`rules`文件如下：
```makefile
#!/usr/bin/make -f
export DH_GOPKG := github.com/junegunn/fzf

%:
    dh $@ --builddirectory=_build --buildsystem=golang --with=golang

override_dh_auto_install:
    dh_auto_install -- --no-source

override_dh_compress:
    dh_compress -Xkey-bingings -Xcompletion -Xfzf.vim
```
在执行`fakeroot debian/rules binary`时，可以发现每个命令后都加上了`-O--builddirectory=_build -O--buildsystem=golang`参数，但是没有`with`。哪些参数需要加，哪些参数不需要加？
另一个问题是，在手动执行`fakeroot debian/rules override_dh_auto_install`时，参数`--no-source`无法识别。