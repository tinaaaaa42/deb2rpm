本篇内容基于deb包源码包内容的[官方文档](https://www.debian.org/doc/debian-policy/ch-controlfields.html)和control文件内容的[官方文档](https://www.debian.org/doc/debian-policy/ch-controlfields.html)，对照rpm包spec文件内容的[官方文档](https://rpm-software-management.github.io/rpm/manual/spec.html)，对比两者在*元数据*上的差异。

# Source字段
## 相同内容
| deb | spec |
| :---: | :---: |
| Source | Name |
| Homepage | URL |

## 不同内容
- **Sections**和**Groups**
两者含义相同，但具体分类不同。分别可以参考[Sections](https://www.debian.org/doc/debian-policy/ch-archive.html#s-subsections)和[Groups](https://fedoraproject.org/wiki/RPMGroups)。
但由于两者都是可选的，所以可以不写。
- **依赖相关**
在键的内容上，两者具有对应关系：

| deb | spec |
| :---: | :---: |
| Build-Depends | BuildRequires |
| Depends | Requires |
| Breaks | Conflicts |
| Replace | Obsoletes |
| Provides | Provides |
| Recommends | Recommends |
| Suggests | Suggests |
<!-- | Enhances | Enhances | -->

deb中的`Pre-Depends`字段，spec中没有对应字段，暂时统一均使用`Requires`。另外，deb字段键名均可加上`-Indep`或`-Arch`后缀，分别表示独立于架构和依赖于架构，spec中可以通过`%ifarch`和`%ifnarch`来实现，也可以忽略。

而在值的内容上，deb会使用`|`来表示或关系，而spec中则没有对应的表示方法，暂时确定选择第一个值。

## deb独有
- **Maintainer & Uploaders**
spec文件中也有`Packager`字段，但由于是可选的，一般并不会写
- **Priority**
表示该包的重要程度，spec文件中没有对应字段
- **Standards-Version**
表示使用的debian标准版本，spec文件中没有对应字段
- **Vcs-Brower & Vcs-Git**
spec文件中也有`VCS`字段，但由于是可选的，一般并不会写
- **Testsuite**
由`dpkg`自动生成的测试相关的字段，spec文件中没有对应字段
- **Rules-Requires-Root**
表示`debian/rules`文件中是否需要root权限，spec文件中没有对应字段，暂时统一均使用`fakeroot`

# Package子包字段
## 相同内容
| deb | spec |
| :---: | :---: |
| Package | %package |
| Architecture | BuildArch |

## 不同内容
- **Section & Group**
同上
- **依赖相关**
同上
- **Description**
deb中的`Description`字段第一行内容对应spec中的`Summary`字段，其余内容对应spec中的`%description`字段
- **Version**
该字段的标准格式是`[epoch:]upstream_version[-debian_revision]`，其中`epoch`和`debian_revision`是可选的，三者分别对应spec文件中的`Epoch`、`Version`和`Release`字段。
`debian-revision`有两者格式，一种是纯数字，可以直接对应；而另一种是形如`1build1`或者`1ubuntu1`，这种情况下，`1`对应spec中的`Release`字段，`build1`或者`ubuntu1`对应spec中的`%dist`字段。

## deb独有
- **Priority**
同上
- **Essential**
较为少见，如果为`yes`则无法删除该包，spec文件中没有对应字段
- **Built-Using**
表示该包是由哪些包构建的，需要添加到`BuildRequires`中

# spec文件
除了以上内容，spec文件还有以下的元数据内容：
## License
deb包中的License存在`debian/copyright`文件中，其格式信息可以参考[官方文档](https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/)，其大致格式为：
```
Files:
 *
Copyright: 1975-2010 Ulla Upstream
License: GPL-2+

Files:
 debian/*
Copyright: 2010 Daniela Debianizer
License: GPL-2+

Files:
 debian/patches/fancy-feature
Copyright: 2010 Daniela Debianizer
License: GPL-3+

Files:
 */*.1
Copyright: 2010 Manuela Manpager
License: GPL-2+
```
而spec文件中的`License`字段只需要写上License的名称即可，并用`and`连接，如`GPL-2+ and BSD`。

## Source
源代码文件

## Patch
deb包的patch文件存在于`debian/patch`目录下，在spec文件中加上对应文件名即可，因为dh脚本会自动打patch

## %files
文件列表

## %changelog
deb包中的changelog存在`debian/changelog`文件中，可以通过`dpkg-parsechangelog`命令解析获取最新的内容。具体格式如下：
```
package (version) distribution(s); urgency=urgency
  [optional blank line(s), stripped]
  * change details
  more change details
  [blank line(s), included in output of dpkg-parsechangelog]
  * even more change details
  [optional blank line(s), stripped]
 -- maintainer name <email address>[two spaces]  date
```
而spec文件中的`%changelog`字段格式如下：
```spec
* date maintainer <email address> - version-1
- change details
- more change details
* date maintainer <email address> - version-2
- even more change details
```
