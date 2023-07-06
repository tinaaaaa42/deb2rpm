# ubuntu迁移工具demo



## 流程图

![image-20230106164331291](C:\Users\w30041197\AppData\Roaming\Typora\typora-user-images\image-20230106164331291.png)



## 步骤1（完成度80%）

+ 获取deb软件包的集合

  + 手动输入强关联的包
  + wget获取系统层面的包

+ 获取软件的依赖关系

  + 过滤 dpkg的数据库文件
  + 强连通分量缩点形成DAG图，给每一个依赖计算深度

+ 确认需要转换的软件包

  ![image-20230105202628287](C:\Users\w30041197\AppData\Roaming\Typora\typora-user-images\image-20230105202628287.png)

  + 任意一个软件都可以找到一棵对应的依赖树
  + 将存在映射关系的软件包 以及 白名单（与deb强相关的包，例如debconf，dpkg）中的软件包，标黑色，一定能得到一颗被黑色截断的树
  + 根据依赖树重新组装软件的映射关系

## 步骤2（完成度100%）

+ fpm 转换软件包（deb to rpm）



## 步骤3（完成度100%）

+ 根据步骤1得到的依赖树，重新组装依赖关系
  + G、F：直接根据映射关系替换依赖
  + A、B、C：用转换后的rpm包的名字替换依赖关系
+ 映射关系使用的之前按照 so对应得出来的映射关系，和一部分手动添加的映射关系



## 步骤4（完成度0%）

+ 目前没想法怎么去做这一部分
+ 因为是脚本中存在与dpkg相关的命令



## 步骤5 （完成度0%）

+ 暂未安装测试





## 结果展示

### nginx

+ 输入业务相关的包

  ![image-20230106165502615](C:\Users\w30041197\AppData\Roaming\Typora\typora-user-images\image-20230106165502615.png)

+ 运行py文件

  ![image-20230106165702314](C:\Users\w30041197\AppData\Roaming\Typora\typora-user-images\image-20230106165702314.png)

+ 得到结果（业务本身软件 + 系统差异软件 +  安装脚本）

  ![image-20230106165729812](C:\Users\w30041197\AppData\Roaming\Typora\typora-user-images\image-20230106165729812.png)

  + nginx_install.sh(目的是确定软件包的安装顺序，处于依赖树更底层的软件包应该优先被安装)

```bash
dnf install libpcre3-8.39-9ubuntu0.1.x86_64.rpm
dnf install lsb-base-9.20170808ubuntu1-1.noarch.rpm
dnf install nginx-common-1.14.0-0ubuntu1.11.noarch.rpm
dnf install libnginx-mod-http-geoip-1.14.0-0ubuntu1.11.x86_64.rpm
dnf install libnginx-mod-http-image-filter-1.14.0-0ubuntu1.11.x86_64.rpm
dnf install libnginx-mod-http-xslt-filter-1.14.0-0ubuntu1.11.x86_64.rpm
dnf install libnginx-mod-mail-1.14.0-0ubuntu1.11.x86_64.rpm
dnf install libnginx-mod-stream-1.14.0-0ubuntu1.11.x86_64.rpm
dnf install nginx-core-1.14.0-0ubuntu1.11.x86_64.rpm
dnf install nginx-1.14.0-0ubuntu1.11.noarch.rpm
```

+ 验证软件包的依赖关系

  + 转换后

  ```bash
  root@wangzheng-Virtual-Machine:~/rebuild/nginx_rpm# rpm -qpR libpcre3-8.39-9ubuntu0.1.x86_64.rpm
  /bin/sh
  /bin/sh
  /bin/sh
  /bin/sh
  /bin/sh
  /bin/sh
  /bin/sh
  glibc-2.28-49.oe1.x86_64
  rpmlib(CompressedFileNames) <= 3.0.4-1
  rpmlib(PayloadFilesHavePrefix) <= 4.0-1
  
  root@wangzheng-Virtual-Machine:~/rebuild/nginx_rpm# rpm -qpR nginx-core-1.14.0-0ubuntu1.11.x86_64.rpm
  /bin/sh
  /bin/sh
  /bin/sh
  /bin/sh
  /bin/sh
  /bin/sh
  /bin/sh
  /bin/sh
  glibc-2.28-49.oe1.x86_64
  iproute-5.5.0-4.oe1.x86_64
  libnginx-mod-http-geoip-1.14.0-0ubuntu1.11.x86_64
  libnginx-mod-http-image-filter-1.14.0-0ubuntu1.11.x86_64
  libnginx-mod-http-xslt-filter-1.14.0-0ubuntu1.11.x86_64
  libnginx-mod-mail-1.14.0-0ubuntu1.11.x86_64
  libnginx-mod-stream-1.14.0-0ubuntu1.11.x86_64
  libpcre3-8.39-9ubuntu0.1.x86_64
  nginx-common-1.14.0-0ubuntu1.11.noarch
  openssl-libs-1.1.1f-1.oe1.x86_64
  rpmlib(CompressedFileNames) <= 3.0.4-1
  rpmlib(PayloadFilesHavePrefix) <= 4.0-1
  zlib-1.2.11-17.oe1.x86_64
  ```

  + 转换前

  ```bash
  root@wangzheng-Virtual-Machine:~/rebuild/nginx# dpkg --info libpcre3_8.39-9ubuntu0.1_amd64.deb | grep Depends
   Depends: libc6 (>= 2.14)
   
  root@wangzheng-Virtual-Machine:~/rebuild/nginx# dpkg --info nginx-core_1.14.0-0ubuntu1.11_amd64.deb | grep Depends
   Depends: iproute2, libnginx-mod-http-geoip (= 1.14.0-0ubuntu1.11), libnginx-mod-http-image-filter (= 1.14.0-0ubuntu1.11), libnginx-mod-http-xslt-filter (= 1.14.0-0ubuntu1.11), libnginx-mod-mail (= 1.14.0-0ubuntu1.11), libnginx-mod-stream (= 1.14.0-0ubuntu1.11), nginx-common (= 1.14.0-0ubuntu1.11), libc6 (>= 2.27), libpcre3, libssl1.1 (>= 1.1.0), zlib1g (>= 1:1.1.4)
  ```

### 	redis	

+ 结果相似