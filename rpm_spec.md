本篇基于[RPM package guide](https://rpm-packaging-guide.github.io/#what-is-a-spec-file), 概括了RPM包中`SPEC`文件的内容和格式。

# 什么是SPEC文件？
`SPEC`文件通过定义一系列`section`来告诉build system如`rpmbuild`如何构建RPM包。这些`section`定义在前言`Preamble`和主题`Body`部分。`Preamble`部分包含一系列`Body`中可能使用的元数据，而`Body`包含指令的主要部分。

# Preamble items
- `Name` 包的`base name`，与`SPEC`文件应相符
- `Version` 软件版本
- `Release` 该版本的发布次数
- `Summary` 单行摘要
- `License` 证书
- `URL` 获取关于该包的更多信息的完整URL
- `Source0` 路径或URL，指向软件包的源代码。可以有`Source1`，`Source2`等
- `Patch0` 路径或URL，指向补丁文件。可以有`Patch1`，`Patch2`等
- `BuildArch` 指定架构或`noarch`，默认为本机架构
- `BuildRequires` 指定构建该包所需的其他包
- `Requires` 指定运行该包所需的其他包
- `ExclusiveArch` 指定不兼容的架构
`NVR`即`Name-Version-Release`，是一个包的唯一标识符。
如：
```
rpm -q python
python-2.7.5-88.el7.x86_64
```

# Body items
- `%description` 包的详细描述
- `%prep` 为构建做准备，如解压源代码, 这一部分可以包含一个shell脚本
- `%build` 构建软件包（转换为机器码或二进制码）
- `%install` 将`%builddir`（一般是`~/rpmbuild/BUILD`）中需要的组件复制到`%buildroot`(一般是`~/rpmbuild/BUILDROOT`)中去。只会在创建包的时候执行这部分命令。
- `%check` 测试，通常包含单元测试
- `%files` end user's system中会安装的文件
- `%changelog` 不同`Version`或者`Release`间的改变记录

# Advanced items
如[Scriptlets and Triggers](https://rpm-packaging-guide.github.io/#trigger-and-scriptlets)

# BuildRoots
在RPM包中，`buildroot`相当于`chroot`环境。

# RPM Macros
rpm宏也是一直文字的直接替代。
如：
```
$ rpm --eval %{_bindir}
/usr/bin
```
一个常见的宏是`%{?dist}`，即"distribution tag"，表示发行版本
```bash
# On a RHEL 7.x machine
$ rpm --eval %{?dist}
.el7

# On a Fedora 23 machine
$ rpm --eval %{?dist}
.fc23
```

# [几个例子](https://rpm-packaging-guide.github.io/#working-with-spec-files)

下面以三个代表性的例子来展示`SPEC`文件，分别是bash脚本`bello`，python程序`pello`和c程序`cello`

## bello
```
Name:           bello
Version:        0.1
Release:        1%{?dist}
Summary:        Hello World example implemented in bash script

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

Requires:       bash

BuildArch:      noarch

%description
The long-tail description for our Hello World Example implemented in
bash script.

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org> - 0.1-1
- First bello package
- Example second item in the changelog for version-release 0.1-1
```
几点说明：
- 由于bash脚本不需要build,所以不需要`BuildRequires`
- `%changelog`第一行的格式为：
```
* Day-of-Week Month Day Year Name Surname <email> - Version-Release
```

## pello
```
Name:           pello
Version:        0.1.1
Release:        1%{?dist}
Summary:        Hello World example implemented in python

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

BuildRequires:  python
Requires:       python
Requires:       bash

BuildArch:      noarch

%description
The long-tail description for our Hello World Example implemented in
Python.

%prep
%setup -q

%build

python -m compileall %{name}.py

%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}

cat > %{buildroot}%{_bindir}/%{name} <<-EOF
#!/bin/bash
/usr/bin/python /usr/lib/%{name}/%{name}.pyc
EOF

chmod 0755 %{buildroot}%{_bindir}/%{name}

install -m 0644 %{name}.py* %{buildroot}/usr/lib/%{name}/

%files
%license LICENSE
%dir /usr/lib/%{name}/
%{_bindir}/%{name}
/usr/lib/%{name}/%{name}.py*

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org> 
- 0.1.1-1
- First pello package
```

## cello
```
Name:           cello
Version:        1.0
Release:        1%{?dist}
Summary:        Hello World example implemented in C

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

Patch0:         cello-output-first-patch.patch

BuildRequires:  gcc
BuildRequires:  make

%description
The long-tail description for our Hello World Example implemented in
C.

%prep
%setup -q

%patch0

%build
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue May 31 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.0-1
- First cello package
```
几点说明：
- 由于该程序不需要除了C标准库以外的资源，`rpmbuild`会自动处理运行时的包，所以`Requires`可以省略
- `%{?_smp_mflags}`和`%make_install`宏都是`rpmdev-newspec`命令提供的
