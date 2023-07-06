# Ubuntu迁移工具预研

## 目标

+ deb包格式与rpm包的区别，包括依赖关系梳理等等





## RPM与DEB简单对比

### 包全名

> RPM：包名-版本号-发布次数-发行商-Linux平台-适合的硬件平台-包扩展名
>
> tar-1.26-35.el7.x86_64
>
> 包名：tar
>
> 版本号：1.26
>
> 发布次数：35
>
> 发行商：el7
>
> 硬件平台:x86_64



> DEB： 软件包名称 - 版本 - 修订号 - 平台 - 包扩展名
>
> tar_1.34+dfsg-1build3_amd64.deb
>
> 包名：tar
>
> 版本：1.34+dfsg
>
> 修订号：1build3
>
> 平台：amd64



### DEB包格式

#### tar_1.34+dfsg-1build3_amd64.deb



```bash
dpkg -X tar_1.34+dfsg-1build3_amd64.deb
cd tar 
dpkg -e ../tar_1.34+dfsg-1build3_amd64.deb
```



```bash
wangzheng@wangzheng-Virtual-Machine:~/test$ tree tar
tar
├── bin
│   └── tar
├── DEBIAN
│   ├── control
│   ├── md5sums
│   ├── postinst
│   └── prerm
├── etc
│   └── rmt -> /usr/sbin/rmt
└── usr
    ├── lib
    │   └── mime
    │       └── packages
    │           └── tar
    ├── sbin
    │   ├── rmt-tar
    │   └── tarcat
    └── share
        ├── doc
        │   └── tar
        │       ├── AUTHORS
        │       ├── changelog.Debian.gz
        │       ├── copyright
        │       ├── NEWS.gz
        │       ├── README.Debian
        │       └── THANKS.gz
        └── man
            ├── man1
            │   ├── tar.1.gz
            │   └── tarcat.1.gz
            └── man8
                └── rmt-tar.8.gz
```



```bash
wangzheng@wangzheng-Virtual-Machine:~/test/tar/DEBIAN$ cat control 
Package: tar
Version: 1.34+dfsg-1build3
Architecture: amd64
Essential: yes
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Installed-Size: 956
Pre-Depends: libacl1 (>= 2.2.23), libc6 (>= 2.34), libselinux1 (>= 3.1~)
Suggests: bzip2, ncompress, xz-utils, tar-scripts, tar-doc
Conflicts: cpio (<= 2.4.2-38)
Breaks: dpkg-dev (<< 1.14.26)
Replaces: cpio (<< 2.4.2-39)
Section: utils
Priority: required
Multi-Arch: foreign
Homepage: https://www.gnu.org/software/tar/
Description: GNU version of the tar archiving utility
 Tar is a program for packaging a set of files as a single archive in tar
 format.  The function it performs is conceptually similar to cpio, and to
 things like PKZIP in the DOS world.  It is heavily used by the Debian package
 management system, and is useful for performing system backups and exchanging
 sets of files with others.
Original-Maintainer: Janos Lenart <ocsi@debian.org>

```

+ 控制文件术语：[Chapter 7. Basics of the Debian package management system](https://www.debian.org/doc/manuals/debian-faq/pkg-basics.en.html)



### RPM包格式

#### tar-1.26-35.el7.x86_64 -> tar-1.26-35.el7.src.rpm

```bash
rpm -ivh tar-1.26-35.el7.src.rpm
```

p

```bash
[wangzheng@localhost ~]$ tree rpmbuild/
rpmbuild/
├── SOURCES
│   ├── tar.1
│   ├── tar-1.14-loneZeroWarning.patch
│   ├── tar-1.15.1-vfatTruncate.patch
│   ├── tar-1.17-wildcards.patch
│   ├── tar-1.22-atime-rofs.patch
│   ├── tar-1.23-oldarchive.patch
│   ├── tar-1.26-add-skip-old-files-option.patch
│   ├── tar-1.26-allow-extract-single-volume.patch
│   ├── tar-1.26-default-acls.patch
│   ├── tar-1.26-delay-dir-restore.patch
│   ├── tar-1.26-directory_with_remove-files.patch
│   ├── tar-1.26-docu-xattrs.patch
│   ├── tar-1.26-dont-segfault-with-disabled-selinux.patch
│   ├── tar-1.26-fix-symlink-eating-bug.patch
│   ├── tar-1.26-keep-directory-symlink-doc-and-test.patch
│   ├── tar-1.26-keep-directory-symlink.patch
│   ├── tar-1.26-large-sparse-file-listing.patch
│   ├── tar-1.26-non-deterministic-archive-detection.patch
│   ├── tar-1.26-pax-big-sparse-files.patch
│   ├── tar-1.26-posix-biguid.patch
│   ├── tar-1.26-restore-incremental-backups.patch
│   ├── tar-1.26-selinux-gnulib.patch
│   ├── tar-1.26-silence-gcc.patch
│   ├── tar-1.26-stdio.in.patch
│   ├── tar-1.26.tar.xz
│   ├── tar-1.26.tar.xz.sig
│   ├── tar-1.26-update-with-change-directory.patch
│   ├── tar-1.26-xattrs-exclude-include-repair.patch
│   ├── tar-1.26-xattrs-include-implies-xattrs.patch
│   ├── tar-1.26-xattrs.patch
│   ├── tar-1.26-xattrs-printing.patch
│   ├── tar-1.26-xattrs-skip-old-files-hangs.patch
│   └── tar-1.27-sparse-stat-detection.patch
└── SPECS
    └── tar.spec
```

+ .SEPC文件格式：[ Building RPMs](https://tldp.org/HOWTO/RPM-HOWTO/build.html)







### 参考资料

+ [Linux极简小知识：15、rpm包的介绍和命名规则](https://juejin.cn/post/7016621989133565989)

+ [deb包格式实例详解](https://juejin.cn/post/7167338717621780517)

+ [deb和rpm的解包和打包](http://3ms.huawei.com/km/blogs/details/1984761)

+ [deb打包流程步骤](https://blog.csdn.net/LvJzzZ/article/details/109452895)

+ [rpm打包流程步骤](https://blog.csdn.net/LvJzzZ/article/details/114328421)

+ [Building binary deb packages: a practical guide](https://www.internalpointers.com/post/build-binary-deb-package-practical-guide)

  



## Centos7.6(参考)

+ `x2openEuler`项目中的`x2openEuler-client.py`为例，`upgrade_check_collect`会生成所有RPM包的信息


  ```json
   "tar-1.26-35.el7.x86_64": {
      "files": [
        "/usr/bin/gtar", 
        "/usr/bin/tar", 
        "/usr/share/doc/tar-1.26", 
        "/usr/share/doc/tar-1.26/AUTHORS", 
        "/usr/share/doc/tar-1.26/COPYING", 
        "/usr/share/doc/tar-1.26/ChangeLog", 
        "/usr/share/doc/tar-1.26/ChangeLog.1", 
        "/usr/share/doc/tar-1.26/NEWS", 
        "/usr/share/doc/tar-1.26/README", 
        "/usr/share/doc/tar-1.26/THANKS", 
        "/usr/share/doc/tar-1.26/TODO", 
        "/usr/share/info/tar.info-1.gz", 
        "/usr/share/info/tar.info-2.gz", 
        "/usr/share/info/tar.info.gz", 
        "/usr/share/locale/bg/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/ca/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/cs/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/da/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/de/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/el/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/es/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/et/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/eu/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/fi/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/fr/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/ga/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/gl/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/hr/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/hu/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/id/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/it/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/ja/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/ko/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/ky/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/ms/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/nb/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/nl/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/pl/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/pt/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/pt_BR/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/ro/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/ru/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/sk/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/sl/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/sv/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/tr/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/uk/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/vi/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/zh_CN/LC_MESSAGES/tar.mo", 
        "/usr/share/locale/zh_TW/LC_MESSAGES/tar.mo", 
        "/usr/share/man/man1/gtar.1.gz", 
        "/usr/share/man/man1/tar.1.gz"
      ], 
      "src_pkg_name": "tar-1.26-35.el7.x86_64", 
      "require_pkg": [
        "libselinux-2.5-15.el7.x86_64", 
        "bash-4.2.46-31.el7.x86_64", 
        "glibc-2.17-260.el7.x86_64", 
        "libacl-2.2.51-14.el7.x86_64", 
        "info-5.1-5.el7.x86_64"
      ], 
      "provide_pkg": [
        "amanda-3.3.3-21.el7.x86_64", 
        "supermin5-5.1.19-1.el7.x86_64", 
        "libtool-2.4.2-22.el7_3.x86_64", 
        "libguestfs-1.38.2-12.el7.x86_64", 
        "ipa-server-4.6.4-10.el7.centos.x86_64", 
        "file-roller-3.28.1-2.el7.x86_64", 
        "open-vm-tools-10.2.5-3.el7.x86_64", 
        "abrt-retrace-client-2.1.11-52.el7.centos.x86_64", 
        "rpm-build-4.11.3-35.el7.x86_64", 
        "dracut-033-554.el7.x86_64"
      ], 
      "pkg_info": {
        "Group": "Applications/Archiving", 
        "Name": "tar", 
        "License": "GPLv3+", 
        "URL": "http://www.gnu.org/software/tar/", 
        "Relocations": "(not relocatable)", 
        "Install Date": "Wed 23 Nov 2022 02:09:55 AM CST", 
        "Build Host": "x86-01.bsys.centos.org", 
        "Source RPM": "tar-1.26-35.el7.src.rpm", 
        "Description": "", 
        "Build Date": "Wed 31 Oct 2018 04:29:09 AM CST", 
        "Epoch": "2", 
        "Version": "1.26", 
        "Architecture": "x86_64", 
        "Signature": "RSA/SHA256, Mon 12 Nov 2018 10:47:46 PM CST, Key ID 24c6a8a7f4a80eb5", 
        "Release": "35.el7", 
        "Vendor": "CentOS", 
        "Packager": "CentOS BuildSystem <http://bugs.centos.org>", 
        "Summary": "A GNU file archiving program", 
        "Size": "2838510"
      }, 
      "rpm_provides": [
        "/bin/gtar", 
        "/bin/tar", 
        "bundled(gnulib)", 
        "tar = 2:1.26-35.el7", 
        "tar(x86-64) = 2:1.26-35.el7"
      ], 
      "package_source": "", 
      "symbols": [], 
      "shell_command": [], 
      "rpm_conflicts": [], 
      "rpm_recommends": [], 
      "python_import": [], 
      "so_requires": {}, 
      "rpm_requires": {
        "libc.so.6(GLIBC_2.6)(64bit)": "glibc-2.17-260.el7.x86_64", 
        "libc.so.6(GLIBC_2.3)(64bit)": "glibc-2.17-260.el7.x86_64", 
        "libc.so.6(GLIBC_2.14)(64bit)": "glibc-2.17-260.el7.x86_64", 
        "libc.so.6(GLIBC_2.4)(64bit)": "glibc-2.17-260.el7.x86_64", 
        "libacl.so.1(ACL_1.0)(64bit)": "libacl-2.2.51-14.el7.x86_64", 
        "libc.so.6(GLIBC_2.17)(64bit)": "glibc-2.17-260.el7.x86_64", 
        "/bin/sh": "bash-4.2.46-31.el7.x86_64", 
        "libc.so.6(GLIBC_2.2.5)(64bit)": "glibc-2.17-260.el7.x86_64", 
        "rtld(GNU_HASH)": "glibc-2.17-260.el7.x86_64", 
        "libc.so.6(GLIBC_2.3.4)(64bit)": "glibc-2.17-260.el7.x86_64", 
        "libc.so.6(GLIBC_2.8)(64bit)": "glibc-2.17-260.el7.x86_64", 
        "libselinux.so.1()(64bit)": "libselinux-2.5-15.el7.x86_64", 
        "libacl.so.1()(64bit)": "libacl-2.2.51-14.el7.x86_64", 
        "libc.so.6()(64bit)": "glibc-2.17-260.el7.x86_64", 
        "/sbin/install-info": "info-5.1-5.el7.x86_64", 
        "libc.so.6(GLIBC_2.7)(64bit)": "glibc-2.17-260.el7.x86_64"
      }, 
      "python_map": {}
    }
  ```

  

+ `upgrade_check_collect`的数据流相关文件

  > x2openEuler-client.py
  > software_collect.py
  > upgrade_check_collect.py
  > software_collect_data.py

+ rpm相关命令

  ```bash
  rpm -qa -> rpm_list
  rpm_name -> src_pkg_name
  SoftwareCollectData(rpm_name) -> software_collect_result
  rpm -qi -> pkg_info
  rpm -ql -> files
  rpm -q --provides -> rpm_provides
  rpm -qR tar -> collect_requires -> rpm_requires
  rpm -q --conflicts -> rpm_conflicts
  // 图
  require_pkg 
  provide_pkg
  ```

## Ubuntu2204

### dpkg

#### dpkg vs apt

> dpkg命令来自于英文词组“Debian package”的缩写，其功能是用于管理软件安装包，在Debian系统中最常用的软件安装、管理、卸载的实用工具，安装软件时，可以使用`-i`选项并指定deb安装包的路径



> apt-get命令并不直接操作deb安装包文件，而是从 `/etc/apt/sources.list`配置文件中定义的软件镜像源里下载软件包并安装，使用时也只需要制定软件的名称（或者也可以附上版本号）



> 虽然我们在使用dpkg时，已经解决掉了 软件安装过程中的大量问题，但是当依赖关系不满足时，仍然需要手动解决，而apt这个工具解决了这样的问题，linux distribution 先将软件放置到对应的服务器中，然后分析软件的依赖关系，并且记录下来，然后当客户端有安装软件需求时，通过清单列表与本地的dpkg以存在的软件数据相比较，就能从网络端获取所有需要的具有依赖属性的软件了



#### FILES

```bash
FILES
       /etc/dpkg/dpkg.cfg.d/[0-9a-zA-Z_-]*
           Configuration fragment files (since dpkg 1.15.4).

       /etc/dpkg/dpkg.cfg
           Configuration file with default options.

       /var/log/dpkg.log
           Default log file (see /etc/dpkg/dpkg.cfg and
           option --log).

       The other files listed below are in their default
       directories, see option --admindir to see how to
       change locations of these files.

       /var/lib/dpkg/available
           List of available packages.

       /var/lib/dpkg/status
           Statuses of available packages. This file
           contains information about whether a package is
           marked for removing or not, whether it is
           installed or not, etc. See section INFORMATION
           ABOUT PACKAGES for more info.

           The status file is backed up daily in
           /var/backups. It can be useful if it's lost or
           corrupted due to filesystems troubles.

       The format and contents of a binary package are
       described in deb(5).

```









#### /var/lib/dpkg/status

+ /var/lib 该目录保存系统或者某个应用程序运行过程中的状态信息。用户不允许更改该目录下的文件。
+ dpkg -l 的来源  **(?)**

```json
Package: zip
Status: install ok installed
Priority: optional
Section: utils
Installed-Size: 531
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: amd64
Multi-Arch: foreign
Version: 3.0-12build2
Depends: libbz2-1.0, libc6 (>= 2.34)
Recommends: unzip
Description: Archiver for .zip ficd les
This is InfoZIP's zip program. It produces files that are fully
compatible with the popular PKZIP program; however, the command line
options are not identical. In other words, the end result is the same,
but the methods differ. :-)
.
This version supports encryption.
Homepage: http://www.info-zip.org/Zip.html
Original-Maintainer: Santiago Vila <sanvila@debian.org>
```

#### dpkg  -l

> -l|--list [<pattern>...]         List packages concisely.

```json
wangzheng@wangzheng-Virtual-Machine:~$ dpkg -l
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                                       Version                                 Architecture Description
+++-==========================================-=======================================-============-================================================================================
ii  accountsservice                            22.07.5-2ubuntu1.3                      amd64        query and manipulate user account information
ii  acl                                        2.3.1-1                                 amd64        access control list - utilities
ii  acpi-support                               0.144                                   amd64        scripts for handling many ACPI events
ii  acpid                                      1:2.0.33-1ubuntu1                       amd64        Advanced Configuration and Power Interface event daemon
ii  adduser                                    3.118ubuntu5                            all          add and remove users and groups
ii  adwaita-icon-theme                         41.0-1ubuntu1                           all          default icon theme of GNOME (small subset)
ii  aisleriot                                  1:3.22.22-1                             amd64        GNOME solitaire card game collection
ii  alien                                      8.95.5                                  all          convert and install rpm and other packages
ii  alsa-base                                  1.0.25+dfsg-0ubuntu7                    all          ALSA driver configuration files
ii  alsa-topology-conf                         1.2.5.1-2                               all          ALSA topology configuration files
ii  alsa-ucm-conf                              1.2.6.3-1ubuntu1                        all          ALSA Use Case Manager configuration files
ii  alsa-utils                                 1.2.6-1ubuntu1                          amd64        Utilities for configuring and using ALSA
ii  amd64-microcode                            3.20191218.1ubuntu2                     amd64        Processor microcode firmware for AMD CPUs

```



#### dpkg  -s

> -s|--status [<package>...]       Display package status details.

```json
wangzheng@wangzheng-Virtual-Machine:~$ dpkg -s tar
Package: tar
Essential: yes
Status: install ok installed
Priority: required
Section: utils
Installed-Size: 956
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: amd64
Multi-Arch: foreign
Version: 1.34+dfsg-1build3
Replaces: cpio (<< 2.4.2-39)
Pre-Depends: libacl1 (>= 2.2.23), libc6 (>= 2.34), libselinux1 (>= 3.1~)
Suggests: bzip2, ncompress, xz-utils, tar-scripts, tar-doc
Breaks: dpkg-dev (<< 1.14.26)
Conflicts: cpio (<= 2.4.2-38)
Description: GNU version of the tar archiving utility
 Tar is a program for packaging a set of files as a single archive in tar
 format.  The function it performs is conceptually similar to cpio, and to
 things like PKZIP in the DOS world.  It is heavily used by the Debian package
 management system, and is useful for performing system backups and exchanging
 sets of files with others.
Homepage: https://www.gnu.org/software/tar/
Original-Maintainer: Janos Lenart <ocsi@debian.org>
```





+ dependency

  - Package A ***depends*** on Package B if B absolutely must be installed in order to run A. In some cases, A depends not only on B, but on a version of B. In this case, the version dependency is usually a lower limit, in the sense that A depends on any version of B more recent than some specified version.

  - Package A ***recommends*** Package B, if the package maintainer judges that most users would not want A without also having the functionality provided by B.

  - Package A **suggests** Package B if B contains files that are related to (and usually enhance) the functionality of A.

  - Package A ***conflicts*** with Package B when A will not operate if B is installed on the system. Most often, conflicts are cases where A contains files which are an improvement over those in B. "Conflicts" are often combined with "replaces".

  - Package A ***replaces*** Package B when files installed by B are removed and (in some cases) over-written by files in A.

  - Package A ***breaks*** Package B when both packages cannot be simultaneously configured in a system. The package management system will refuse to install one if the other one is already installed and configured in the system.

  - Package A ***provides*** Package B when all of the files and functionality of B are incorporated into A. This mechanism provides a way for users with constrained disk space to get only that part of package A which they really need.

  + "**Pre-Depends**" is a special dependency. In the case of most packages, `dpkg` will unpack the archive file of a package (i.e., its `.deb` file) independently of whether or not the files on which it depends exist on the system.

+ *priority*

  + **Required**: packages that are necessary for the proper functioning of the system.

    This includes all tools that are necessary to repair system defects. You must not remove these packages or your system may become totally broken and you may probably not even be able to use dpkg to put things back. Systems with only the Required packages are probably unusable, but they do have enough functionality to allow the sysadmin to boot and install more software.

  + **Important** packages should be found on any Unix-like system.

    Other packages which the system will not run well or be usable without will be here. This does *NOT* include Emacs or X or TeX or any other large application. These packages only constitute the bare infrastructure.

  + **Standard** packages are standard on any Linux system, including a reasonably small but not too limited character-mode system. Tools are included to be able to send e-mail (with mutt) and download files from archive servers.

    This is what will be installed by default if users do not select anything else. It does not include many large applications, but it does include the Python interpreter and some server software like OpenSSH (for remote administration) and Exim (for mail delivery, although it can be configured for local delivery only). It also includes some common generic documentation that most users will find helpful.

  + **Optional** packages include all those that you might reasonably want to install if you do not know what they are, or that do not have specialized requirements.

    This includes X, a full TeX distribution, and lots of applications.

  + **Extra**: packages that either conflict with others with higher priorities, are only likely to be useful if you already know what they are, or have specialized requirements that make them unsuitable for "Optional".



+ 参考资料
  + [Chapter 7. Basics of the Debian package management system](https://www.debian.org/doc/manuals/debian-faq/pkg-basics.en.html#controlfile)





#### dpkg -p

>  -p|--print-avail [<package>...]  Display available version details.

```json
wangzheng@wangzheng-Virtual-Machine:~$ dpkg -p tar
Package: tar
Essential: yes
Priority: required
Section: utils
Installed-Size: 956
Origin: Ubuntu
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Architecture: amd64
Multi-Arch: foreign
Version: 1.34+dfsg-1build3
Replaces: cpio (<< 2.4.2-39)
Pre-Depends: libacl1 (>= 2.2.23), libc6 (>= 2.34), libselinux1 (>= 3.1~)
Suggests: bzip2, ncompress, xz-utils, tar-scripts, tar-doc
Breaks: dpkg-dev (<< 1.14.26)
Conflicts: cpio (<= 2.4.2-38)
Filename: pool/main/t/tar/tar_1.34+dfsg-1build3_amd64.deb
Size: 294890
MD5sum: 17404f7ff3a169067e480e6674e7b1d9
Description: GNU version of the tar archiving utility
Original-Maintainer: Janos Lenart <ocsi@debian.org>
SHA1: 2fedbfb9513b203219269459646dd6b18973b535
SHA256: d6e4ef9e5793a271764209047ebb78970404b035fd1490cb513302744cfe9a25
SHA512: 699477fad44eac1d64c1b783fc9ded2294ba038f86208a5680eff729534d0cd878339820847781d54b250efa151678ed33a277a7d40cd0dd512d4714d4806e01
Homepage: https://www.gnu.org/software/tar/
Task: minimal, server-minimal
Description-md5: 48033bf96442788d1f697785773ad9bb
```

#### dpkg -L

> -L|--listfiles <package>...      List files 'owned' by package(s).

```json
wangzheng@wangzheng-Virtual-Machine:~$ dpkg -L tar
/.
/bin
/bin/tar
/etc
/usr
/usr/lib
/usr/lib/mime
/usr/lib/mime/packages
/usr/lib/mime/packages/tar
/usr/sbin
/usr/sbin/rmt-tar
/usr/sbin/tarcat
/usr/share
/usr/share/doc
/usr/share/doc/tar
/usr/share/doc/tar/AUTHORS
/usr/share/doc/tar/NEWS.gz
/usr/share/doc/tar/README.Debian
/usr/share/doc/tar/THANKS.gz
/usr/share/doc/tar/changelog.Debian.gz
/usr/share/doc/tar/copyright
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/tar.1.gz
/usr/share/man/man1/tarcat.1.gz
/usr/share/man/man8
/usr/share/man/man8/rmt-tar.8.gz
/etc/rmt
```



#### 参考文章

+ [What is the difference between dependencies and pre-depends?](https://askubuntu.com/questions/83553/what-is-the-difference-between-dependencies-and-pre-depends)
+ [dpkg(1) — Linux manual page](https://man7.org/linux/man-pages/man1/dpkg.1.html)
+ [5.4. Manipulating Packages with `dpkg`](https://debian-handbook.info/browse/da-DK/stable/sect.manipulating-packages-with-dpkg.html)
+ [[Linux软件安装管理之——dpkg与apt-*详解](https://segmentfault.com/a/1190000011463440)]
+ [Kapitel 5. Packaging System: Tools and Fundamental Principles](https://debian-handbook.info/browse/da-DK/stable/packaging-system.html)
+ [apt-get apt-cache命令使用](https://blog.csdn.net/hunanchenxingyu/article/details/42030227)
+ [Linux apt-cache 命令](https://www.computerhope.com/unix/apt-cache.htm)
+ [dpkg-query命令 – 在dpkg数据库中查询软件包](https://www.linuxcool.com/dpkg-query)
+ [Chapter 7. Basics of the Debian package management system](https://www.debian.org/doc/manuals/debian-faq/pkg-basics.en.html#controlfile)

### alien

> alien is a program that converts between Red Hat rpm, Debian deb, Stampede slp, Slackware tgz, and Solaris pkg file formats.



+ `ubuntu`下`tar_1.34+dfsg-1build3_amd64.deb`

  ```bash
  wangzheng@wangzheng-Virtual-Machine:~/test$ dpkg -c tar_1.34+dfsg-1build3_amd64.deb 
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./bin/
  -rwxr-xr-x root/root    517952 2022-03-25 17:52 ./bin/tar
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./etc/
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/lib/
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/lib/mime/
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/lib/mime/packages/
  -rw-r--r-- root/root       321 2021-02-17 17:53 ./usr/lib/mime/packages/tar
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/sbin/
  -rwxr-xr-x root/root     59976 2022-03-25 17:52 ./usr/sbin/rmt-tar
  -rwxr-xr-x root/root       936 2022-03-25 17:52 ./usr/sbin/tarcat
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/share/
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/share/doc/
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/share/doc/tar/
  -rw-r--r-- root/root       601 2021-02-17 17:53 ./usr/share/doc/tar/AUTHORS
  -rw-r--r-- root/root     22939 2021-02-17 17:53 ./usr/share/doc/tar/NEWS.gz
  -rw-r--r-- root/root       849 2021-02-17 17:53 ./usr/share/doc/tar/README.Debian
  -rw-r--r-- root/root     10637 2021-02-17 17:53 ./usr/share/doc/tar/THANKS.gz
  -rw-r--r-- root/root       999 2022-03-25 17:52 ./usr/share/doc/tar/changelog.Debian.gz
  -rw-r--r-- root/root      1488 2021-02-17 17:53 ./usr/share/doc/tar/copyright
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/share/man/
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/share/man/man1/
  -rw-r--r-- root/root     13535 2022-03-25 17:52 ./usr/share/man/man1/tar.1.gz
  -rw-r--r-- root/root       366 2022-03-25 17:52 ./usr/share/man/man1/tarcat.1.gz
  drwxr-xr-x root/root         0 2022-03-25 17:52 ./usr/share/man/man8/
  -rw-r--r-- root/root      2393 2022-03-25 17:52 ./usr/share/man/man8/rmt-tar.8.gz
  lrwxrwxrwx root/root         0 2022-03-25 17:52 ./etc/rmt -> /usr/sbin/rmt
  
  ```

+ `alien` 转换

  ```bash
  wangzheng@wangzheng-Virtual-Machine:~/test$ alien tar_1.34+dfsg-1build3_amd64.deb 
  wangzheng@wangzheng-Virtual-Machine:~/test$ ls
  tar_1.34+dfsg-1build3_amd64.deb  tar-1.34+dfsg-2.x86_64.rpm
  ```

+ `centos`下`tar-1.34+dfsg-2.x86_64.rpm`

  ```bash
  [wangzheng@localhost test]$ rpm -qpl tar-1.34+dfsg-2.x86_64.rpm
  /bin/tar
  /etc/rmt
  /usr/lib/.build-id
  /usr/lib/.build-id/87
  /usr/lib/.build-id/87/ef81e5a7788f0c740b9048d37629d85da42904
  /usr/lib/.build-id/b4
  /usr/lib/.build-id/b4/6be844e48880d6bd83601e7d9e7abd5260be25
  /usr/lib/mime
  /usr/lib/mime/packages
  /usr/lib/mime/packages/tar
  /usr/sbin/rmt-tar
  /usr/sbin/tarcat
  /usr/share/doc/tar
  /usr/share/doc/tar/AUTHORS
  /usr/share/doc/tar/NEWS.gz
  /usr/share/doc/tar/README.Debian
  /usr/share/doc/tar/THANKS.gz
  /usr/share/doc/tar/changelog.Debian.gz
  /usr/share/doc/tar/copyright
  /usr/share/man/man1/tar.1.gz
  /usr/share/man/man1/tarcat.1.gz
  /usr/share/man/man8/rmt-tar.8.gz
  ```

  
