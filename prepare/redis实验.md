# redis实验

## 实验环境

```bash
wangzheng@wangzheng-Virtual-Machine:~$ cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.6 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.6 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

## UBUNTU

### 安装redis

```bash
wangzheng@wangzheng-Virtual-Machine:~$ sudo apt install redis
[sudo] password for wangzheng: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libjemalloc1 redis-server redis-tools
Suggested packages:
  ruby-redis
The following NEW packages will be installed:
  libjemalloc1 redis redis-server redis-tools
0 upgraded, 4 newly installed, 0 to remove and 26 not upgraded.
Need to get 637 kB of archives.
After this operation, 3,083 kB of additional disk space will be used.
Do you want to continue? [Y/n]

Get:1 http://mirrors.tools.huawei.com/ubuntu bionic/universe amd64 libjemalloc1 amd64 3.6.0-11 [82.4 kB]
Get:2 http://mirrors.tools.huawei.com/ubuntu bionic-updates/universe amd64 redis-tools amd64 5:4.0.9-1ubuntu0.2 [516 kB]
Get:3 http://mirrors.tools.huawei.com/ubuntu bionic-updates/universe amd64 redis-server amd64 5:4.0.9-1ubuntu0.2 [35.4 kB]
Get:4 http://mirrors.tools.huawei.com/ubuntu bionic-updates/universe amd64 redis all 5:4.0.9-1ubuntu0.2 [3,084 B]
Fetched 637 kB in 0s (4,656 kB/s)
Selecting previously unselected package libjemalloc1.
(Reading database ... 211544 files and directories currently installed.)
Preparing to unpack .../libjemalloc1_3.6.0-11_amd64.deb ...
Unpacking libjemalloc1 (3.6.0-11) ...
Selecting previously unselected package redis-tools.
Preparing to unpack .../redis-tools_5%3a4.0.9-1ubuntu0.2_amd64.deb ...
Unpacking redis-tools (5:4.0.9-1ubuntu0.2) ...
Selecting previously unselected package redis-server.
Preparing to unpack .../redis-server_5%3a4.0.9-1ubuntu0.2_amd64.deb ...
Unpacking redis-server (5:4.0.9-1ubuntu0.2) ...
Selecting previously unselected package redis.
Preparing to unpack .../redis_5%3a4.0.9-1ubuntu0.2_all.deb ...
Unpacking redis (5:4.0.9-1ubuntu0.2) ...
Setting up libjemalloc1 (3.6.0-11) ...
Setting up redis-tools (5:4.0.9-1ubuntu0.2) ...
Setting up redis-server (5:4.0.9-1ubuntu0.2) ...
Created symlink /etc/systemd/system/redis.service → /lib/systemd/system/redis-server.service.
Created symlink /etc/systemd/system/multi-user.target.wants/redis-server.service → /lib/systemd/system/redis-server.service.
Setting up redis (5:4.0.9-1ubuntu0.2) ...
Processing triggers for libc-bin (2.27-3ubuntu1.5) ...
Processing triggers for systemd (237-3ubuntu10.56) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for ureadahead (0.100.0-21) ...
```

### redis 版本

```bash
wangzheng@wangzheng-Virtual-Machine:~$ redis-server -v
Redis server v=4.0.9 sha=00000000:0 malloc=jemalloc-3.6.0 bits=64 build=9435c3c2879311f3
wangzheng@wangzheng-Virtual-Machine:~$ redis-cli -v
redis-cli 4.0.9
```

### redis 包传递到openeuler

```bash
wangzheng@wangzheng-Virtual-Machine:/var/cache/apt/archives$ scp redis* root@172.23.164.120:~/redis_pkg_deb

Authorized users only. All activities may be monitored and reported.
root@172.23.164.120's password: 
/root/.bashrc: line 21: pyenv: command not found
redis_5%3a4.0.9-1ubuntu0.2_all.deb                                                                                                                             100% 3084     4.5MB/s   00:00    
redis-server_5%3a4.0.9-1ubuntu0.2_amd64.deb                                                                                                                    100%   35KB  31.5MB/s   00:00    
redis-tools_5%3a4.0.9-1ubuntu0.2_amd64.deb                                                                                                                     100%  504KB 107.6MB/s   00:00  
```

### redis 依赖展示

```bash
wangzheng@wangzheng-Virtual-Machine:~$ apt-rdepends redis
Reading package lists... Done
Building dependency tree       
Reading state information... Done
redis
  Depends: redis-server (>= 5:4.0.9-1ubuntu0.2)
redis-server
  Depends: lsb-base (>= 3.2-14)
  Depends: redis-tools (= 5:4.0.9-1ubuntu0.2)
lsb-base
redis-tools
  Depends: adduser
  Depends: libc6 (>= 2.14)
  Depends: libjemalloc1 (>= 2.1.1)
adduser
  Depends: debconf (>= 0.5)
  Depends: debconf-2.0
  Depends: passwd
debconf
  PreDepends: perl-base (>= 5.20.1-3~)
perl-base
  PreDepends: dpkg (>= 1.17.17)
  PreDepends: libc6 (>= 2.23)
dpkg
  Depends: tar (>= 1.28-1)
  PreDepends: libbz2-1.0
  PreDepends: libc6 (>= 2.14)
  PreDepends: liblzma5 (>= 5.2.2)
  PreDepends: libselinux1 (>= 2.3)
  PreDepends: libzstd1 (>= 1.3.2)
  PreDepends: zlib1g (>= 1:1.1.4)
tar
  PreDepends: libacl1 (>= 2.2.51-8)
  PreDepends: libc6 (>= 2.17)
  PreDepends: libselinux1 (>= 1.32)
libacl1
  Depends: libattr1 (>= 1:2.4.46-8)
  Depends: libc6 (>= 2.14)
libattr1
  Depends: libc6 (>= 2.4)
libc6
  Depends: libgcc1
libgcc1
  Depends: gcc-8-base (= 8.4.0-1ubuntu1~18.04)
  Depends: libc6 (>= 2.14)
gcc-8-base
libselinux1
  Depends: libc6 (>= 2.14)
  Depends: libpcre3
libpcre3
  Depends: libc6 (>= 2.14)
libbz2-1.0
  Depends: libc6 (>= 2.4)
liblzma5
  Depends: libc6 (>= 2.17)
libzstd1
  Depends: libc6 (>= 2.14)
zlib1g
  Depends: libc6 (>= 2.14)
debconf-2.0
passwd
  Depends: libaudit1 (>= 1:2.2.1)
  Depends: libc6 (>= 2.14)
  Depends: libpam-modules
  Depends: libpam0g (>= 0.99.7.1)
  Depends: libselinux1 (>= 1.32)
  Depends: libsemanage1 (>= 2.0.3)
libaudit1
  Depends: libaudit-common (>= 1:2.8.2-1ubuntu1.1)
  Depends: libc6 (>= 2.14)
  Depends: libcap-ng0
libaudit-common
libcap-ng0
  Depends: libc6 (>= 2.8)
libpam-modules
  PreDepends: debconf (>= 0.5)
  PreDepends: debconf-2.0
  PreDepends: libaudit1 (>= 1:2.2.1)
  PreDepends: libc6 (>= 2.27)
  PreDepends: libdb5.3
  PreDepends: libpam-modules-bin (= 1.1.8-3.6ubuntu2.18.04.3)
  PreDepends: libpam0g (>= 1.1.3-2)
  PreDepends: libselinux1 (>= 2.1.9)
libdb5.3
  Depends: libc6 (>= 2.17)
libpam-modules-bin
  Depends: libaudit1 (>= 1:2.2.1)
  Depends: libc6 (>= 2.14)
  Depends: libpam0g (>= 0.99.7.1)
  Depends: libselinux1 (>= 1.32)
libpam0g
  Depends: debconf (>= 0.5)
  Depends: debconf-2.0
  Depends: libaudit1 (>= 1:2.2.1)
  Depends: libc6 (>= 2.14)
libsemanage1
  Depends: libaudit1 (>= 1:2.2.1)
  Depends: libbz2-1.0
  Depends: libc6 (>= 2.14)
  Depends: libselinux1 (>= 2.7)
  Depends: libsemanage-common (= 2.7-2build2)
  Depends: libsepol1 (>= 2.7)
libsemanage-common
libsepol1
  Depends: libc6 (>= 2.14)
libjemalloc1
  Depends: libc6 (>= 2.14)
```

![redis](C:\Users\w30041197\Desktop\dot\redis.png)



### 文件替换

| libjemalloc1 | [jemalloc-5.1.0-4.oe1.x86_64.rpm](https://repo.openeuler.org/openEuler-20.03-LTS-SP1/everything/x86_64/Packages/jemalloc-5.1.0-4.oe1.x86_64.rpm)   这个不对！ |
| :----------: | :----------------------------------------------------------: |
|              |                                                              |
|              |                                                              |
|              |                                                              |



## OPNEEULER

### alien 转换包

```bash
[root@localhost redis_pkg_deb]# alien --to-rpm --scripts *
redis-4.0.9-2.noarch.rpm generated
redis-server-4.0.9-2.x86_64.rpm generated
redis-tools-4.0.9-2.x86_64.rpm generated
[root@localhost redis_pkg_deb]# ll
total 1.2M
-rw-r--r--. 1 root root 9.3K Dec  8 16:07 redis-4.0.9-2.noarch.rpm
-rw-r--r--. 1 root root 3.1K Dec  8 15:34 redis_5%3a4.0.9-1ubuntu0.2_all.deb
-rw-r--r--. 1 root root  49K Dec  8 16:07 redis-server-4.0.9-2.x86_64.rpm
-rw-r--r--. 1 root root  35K Dec  8 15:34 redis-server_5%3a4.0.9-1ubuntu0.2_amd64.deb
-rw-r--r--. 1 root root 550K Dec  8 16:07 redis-tools-4.0.9-2.x86_64.rpm
-rw-r--r--. 1 root root 505K Dec  8 15:34 redis-tools_5%3a4.0.9-1ubuntu0.2_amd64.deb
```

### 安装

+ jemalloc

  ```bash
  # download from https://repo.openeuler.org/openEuler-20.03-LTS-SP1/everything/x86_64/Packages/
  [root@localhost redis_pkg_deb]# ls | grep jemalloc-
  jemalloc-5.1.0-4.oe1.x86_64.rpm
  jemalloc-devel-5.1.0-4.oe1.x86_64.rpm
  jemalloc-help-5.1.0-4.oe1.x86_64.rpm
  
  [root@localhost redis_pkg_deb]# rpm -ivh jemall*
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:jemalloc-help-5.1.0-4.oe1        ################################# [ 33%]
     2:jemalloc-5.1.0-4.oe1             ################################# [ 67%]
     3:jemalloc-devel-5.1.0-4.oe1       ################################# [100%]
  ```

  ```bash
  
  # jemalloc 5.1版本太高(openeuler repo 没有提供低版本），没有提供*.so.1, 选择转换ubuntu的包
  [root@localhost redis_pkg_deb]# rpm -ivh redis-tools-4.0.9-2.x86_64.rpm 
  error: Failed dependencies:
  	libjemalloc.so.1()(64bit) is needed by redis-tools-4.0.9-2.x86_64
  ```

  ```bahs
  apt-cache show libjemalloc1
  Filename: pool/universe/j/jemalloc/libjemalloc1_3.6.0-11_amd64.deb
  ```

  ```bash
  [root@localhost redis_pkg_deb]# rpm -ivh libjemalloc1-3.6.0-12.x86_64.rpm 
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  	file / from install of libjemalloc1-3.6.0-12.x86_64 conflicts with file from package filesystem-3.14-1.oe1.x86_64
  	file /usr/lib from install of libjemalloc1-3.6.0-12.x86_64 conflicts with file from package filesystem-3.14-1.oe1.x86_64
  [root@localhost redis_pkg_deb]# rpmrebuild -pe libjemalloc1-3.6.0-12.x86_64.rpm 
  (GenRpmQf) remove tag line ENHANCESFLAGS
  (GenRpmQf) remove tag line ENHANCESNAME
  (GenRpmQf) remove tag line ENHANCESVERSION
  (GenRpmQf) remove tag line SUGGESTSFLAGS
  (GenRpmQf) remove tag line SUGGESTSNAME
  (GenRpmQf) remove tag line SUGGESTSVERSION
  Do you want to continue ? (y/N) y
  result: /root/rpmbuild/RPMS/x86_64/libjemalloc1-3.6.0-12.x86_64.rpm
  [root@localhost redis_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/x86_64/libjemalloc1-3.6.0-12.x86_64.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:libjemalloc1-3.6.0-12            ################################# [100%]
  
  ```

+ redis-tools

  ```bash
  [root@localhost redis_pkg_deb]# rpmrebuild -pe redis-tools-4.0.9-2.x86_64.rpm 
  (GenRpmQf) remove tag line ENHANCESFLAGS
  (GenRpmQf) remove tag line ENHANCESNAME
  (GenRpmQf) remove tag line ENHANCESVERSION
  (GenRpmQf) remove tag line SUGGESTSFLAGS
  (GenRpmQf) remove tag line SUGGESTSNAME
  (GenRpmQf) remove tag line SUGGESTSVERSION
  Do you want to continue ? (y/N) y
  warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.130208/work/root/usr/share/doc/redis-tools/00-RELEASENOTES.gz
  result: /root/rpmbuild/RPMS/x86_64/redis-tools-4.0.9-2.x86_64.rpm
  ```

  ```bash
  [root@localhost redis_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/x86_64/redis-tools-4.0.9-2.x86_64.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:redis-tools-4.0.9-2              ################################# [100%]
  ```

+ redis-server

  ```bash
  [root@localhost redis_pkg_deb]# rpmrebuild -pe redis-server-4.0.9-2.x86_64.rpm 
  (GenRpmQf) remove tag line ENHANCESFLAGS
  (GenRpmQf) remove tag line ENHANCESNAME
  (GenRpmQf) remove tag line ENHANCESVERSION
  (GenRpmQf) remove tag line SUGGESTSFLAGS
  (GenRpmQf) remove tag line SUGGESTSNAME
  (GenRpmQf) remove tag line SUGGESTSVERSION
  Do you want to continue ? (y/N) y
  warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.130526/work/root/usr/bin/redis-server
  warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.130526/work/root/usr/share/doc/redis-server/00-RELEASENOTES.gz
  warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.130526/work/root/usr/share/doc/redis-server/NEWS.Debian.gz
  warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.130526/work/root/usr/share/doc/redis-server/changelog.Debian.gz
  
  
  [root@localhost redis_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/x86_64/redis-server-4.0.9-2.x86_64.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  /var/tmp/rpm-tmp.Nidk7p: line 4: dpkg-maintscript-helper: command not found
  error: %prein(redis-server-4.0.9-2.x86_64) scriptlet failed, exit status 127
  error: redis-server-4.0.9-2.x86_64: install failed
  
  # 原因
  %pre -p /bin/sh
  #!/bin/sh
  set -e
  # Automatically added by dh_installdeb/11.1.6ubuntu1
  dpkg-maintscript-helper rm_conffile /etc/redis/redis-server.pre-up.d/00_example 4:4.0.2-3\~ -- "$@"
  dpkg-maintscript-helper rm_conffile /etc/redis/redis-server.pre-down.d/00_example 4:4.0.2-3\~ -- "$@"
  dpkg-maintscript-helper rm_conffile /etc/redis/redis-server.post-up.d/00_example 4:4.0.2-3\~ -- "$@"
  dpkg-maintscript-helper rm_conffile /etc/redis/redis-server.post-down.d/00_example 4:4.0.2-3\~ -- "$@"
  # End automatically added section
  
  
  # 解决： 不生成脚本
  result: /root/rpmbuild/RPMS/x86_64/redis-server-4.0.9-2.x86_64.rpm
  [root@localhost redis_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/x86_64/redis-server-4.0.9-2.x86_64.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:redis-server-4.0.9-2             ################################# [100%]
  ```

  

+ redis

  ```bash
  [root@localhost redis_pkg_deb]# rpmrebuild -pe redis-4.0.9-2.noarch.rpm 
  (GenRpmQf) remove tag line ENHANCESFLAGS
  (GenRpmQf) remove tag line ENHANCESNAME
  (GenRpmQf) remove tag line ENHANCESVERSION
  (GenRpmQf) remove tag line SUGGESTSFLAGS
  (GenRpmQf) remove tag line SUGGESTSNAME
  (GenRpmQf) remove tag line SUGGESTSVERSION
  Do you want to continue ? (y/N) y
  warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.131977/work/root/usr/share/doc/redis/00-RELEASENOTES.gz
  warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.131977/work/root/usr/share/doc/redis/NEWS.Debian.gz
  warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.131977/work/root/usr/share/doc/redis/changelog.Debian.gz
  result: /root/rpmbuild/RPMS/noarch/redis-4.0.9-2.noarch.rpm
  
  [root@localhost redis_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/noarch/redis-4.0.9-2.noarch.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:redis-4.0.9-2                    ################################# [100%]
  ```

  

### 测试redis

+ 问题1(解决)

  ```bash
  [root@localhost redis_pkg_deb]# redis-cli
  redis-cli: error while loading shared libraries: libjemalloc.so.1: cannot open shared object file: No such file or directory
  
  [root@localhost redis_pkg_deb]# ln -s /usr/lib/x86_64-linux-gnu/libjemalloc.so.1 /usr/lib64/libjemalloc.so.1
  ```

+ 问题2(解决)

  ```bash
  [root@localhost redis_pkg_deb]# redis-cli
  Could not connect to Redis at 127.0.0.1:6379: Connection refused
  Could not connect to Redis at 127.0.0.1:6379: Connection refused
  not connected> 
  
  redis-server 没启动，估计是没有生成脚本导致的
  ```



### 结果

```bash
[root@localhost redis_pkg_deb]# redis-cli
127.0.0.1:6379> set a 10
OK
127.0.0.1:6379> get a 
"10"
```

