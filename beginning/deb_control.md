本篇基于[Debian Policy Manual](https://www.debian.org/doc/debian-policy/ch-controlfields.html)，概括`Debian control files`的一些基本概念和规范。
# Syntax
- 空格分割每一节`stanza`
- 每一节由若干数据字段`data fields`构成
  `field_name:data/value` 名字不允许空格，中间允许空格
- 注释以`#`开头
- 空值只可能是源包的`control file`, 如`debian/control`。这样的字段可以忽略
- 有三种可能的字段类型：
  1. `simple` 单行键值对
  2. `folded` 可能横跨多行的逻辑表达式，第二行及以后（`continuation lines`）以空格或tab开头
  3. `multiline`
# Source package control files 
**debian/control** 文件包含着有关源包和它生成的二进制包的最重要的信息。 
该文件的第一节包含着源包的描述信息，后面的每一节包含着一个二进制包的描述信息。 
第一节`general stanza`由以下字段组成：
- [source](#source) (mandatory)
- [Maintainer](#maintainer) (mandatory)
- [Uploaders](#uploaders)
- [Section](#section) (recommended)
- [Priority](#priority) (recommended)
- [Build-Depends et al](#package-interrelationship-fields)
- [Standards-Version](#standards-Version) (mandatory)
- [Homepage](#homepage)
- [Version Control System (VCS) fields](#version-control-system-vcs-fields)
- [Testsuite](#testsuite)
- [Rules-Requires-Root](#rules-requires-root)

后面的每一节`binary stanza`由以下字段组成：
- [Package](#package) (mandatory)
- [Architecture](#architecture) (mandatory)
- [Section](#section) (recommended)
- [Priority](#priority) (recommended)
- [Essential](#essential)
- [Build-Depends et al](#package-interrelationship-fields)
- [Description](#description) (mandatory)
- [Homepage](#homepage)
- `Built-Using`
- [Package-Type](#package-type)

以上内容详细见下

# Binary package control files
**DEBIAN/control** 文件包含着关于二进制包的重要信息。它只有一节内容，包含以下字段：
- [Package](#package) (mandatory)
- [source](#source)
- `Version` (mandatory)
- [Section](#section) (recommended)
- [Priority](#priority) (recommended)
- [Architecture](#architecture) (mandatory)
- [Essential](#essential)
- [Build-Depends et al](#package-interrelationship-fields)
- [Installed-Size](#installed-size)
- `Maintainer` (mandatory)
- [Description](#description) (mandatory)
- [Homepage](#homepage)
- `Built-Using`

# Debian source control files
**.dsc** 文件包含着关于源包的重要信息。它是由`dpkg-source`命令生成的，只有一节内容(possibly surrounded by an OpenPGP signature)，包含以下字段：
- `Format` (mandatory)
- [source](#source) (mandatory)
- [Binary](#binary)
- [Architecture](#architecture)
- `Version` (mandatory)
- `Maintainer` (mandatory)
- [Uploaders](#uploaders)
- [Homepage](#homepage)
- [Version Control System (VCS) fields](#version-control-system-vcs-fields)
- [Testsuite](#testsuite)
- [Dgit](#dgit)
- [Standards-Version](#standards-Version) (mandatory)
- [Build-Depends et al](#package-interrelationship-fields)
- [Package-List](#package-list) (recommended)
- `Checksums-Sha1 and Checksums-Sha256` (mandatory)
- `Files` (mandatory)

# Debian changes files
**.changes** 文件用于更新二进制包的版本。它是由`dpkg-genchanges`命令生成的，只有一节内容(possibly surrounded by an OpenPGP signature)，包含以下字段：
- `Format` (mandatory)
- `Date` (mandatory)
- [source](#source) (mandatory)
- `Binary` (mandatory)
- [Architecture](#architecture) (mandatory)
- `Version` (mandatory)
- `Distribution` (mandatory)
- `Urgency` (recommended)
- `Maintainer` (mandatory)
- [Changed-By](#changed-by)
- [Description](#description) (mandatory)
- [Closes](#closes)
- `Changes` (mandatory)
- `Checksums-Sha1 and Checksums-Sha256` (mandatory)
- `Files` (mandatory)

# List of fields
## Source
在`debian/control`和`.dsc`文件中，该字段只包含源包的名字。 
在二进制包control file或者`.changes`文件中，名字后可以有加上括号的版本号

## Maintainer
该字段包含着源包的维护者的名字和邮件地址。
格式为： `name <email>`

## Uploaders
格式与[**Maintainer**](#maintainer)相同，但是可以有多个(以逗号分隔)

## Changed-By
格式与[**Maintainer**](#maintainer)相同，通常只有一个

## Section
该字段将源包或者二进制包分到一个类别中，多个以/分隔。

## Priority
该字段将源包或者二进制包分到不同的优先级中。

## Package
该字段包含着二进制包的名字。
名字的要求与[**Source**](#source)相同，但是可以有加上括号的版本号

## Architecture
该字段包含着二进制包的架构。
它的值可以是：
- 某个特定的架构，如`i386`或者`amd64`
- 使用`architecture wildcards`指定的一些架构
- `all`，表示所有架构
- `source`，表示源包

## Essential
该字段只能在二进制包control file中出现，包含着二进制包是否是`essential`的信息。

## Package interrelationship fields
多个包名用`，`分隔, 且可以使用`|`表示或关系（`alternative`）。 
版本选择可以采取以下形式：
- `<<` 严格低于
- `<=` 低于等于
- `=`  严格等于
- `>=` 高于等于
- `>>` 严格高于

架构确定需要以中括号`[]`括起来，多个架构以空格分隔。
架构选择可以使用`|`和`！`表示或关系和非关系。

### Depends
该字段包含着二进制包的运行时依赖。
### Recommands
除去一些特殊情况安装以外，所需要的包
### Suggests
声明相比其他一个或多个包，可能会更有用的包
### Enhances
与[**Suggests**](#suggests)类似，但是声明能够增强其他包的功能的包
### Pre-Depends
与[**Depends**](#depends)类似，但是在安装该包之前，必须先安装这些包

### Breaks
声明了安装后会损坏的包
### Conflicts
声明了安装后会冲突的包，卸载后才能继续安装
### Provides
声明了该包提供的功能，可以用于满足其他包的依赖，如原先依赖`foo`的包，可以依赖`bar`，而`bar`提供了`foo`的功能
```
Package: foo
Depends: bar
```
之后有人开发了`bar-plus`，它提供了`bar`的功能，那么可以这样写：
```
Package: bar-plus
Provides: bar
```
### Replaces
需要替代的包

## Stardards-Version
编译该包所遵循的Debian Policy的版本号

## Version
格式为: `[epoch:]upstream_version[-debian_revision]`
- `epoch`是一个非负整数，用于比较版本号，如果没有该字段，那么默认为0
- `upstream_version` 版本号的主要部分
- `debian_revision` 用于区分Debian的版本，如果没有该字段，那么默认为0

## Description
该字段包含着关于包的描述信息，包含单行的短描述和多行的长描述。

## Distribution
在`.changes`文件中，该字段包含着二进制包的目标发行版。

## Date
在`.changes`文件中，该字段包含着二进制包的编译时间。

## Format
在`.dsc`和`.changes`文件中，该字段包含着文件的格式版本号。

## Urgency
`low`, `medium`, `high` or `emergency`中的一个，表示升级的紧急程度。
```
Urgency: low (HIGH for users of diversions)
```

## Changes
描述前后版本的差异

## Binary
在`.dsc`文件中，该字段列出了源包生成的二进制包，多个以逗号分隔。
在`.changes`文件中，该字段列出了上传的二进制包名，多个以空格分隔。

## Installed-Size
在二进制包control file中，该字段包含着二进制包安装后所占用的空间大小。

## Files
包含各文件的信息，每行包含以下字段：
- `md5sum`
- `size`
- `section`  (in `.changes` files only)
- `priority` (in `.changes` files only)
- `filename`

## Closes
以空格分隔的Bug号，表示该版本修复了哪些Bug

## Homepage
包的主页，只是一个url而没有任何附加字符如<>

## Checksums-Sha1 and Checksums-Sha256
该字段包含着一系列文件的SHA1和SHA256的校验和和大小。

## Version Control System (VCS) fields
版本控制信息，包含以下字段：
- Vcs-Browser 代码仓库的url
- Vcs-<type>

## Package-List
列出在每一个架构下，从源包能构建出的包

## Package-Type
- `deb` binary package
- `udeb` micro binary package

## Dgit
该字段包含着dgit的信息，用于dgit的上传。

## Testsuite
该字段包含着测试套件的名字，用于自动化测试。以逗号分隔

## Rules-Requires-Root
该字段包含着构建该包所需要的root权限的信息。
- `no` 不需要root权限
- `binary-targets` (default)
- 一系列以逗号分隔的关键词([**keywords**](#keywords))

## Remarks
标记为不能root

## Keywords
格式为: `<namespace>/<case>`

# User-defined fields
一般被忽略
