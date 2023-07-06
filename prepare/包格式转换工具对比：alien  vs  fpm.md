# 包格式转换工具对比：alien  vs  fpm



## 对比

|                                |               alien                |                 fpm                 |
| ------------------------------ | :--------------------------------: | :---------------------------------: |
| github地址                     |  https://github.com/mildred/alien  | https://github.com/jordansissel/fpm |
| 收藏数                         |                 25                 |                10.6K                |
| 最近更新时间                   |               2011年               |               三周前                |
| 是否支持deb转rpm               |                支持                |                支持                 |
|                                |                                    |                                     |
| 转换是否成功（转换时）         | 全部成功，目前未碰到转换失败的例子 |      存在失败的情况，举例nginx      |
| 是否支持Autoreq 字段（转换时） |               不支持               |                支持                 |
|                                |                                    |                                     |
| 是否会有文件冲突（转换后）     |                 有                 |                没有                 |
| 依赖关系是否正确（转换后）     |     依赖部分缺失，甚至全部缺失     |      依赖关系沿用Ubuntu的包名       |
| 是否能够成功安装（转换后）     |                 ~                  |                  ~                  |



## fpm 转换包失败的例子

```bash
fpm -s deb -t rpm --verbose nginx_1.14.0-0ubuntu1.11_all.deb

错误：行 56：依赖项标记必须以字母、数字，_ 或 '/' 开头：Requires: nginx-core (<< 1.14.0-0ubuntu1.11.1~) | nginx-full (<< 1.14.0-0ubuntu1.11.1~) | nginx-light (<< 1.14.0-0ubuntu1.11.1~) | nginx-extras (<< 1.14.0-0ubuntu1.11.1~) {:level=>:info}
```

+ 分析：deb下的depends，具有 竖线（|）这个字符，RPM不能处理





## fpm添加--rpm-auto-req 选项和不添加    转换的软件包依赖关系对比

```bash
# 不添加Autoreq选项
[root@localhost ~]# rpm -q --requires nginx1.rpm
/bin/sh
/bin/sh
iproute2
libc6 >= 2.27
libnginx-mod-http-geoip = 1.14.0-0ubuntu1.11
libnginx-mod-http-image-filter = 1.14.0-0ubuntu1.11
libnginx-mod-http-xslt-filter = 1.14.0-0ubuntu1.11
libnginx-mod-mail = 1.14.0-0ubuntu1.11
libnginx-mod-stream = 1.14.0-0ubuntu1.11
libpcre3
libssl1.1 >= 1.1.0
nginx-common = 1.14.0-0ubuntu1.11
rpmlib(CompressedFileNames) <= 3.0.4-1
rpmlib(PayloadFilesHavePrefix) <= 4.0-1
zlib1g >= 1:1.1.4

```



```bash
# 添加Autoreq选项
[root@localhost ~]# rpm -q --requires nginx2.rpm
/bin/sh
/bin/sh
iproute2                    // (ubuntu 下软件包名)
libc.so.6()(64bit)
libc.so.6(GLIBC_2.10)(64bit)
libc.so.6(GLIBC_2.14)(64bit)
libc.so.6(GLIBC_2.17)(64bit)
libc.so.6(GLIBC_2.2.5)(64bit)
libc.so.6(GLIBC_2.27)(64bit)
libc.so.6(GLIBC_2.3)(64bit)
libc.so.6(GLIBC_2.3.2)(64bit)
libc.so.6(GLIBC_2.3.4)(64bit)
libc.so.6(GLIBC_2.4)(64bit)
libc.so.6(GLIBC_2.7)(64bit)
libc6 >= 2.27               // (ubuntu 下软件包名)
libcrypt.so.1()(64bit)
libcrypt.so.1(GLIBC_2.2.5)(64bit)
libcrypto.so.1.1()(64bit)
libcrypto.so.1.1(OPENSSL_1_1_0)(64bit)
libdl.so.2()(64bit)
libdl.so.2(GLIBC_2.2.5)(64bit)
libnginx-mod-http-geoip = 1.14.0-0ubuntu1.11           // (ubuntu 下软件包名)
libnginx-mod-http-image-filter = 1.14.0-0ubuntu1.11    // (ubuntu 下软件包名)
libnginx-mod-http-xslt-filter = 1.14.0-0ubuntu1.11     // (ubuntu 下软件包名)
libnginx-mod-mail = 1.14.0-0ubuntu1.11                 // (ubuntu 下软件包名)
libnginx-mod-stream = 1.14.0-0ubuntu1.11               // (ubuntu 下软件包名)
libpcre.so.3()(64bit)
libpcre3                                               // (ubuntu 下软件包名)
libpthread.so.0()(64bit)
libpthread.so.0(GLIBC_2.2.5)(64bit)
libpthread.so.0(GLIBC_2.3.2)(64bit)
libssl.so.1.1()(64bit)
libssl.so.1.1(OPENSSL_1_1_0)(64bit)
libssl1.1 >= 1.1.0                                     // (ubuntu 下软件包名)
libz.so.1()(64bit)
nginx-common = 1.14.0-0ubuntu1.11                      // (ubuntu 下软件包名)
rpmlib(CompressedFileNames) <= 3.0.4-1
rpmlib(PayloadFilesHavePrefix) <= 4.0-1
rtld(GNU_HASH)
zlib1g >= 1:1.1.4                                      // (ubuntu 下软件包名)
```

+ 对比结论：
  + Autoreq字段，给RPM包添加了运行时所需要的动态库
  + 两者是包含的关系，前面的依赖关系均在后面的依赖关系中出现



## Alien转换后文件冲突举例

```bash
[root@localhost nginx_pkg_deb]# rpm -ivh lsb-base-9.20170808ubuntu1-2.noarch.rpm 
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
	package lsb-base-9.20170808ubuntu1-2.noarch is already installed
	file / from install of lsb-base-9.20170808ubuntu1-2.noarch conflicts with file from package filesystem-3.14-1.oe1.x86_64
	file /lib from install of lsb-base-9.20170808ubuntu1-2.noarch conflicts with file from package filesystem-3.14-1.oe1.x86_64
```

