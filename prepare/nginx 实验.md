# nginx 实验

## 实验环境

```bash
# ubuntu
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

# openeuler
[root@localhost ~]# cat /etc/os-release 
NAME="openEuler"
VERSION="20.03 (LTS-SP1)"
ID="openEuler"
VERSION_ID="20.03"
PRETTY_NAME="openEuler 20.03 (LTS-SP1)"
ANSI_COLOR="0;31"

# nginx version
wangzheng@wangzheng-Virtual-Machine:~$ nginx -V
nginx version: nginx/1.14.0 (Ubuntu)
built with OpenSSL 1.1.1  11 Sep 2018
```



## nginx安装

```bash
# ubuntu
wangzheng@wangzheng-Virtual-Machine:~$ sudo apt-get install nginx
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libnginx-mod-http-geoip 
  libnginx-mod-http-image-filter 
  libnginx-mod-http-xslt-filter 
  libnginx-mod-mail 
  libnginx-mod-stream 
  nginx-common 
  nginx-core
Suggested packages:
  fcgiwrap nginx-doc
The following NEW packages will be installed:
  libnginx-mod-http-geoip libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter libnginx-mod-mail libnginx-mod-stream nginx nginx-common nginx-core
0 upgraded, 8 newly installed, 0 to remove and 32 not upgraded.
Need to get 597 kB of archives.
After this operation, 2,120 kB of additional disk space will be used.
Do you want to continue? [Y/n] 



# openeuler（未实际安装，仅展示依赖）
[root@localhost ~]# yum install nginx
OS                                                                                                                                                               8.2 kB/s | 3.8 kB     00:00    
everything                                                                                                                                                        35 kB/s | 3.8 kB     00:00    
EPOL                                                                                                                                                              29 kB/s | 2.9 kB     00:00    
debuginfo                                                                                                                                                         42 kB/s | 3.8 kB     00:00    
source                                                                                                                                                            38 kB/s | 3.8 kB     00:00    
依赖关系解决。
=================================================================================================================================================================================================
 Package                                                    Architecture                          Version                                        Repository                                 Size
=================================================================================================================================================================================================
安装:
 nginx                                                      x86_64                                1:1.16.1-7.oe1                                 everything                                478 k
安装依赖关系:
 gperftools-libs                                            x86_64                                2.8-1.oe1                                      OS                                        266 k
 libunwind                                                  x86_64                                1.3.1-3.oe1                                    OS                                         54 k
 nginx-all-modules                                          noarch                                1:1.16.1-7.oe1                                 everything                                8.1 k
 nginx-filesystem                                           noarch                                1:1.16.1-7.oe1                                 everything                                9.1 k
 nginx-mod-http-image-filter                                x86_64                                1:1.16.1-7.oe1                                 everything                                 17 k
 nginx-mod-http-perl                                        x86_64                                1:1.16.1-7.oe1                                 everything                                 26 k
 nginx-mod-http-xslt-filter                                 x86_64                                1:1.16.1-7.oe1                                 everything                                 16 k
 nginx-mod-mail                                             x86_64                                1:1.16.1-7.oe1                                 everything                                 45 k
 nginx-mod-stream                                           x86_64                                1:1.16.1-7.oe1                                 everything                                 68 k
安装弱的依赖:
 nginx-help                                                 noarch                                1:1.16.1-7.oe1                                 everything                                 71 k

事务概要
=================================================================================================================================================================================================
安装  11 软件包

总下载：1.0 M
安装大小：3.5 M
确定吗？[y/N]： 

```

+ 简单对比安装时提示的依赖

|      |             ubuntu             |          openeuler          |
| :--: | :----------------------------: | :-------------------------: |
|  √   | libnginx-mod-http-image-filter | nginx-mod-http-image-filter |
|  √   | libnginx-mod-http-xslt-filter  | nginx-mod-http-xslt-filter  |
|  √   |       libnginx-mod-mail        |       nginx-mod-mail        |
|  √   |      libnginx-mod-stream       |      nginx-mod-stream       |
|      |                                |                             |
|      |          nginx-common          |                             |
|      |    libnginx-mod-http-geoip     |                             |
|      |           nginx-core           |                             |
|      |                                |     nginx-mod-http-perl     |
|      |                                |          libunwind          |
|      |                                |      nginx-all-modules      |
|      |                                |      nginx-filesystem       |
|      |                                |         nginx-help          |
|      |                                |       gperftools-libs       |



## 依赖替换

|   ubuntu   |                          openeuler                           |
| :--------: | :----------------------------------------------------------: |
|  iproute2  |                  iproute-5.5.0-4.oe1.x86_64                  |
|  libpcre3  | pcre-8.44-2.oe1.x86_64  这个不对！！选择通过转换libpcre3_8.39-9_amd64.deb |
| libssl1.1  |                 openssl-1.1.1f-1.oe1.x86_64                  |
| libgeoip1  |                  GeoIP-1.6.12-5.oe1.x86_64                   |
|   zlib1g   |                  zlib-1.2.11-17.oe1.x86_64                   |
| libxslt1.1 |                 libxslt-1.1.34-3.oe1.x86_64                  |
|  libxml2   |                 libxml2-2.9.10-11.oe1.x86_64                 |
|   libgd3   |                    gd-2.3.0-1.oe1.x86_64                     |
|            |                                                              |







## 依赖图

![nginx](C:\Users\w30041197\Desktop\dot\nginx.png)

## 实验过程

### 下载和转换

+ deb 包下载地址：https://mirrors.tools.huawei.com/ubuntu/pool/main/

+ 需要转换的包：9个

  ```bash
  [root@localhost nginx_pkg_deb]# ls | wc -l
  9
  [root@localhost nginx_pkg_deb]# ll
  total 616K
  -rw-r--r--. 1 root root  11K Dec  7 14:34 libnginx-mod-http-geoip_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root  15K Dec  7 14:35 libnginx-mod-http-image-filter_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root  13K Dec  7 14:35 libnginx-mod-http-xslt-filter_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root  41K Dec  7 14:36 libnginx-mod-mail_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root  62K Dec  7 14:36 libnginx-mod-stream_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root  13K Dec  7 14:39 lsb-base_9.20170808ubuntu1_all.deb
  -rw-r--r--. 1 root root 3.6K Dec  7 14:31 nginx_1.14.0-0ubuntu1.11_all.deb
  -rw-r--r--. 1 root root  37K Dec  7 14:32 nginx-common_1.14.0-0ubuntu1.11_all.deb
  -rw-r--r--. 1 root root 404K Dec  7 14:33 nginx-core_1.14.0-0ubuntu1.11_amd64.deb
  
  ```

+ 转换后

  ```bash
  [root@localhost nginx_pkg_deb]# alien --to-rpm --scripts *
  libnginx-mod-http-geoip-1.14.0-1.x86_64.rpm generated
  libnginx-mod-http-image-filter-1.14.0-1.x86_64.rpm generated
  libnginx-mod-http-xslt-filter-1.14.0-1.x86_64.rpm generated
  libnginx-mod-mail-1.14.0-1.x86_64.rpm generated
  libnginx-mod-stream-1.14.0-1.x86_64.rpm generated
  lsb-base-9.20170808ubuntu1-2.noarch.rpm generated
  nginx-1.14.0-1.noarch.rpm generated
  nginx-common-1.14.0-1.noarch.rpm generated
  nginx-core-1.14.0-1.x86_64.rpm generated
  [root@localhost nginx_pkg_deb]# ll
  total 1.4M
  -rw-r--r--. 1 root root  11K Dec  7 14:34 libnginx-mod-http-geoip_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root  20K Dec  7 14:41 libnginx-mod-http-geoip-1.14.0-1.x86_64.rpm
  -rw-r--r--. 1 root root  15K Dec  7 14:35 libnginx-mod-http-image-filter_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root  24K Dec  7 14:41 libnginx-mod-http-image-filter-1.14.0-1.x86_64.rpm
  -rw-r--r--. 1 root root  13K Dec  7 14:35 libnginx-mod-http-xslt-filter_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root  22K Dec  7 14:41 libnginx-mod-http-xslt-filter-1.14.0-1.x86_64.rpm
  -rw-r--r--. 1 root root  41K Dec  7 14:36 libnginx-mod-mail_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root  51K Dec  7 14:41 libnginx-mod-mail-1.14.0-1.x86_64.rpm
  -rw-r--r--. 1 root root  62K Dec  7 14:36 libnginx-mod-stream_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root  74K Dec  7 14:41 libnginx-mod-stream-1.14.0-1.x86_64.rpm
  -rw-r--r--. 1 root root  20K Dec  7 14:41 lsb-base-9.20170808ubuntu1-2.noarch.rpm
  -rw-r--r--. 1 root root  13K Dec  7 14:39 lsb-base_9.20170808ubuntu1_all.deb
  -rw-r--r--. 1 root root 3.6K Dec  7 14:31 nginx_1.14.0-0ubuntu1.11_all.deb
  -rw-r--r--. 1 root root 9.6K Dec  7 14:41 nginx-1.14.0-1.noarch.rpm
  -rw-r--r--. 1 root root  37K Dec  7 14:32 nginx-common_1.14.0-0ubuntu1.11_all.deb
  -rw-r--r--. 1 root root  53K Dec  7 14:41 nginx-common-1.14.0-1.noarch.rpm
  -rw-r--r--. 1 root root 404K Dec  7 14:33 nginx-core_1.14.0-0ubuntu1.11_amd64.deb
  -rw-r--r--. 1 root root 438K Dec  7 14:41 nginx-core-1.14.0-1.x86_64.rpm
  ```

### 安装

+ alien转换后的包均会有目录文件冲突的情况，默认`采取rpmrebuild  %files 下删除对应目录文件`的方法

  ```bash
  [root@localhost nginx_pkg_deb]# rpm -ivh lsb-base-9.20170808ubuntu1-2.noarch.rpm 
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  	package lsb-base-9.20170808ubuntu1-2.noarch is already installed
  	file / from install of lsb-base-9.20170808ubuntu1-2.noarch conflicts with file from package filesystem-3.14-1.oe1.x86_64
  	file /lib from install of lsb-base-9.20170808ubuntu1-2.noarch conflicts with file from package filesystem-3.14-1.oe1.x86_64
  ```

+ lsb-base-9.20170808ubuntu1-2.noarch.rpm(处理mysql时已经安装)

```bash
[root@localhost nginx_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/noarch/lsb-base-9.20170808ubuntu1-2.noarch.rpm
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
	package lsb-base-9.20170808ubuntu1-2.noarch is already installed
```

+ nginx-common-1.14.0-1.noarch.rpm

  ```bash
  [root@localhost nginx_pkg_deb]# rpmrebuild -pe nginx-common-1.14.0-1.noarch.rpm 
  (GenRpmQf) remove tag line ENHANCESFLAGS
  (GenRpmQf) remove tag line ENHANCESNAME
  (GenRpmQf) remove tag line ENHANCESVERSION
  (GenRpmQf) remove tag line SUGGESTSFLAGS
  (GenRpmQf) remove tag line SUGGESTSNAME
  (GenRpmQf) remove tag line SUGGESTSVERSION
  Do you want to continue ? (y/N) y
  warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.85679/work/root/usr/share/nginx/modules
  result: /root/rpmbuild/RPMS/noarch/nginx-common-1.14.0-1.noarch.rpm
  
  [root@localhost nginx_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/noarch/nginx-common-1.14.0-1.noarch.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  /var/tmp/rpm-tmp.oJKMWp: line 5: dpkg-maintscript-helper: command not found
  error: %prein(nginx-common-1.14.0-1.noarch) scriptlet failed, exit status 127
  error: nginx-common-1.14.0-1.noarch: install failed
  ```

  + 这里出现 **%prein（）scriptlet failed**的问题，贴一下spec, （目前为了看最终结果，选择不生成脚本）

    ```bash
    %pre -p /bin/sh
    #!/bin/sh
    set -e
    
    # Handle naxsi removal
    dpkg-maintscript-helper rm_conffile \
              /etc/nginx/naxsi.rules         1.6.2-2~ -- "$@"
    dpkg-maintscript-helper rm_conffile \
              /etc/nginx/naxsi_core.rules    1.6.2-2~ -- "$@"
    dpkg-maintscript-helper rm_conffile \
              /etc/nginx/naxsi-ui.conf.1.4.1 1.6.2-2~ -- "$@"
    dpkg-maintscript-helper rm_conffile \
              /etc/nginx/naxsi-ui.conf       1.6.2-2~ -- "$@"
    
    # Handle upstart removal
    dpkg-maintscript-helper rm_conffile \
              /etc/init/nginx.conf           1.13.5-1~ -- "$@"
    
    case "$1" in
      install)
        # If we are doing a fresh install, then these files are no longer needed.
        # They were around for a very short time and are best simply removed.
        rm -f /etc/logrotate.d/nginx-full
        rm -f /etc/logrotate.d/nginx-light
        rm -f /etc/logrotate.d/nginx-extras
        rm -f /etc/logrotate.d/nginx-common
        ;;
    
      upgrade)
        # If this is an upgrade, then they might have the UFW profile in the wrong spot.
        if [ -d /etc/ufw/applications.d/nginx ]; then
          rm -f /etc/ufw/applications.d/nginx/ufw.profile
          rmdir /etc/ufw/applications.d/nginx
        fi
        rm -f /etc/logrotate.d/nginx-full
        rm -f /etc/logrotate.d/nginx-light
        rm -f /etc/logrotate.d/nginx-extras
        rm -f /etc/logrotate.d/nginx-common
        ;;
    
      abort-upgrade)
        ;;
    
      *)
        echo "preinst called with unknown argument \`$1'" >&2
        exit 1
        ;;
    esac
    
    
    
    exit 0
    
    
    %post -p /bin/sh
    #!/bin/sh
    set -e
    
    . /usr/share/debconf/confmodule
    
    # Handle naxsi removal
    dpkg-maintscript-helper rm_conffile \
                      /etc/nginx/naxsi.rules         1.6.2-2~ -- "$@"
    dpkg-maintscript-helper rm_conffile \
                      /etc/nginx/naxsi_core.rules    1.6.2-2~ -- "$@"
    dpkg-maintscript-helper rm_conffile \
                      /etc/nginx/naxsi-ui.conf.1.4.1 1.6.2-2~ -- "$@"
    dpkg-maintscript-helper rm_conffile \
                      /etc/nginx/naxsi-ui.conf       1.6.2-2~ -- "$@"
    
    # Handle upstart removal
    dpkg-maintscript-helper rm_conffile \
                      /etc/init/nginx.conf           1.13.5-1~ -- "$@"
    
    case "$1" in
      configure)
        logdir="/var/log/nginx"
    
        # Allow local admin to override
        if ! dpkg-statoverride --list "$logdir" >/dev/null; then
          chown root:adm $logdir
          chmod 0755 $logdir
        fi
    
        # Secure default logfiles on fresh installations
        if [ -z "$2" ]; then
          access_log="$logdir/access.log"
         error_log="$logdir/error.log"
    
          if [ ! -e "$access_log" ]; then
            touch "$access_log"
            chmod 640 "$access_log"
            chown www-data:adm "$access_log"
          fi
    
          if [ ! -e "$error_log" ]; then
            touch "$error_log"
            chmod 640 "$error_log"
            chown www-data:adm "$error_log"
          fi
        fi
    
        # If a symlink doesn't exist and can be created, then create it.
        if [ -z $2 ] && [ ! -e /etc/nginx/sites-enabled/default ] &&
           [ -d /etc/nginx/sites-enabled ] && [ -d /etc/nginx/sites-available ]; then
          ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
        fi
    
        # Create a default index page when not already present.
        if [ ! -e /var/www/html/index.nginx-debian.html ]; then
          cp /usr/share/nginx/html/index.html /var/www/html/index.nginx-debian.html
        fi
    
        ;;
    
      abort-upgrade|abort-remove|abort-deconfigure)
        ;;
    
    ```

  + 不生成脚本alien转换

    ```bash
    [root@localhost nginx_pkg_deb]# alien --to-rpm nginx-common_1.14.0-0ubuntu1.11_all.deb 
    Warning: Skipping conversion of scripts in package nginx-common: postinst postrm preinst
    Warning: Use the --scripts parameter to include the scripts.
    nginx-common-1.14.0-1.noarch.rpm generated
    ```

    ```bash
    [root@localhost nginx_pkg_deb]# rpmrebuild -pe nginx-common-1.14.0-1.noarch.rpm 
    (GenRpmQf) remove tag line ENHANCESFLAGS
    (GenRpmQf) remove tag line ENHANCESNAME
    (GenRpmQf) remove tag line ENHANCESVERSION
    (GenRpmQf) remove tag line SUGGESTSFLAGS
    (GenRpmQf) remove tag line SUGGESTSNAME
    (GenRpmQf) remove tag line SUGGESTSVERSION
    Do you want to continue ? (y/N) y
    warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.87933/work/root/usr/share/nginx/modules
    result: /root/rpmbuild/RPMS/noarch/nginx-common-1.14.0-1.noarch.rpm
    [root@localhost nginx_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/noarch/nginx-common-1.14.0-1.noarch.rpm
    Verifying...                          ################################# [100%]
    Preparing...                          ################################# [100%]
    Updating / installing...
       1:nginx-common-1.14.0-1            ################################# [100%]
    ```

    

+ libnginx-mod-http-geoip-1.14.0-1.x86_64.rpm

  ```bash
  [root@localhost nginx_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/x86_64/libnginx-mod-http-geoip-1.14.0-1.x86_64.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:libnginx-mod-http-geoip-1.14.0-1 ################################# [100%]
  ```

+ libnginx-mod-http-image-filter-1.14.0-1.x86_64.rpm

  ```bash
  [root@localhost nginx_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/x86_64/libnginx-mod-http-image-filter-1.14.0-1.x86_64.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:libnginx-mod-http-image-filter-1.################################# [100%]
  
  ```

+ libnginx-mod-http-xslt-filter-1.14.0-1.x86_64.rpm

  ```bash
  [root@localhost nginx_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/x86_64/libnginx-mod-http-xslt-filter-1.14.0-1.x86_64.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:libnginx-mod-http-xslt-filter-1.1################################# [100%]
  ```

+ libnginx-mod-mail-1.14.0-1.x86_64.rpm

  ```bash
  [root@localhost nginx_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/x86_64/libnginx-mod-mail-1.14.0-1.x86_64.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:libnginx-mod-mail-1.14.0-1       ################################# [100%]
  ```

+ libnginx-mod-stream-1.14.0-1.x86_64.rpm

  ```bash
  [root@localhost nginx_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/x86_64/libnginx-mod-stream-1.14.0-1.x86_64.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:libnginx-mod-stream-1.14.0-1     ################################# [100%]
  ```

+ nginx-core-1.14.0-1.x86_64.rpm

  ```bash
  [root@localhost nginx_pkg_deb]# rpm -ivh nginx-core-1.14.0-1.x86_64.rpm
  error: Failed dependencies:
  	libpcre.so.3()(64bit) is needed by nginx-core-1.14.0-1.x86_64
  ```

  + 解决方法：alien 转换libpcre3_8.39-9_amd64.deb

    ```bash
    [root@localhost nginx_pkg_deb]# rpmrebuild -pe libpcre3-8.39-10.x86_64.rpm
    (GenRpmQf) remove tag line ENHANCESFLAGS
    (GenRpmQf) remove tag line ENHANCESNAME
    (GenRpmQf) remove tag line ENHANCESVERSION
    (GenRpmQf) remove tag line SUGGESTSFLAGS
    (GenRpmQf) remove tag line SUGGESTSNAME
    (GenRpmQf) remove tag line SUGGESTSVERSION
    Do you want to continue ? (y/N) y
    warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.90090/work/root/lib/x86_64-linux-gnu/libpcre.so.3
    warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.90090/work/root/usr/lib/x86_64-linux-gnu/libpcreposix.so.3
    ```

  + ```bash
    [root@localhost nginx_pkg_deb]# rpm -ql libpcre3-8.39-10
    /lib/x86_64-linux-gnu
    /lib/x86_64-linux-gnu/libpcre.so.3
    /lib/x86_64-linux-gnu/libpcre.so.3.13.3
    /usr
    /usr/lib/x86_64-linux-gnu
    /usr/lib/x86_64-linux-gnu/libpcreposix.so.3
    /usr/lib/x86_64-linux-gnu/libpcreposix.so.3.13.3
    /usr/share
    /usr/share/doc
    /usr/share/doc/libpcre3
    /usr/share/doc/libpcre3/AUTHORS
    /usr/share/doc/libpcre3/NEWS.gz
    /usr/share/doc/libpcre3/README.Debian
    /usr/share/doc/libpcre3/README.gz
    /usr/share/doc/libpcre3/changelog.Debian.gz
    /usr/share/doc/libpcre3/copyright
    /usr/share/man
    /usr/share/man/man3
    /usr/share/man/man3/pcrepattern.3.gz
    ```

  + ```bash
    ln -s /lib/x86_64-linux-gnu/libpcre.so.3.13.3 /lib/lib64/libpcre.so.3
    [root@localhost nginx_pkg_deb]# rpm -ivh nginx-core-1.14.0-1.x86_64.rpm 
    error: Failed dependencies:
    	libpcre.so.3()(64bit) is needed by nginx-core-1.14.0-1.x86_64
    
    # 修改spec， 增加provides   by wangzhi
    
    # 虽然安装成功，但仍然存在脚本执行出错的问题
    ```

+ nginx-1.14.0-1.noarch.rpm

  ```bash
  [root@localhost nginx_pkg_deb]# rpmrebuild -pe nginx-1.14.0-1.noarch.rpm
  (GenRpmQf) remove tag line ENHANCESFLAGS
  (GenRpmQf) remove tag line ENHANCESNAME
  (GenRpmQf) remove tag line ENHANCESVERSION
  (GenRpmQf) remove tag line SUGGESTSFLAGS
  (GenRpmQf) remove tag line SUGGESTSNAME
  (GenRpmQf) remove tag line SUGGESTSVERSION
  Do you want to continue ? (y/N) y
  warning: Explicit %attr() mode not applicable to symlink: /root/.tmp/rpmrebuild.96255/work/root/usr/share/doc/nginx/changelog.Debian.gz
  result: /root/rpmbuild/RPMS/noarch/nginx-1.14.0-1.noarch.rpm
  
  
  [root@localhost nginx_pkg_deb]# rpm -ivh /root/rpmbuild/RPMS/noarch/nginx-1.14.0-1.noarch.rpm
  Verifying...                          ################################# [100%]
  Preparing...                          ################################# [100%]
  Updating / installing...
     1:nginx-1.14.0-1                   ################################# [100%]
  ```

  

### 开始测试nginx

+ 问题1

```bash
[root@localhost nginx_pkg_deb]# nginx
nginx: error while loading shared libraries: libpcre.so.3: cannot open shared object file: No such file or directory
# 解决
ln -s /usr/lib/x86_64-linux-gnu/libpcre.so.3 /usr/lib64/libpcre.so.3
```

+ 问题2

```bash
root@localhost nginx_pkg_deb]# nginx
nginx: [emerg] getpwnam("www-data") failed in /etc/nginx/nginx.conf:1

# 分析
这个问题，应该是在spec文件中，pre，post之类，在安装后需要添加用户，因为脚本执行错误，所以并没有添加、

# 解决方法
vim /etc/nginx/nginx.conf

user nobody;
```

+ 问题3

```
nginx 正常启动，但端口未启动 ---> 配置文件
```





## 问题总结

+ 问题1，alien转换后的rpm不能直接安装，需要通过rpmrebuild去修改spec。同时，部分包，例如群里提到的 libpcre.so.3()(bit), 需要手动去修改比较具体的spec粒度。
+ 问题2，生成的rpm包的spec文件中，%pre，%post部分，存在一些与dpkg，debconf 有关的命令，会导致安装失败
  + 目前的解决方法是 `先不关注这些脚本，选择不生成他们`。可以关注下有没有必要去安装deb，dpkg这些相关的包
+ 问题3，问题2的副作用，导致像nginx的配置文件，以及examples有部分缺失，目前不能确定问题2中的脚本影响有多大。
+ 问题4，目前只展示了nginx基本功能：展示一个html文件，其他功能未验证
+ 问题5，alien的可靠性，最后一次更新是2016年