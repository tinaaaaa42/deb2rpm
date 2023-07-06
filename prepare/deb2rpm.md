# deb2rpm



## 1.需求分析

### 1.1需求链接

+ 丰富openEuler生态，引入ubuntu 7K+ 软件包

### 1.2功能描述

+ 输入源码包名，输出通过DEB转换后的RPM二进制包

### 1.3方案对齐记录

+ 1.13（泽旭、王执、开田、王铮） 

  ```bash
  1、deb2rpm demo 展示
  ```

+ 2.13  (李萍、王铮) 

  ```bash
  1、a ubuntu 上有， openEuler 没有
  2、deb --> rpm
  3、a --> b / c 
  4、b c openEuler 上有，版本要求一致，b c 需要转换？
  5、版本不一致，通过多版本软件包 构建 (众智任务)
  6、只转换 a， pre 脚本逻辑难以处理
  ```

+ 2.22 (李萍、王铮)

  ```bash
  1、实验确认了 deb包中存在preinstall、postinstall等脚本的包数量占比不大
  ```

+ 2.28 (李萍、王铮)

  ```bash
  1、达成共识：fpm、alien 等包转换工具能力有限，转换后SPEC不存在 ./configure, make, make install 等编译信息
  2、debian 源码包的结构，包括control、rules 等重要文件，control可以做到映射，rules指导编包，很难提取生成SPEC
  3、初步方案：跳过build的过程，直接转换二进制包，运行时依赖如果不存在openEuler对应版本，则递归引入对应的软件包
  ```

+ 3.7 - 3.8 (李萍、王铮、陈辰)

  ```bash
  1、讨论MVP版本框架图
  2、确定三个数据库：ubuntu repo main 分支、openEuler everything 分支、 oepkgs 
  ```


+ 3.10（李萍、王铮、陈辰）

  ```bash
  1、确定rpm与deb 软件版本比较规则
  ```




## 2.方案设计

### 2.1整体方案分析

![img](C:/Users/w30041197/AppData/Roaming/eSpace_Desktop/UserData/w30041197/imagefiles/originalImgfiles/7DFF7939-92C1-4C54-A67B-DC48101C8F4A.png)

### 2.2 详细设计

#### 2.2.1 类

+ Deb

```bash
属性：
	1、deb 软件包的元信息
	2、包名映射信息
	3、文件解压信息
方法:
	1、parse_depend(self) # 解析依赖
	2、add_require_version(self) # 被需要的版本
	
	3、add_mapping_info(self, pkg_name, pkg_version) # 包名映射存储
	4、add_rpm_require(self) # 映射之后软件包被需要的版本  
	
	5、convert_package(self, repo, work_dir) # deb2rpm
		5-1、download_package(self, repo, workdir)
		5-2、check_script(self)
		5-3、convert_deb_to_rpm(self, workdir)
		5-4、convert_rpm_to_rpm(self, workdir)
```

+ Data

```bash
属性：
	1、config 
	2、deb_database
    3、src_deb_database
    4、deb_provides_database
    5、rpm_database
    6、pkg_name_mapping_database
方法：
	1、download_database
	2、load_database
	3-7、normalize_xxx_database
	8- 、get_xxx_from_xxx_database
```

+ Sqlite + Json 数据库

```bash
PriamryPackages
PrimaryProvides
SqliteConnector
SqliteCreator
JsonOperator
```

#### 2.2.2 主函数

```bash
1、read_yaml()
2、get_pkg_list_by_source(args.pkg)
2、breadth_first_search_package(pkg_list) # 解析depend，搜索依赖图
3、convert_package()
```

## 3 疑难杂症

```bash
Depends: libc6 (>= 2.14), libncursesw5 (>= 6), libtinfo5 (>= 6)

1、Depends = (deb package) + (deb package provides)
	1-1、deb_package (>= version) ----> package name mapping ---->  rpm_package(>= version)
	1-2、deb_provides  ----> pkg_who_provides ----> package name mapping ----> rpm_package
```

### 3.1 deb 与 rpm 软件版本比较

```bash
1、depend   ----->   flag  + pkg1 + （upstream + debian）
2、pkg1 ----> pkg2
3、pkg2 -----> pkg2 + version +release 
4、(epoch + upstream + debian)  flag (epoch + version + release) 
```

```bash
### 参考结论
1、epoch 字段只在自身操作系统体系有意义
	1-1、 ubuntu与ubuntu之间， epoch可以比较
	1-2、 ubuntu与openEuler之间，比较epoch没有意义 

2、release
	2-1、同一Version下，不同release版本差异较小
	2-2、不同体系下，release版本不存在比较的意义

3、在比较DEB与RPM的版本时，只比较version， 即上游版本
```

```bahs
### deb depend 修正放缩，把所要求的版本包含在内

1、存在 '|' 字符的依赖， 修正只取第一个作为依赖项
	Depends: debconf (>= 0.5) | debconf-2.0    ---->    Depends: debconf (>= 0.5) 

2、存在EPOCH的依赖，忽略EPOCH，上下放缩
	Depends: libgcc1 (>= 1:3.0)    ---->   Depends: libgcc1 (>= 3.0)
	
3、存在release版本的依赖，忽略release版本，并上下放缩
	Depends: libicu60 (>= 60.1-1~) ----> Depends: libicu60 (>= 60.1)
	Depends: libvips42 (>> 8.0.2-1~) ----> Depends: libvips42 (>= 8.0.2)
	Depends: git (>> 1:2.17.0), git (<< 1:2.17.0-.) ----> Depends: git (>= 2.17.0), git (<= 2.17.0)
	Depends: dkimproxy (<= 1.4.1-3)  ----> dkimproxy (<= 1.4.1)
	Depends：python (<< 2.8) ----> python (< 2.8)
	
4、不存在release、epoch，上下放缩
	Depends: adduser (>> 3.51)  ---->  Depends: adduser (>= 3.51) 
```



### 3.2 软件依赖中deb_provides 映射RPM包名以及版本约束

+ 从统计数据中可以看出，含有 `provides中的数据`的软件包较少
+ 其中，指定了版本约束的依赖仅有`41`条
+ 映射结论：depend ---->  deb_who_provides ----> pkg_name_mapping ----> rpm_package
+ 版本约束：【不加约束】 或者 【>= 最小版本】  （待定？）

|                                                              |        |
| ------------------------------------------------------------ | ------ |
| DEB软件包个数                                                | 60866  |
| 含有Provides字段的软件包个数                                 | 7759   |
| Provides中指定版本的软件包个数，例如php-phpseclib Provides: php-seclib (= 2.0.9-1) | 174    |
| 所有软件包的depend数量和                                     | 257055 |
| 对所有软件包的depend去重后的数量                             | 51387  |
| depend中属于 provides 数据库中的依赖去重                     | 1822   |
| depend中属于 provides数据库 且 有版本限制的数量              | 41     |



```bash
# depends 中属于provides 数据库且有版本限制的全部例子
node-babel-plugin-transform-es2015-shorthand-properties (>= 6.22.0)
kodi-api-pvr (= 5.2.1)
steam (= 1:1.0.0.54+repack-5ubuntu1)
libapt-inst (= 1.6.1)
rtcw-data (>= 1.42b+40)
systemd-shim (>= 10-3~)
node-babel-plugin-transform-es2015-modules-commonjs (>= 6.24.1)
node-babel-plugin-transform-es2015-computed-properties (>= 6.22.0)
node-babel-plugin-transform-es2015-object-super (>= 6.22.0)
php5 (>= 5.4.26)
python3-cffi-backend-api-max (>= 9729)
node-babel-plugin-transform-es2015-typeof-symbol (>= 6.23.0)
obexd-client (>= 0.47)
node-babel-plugin-transform-es2015-duplicate-keys (>= 6.22.0)
node-babel-plugin-transform-es2015-arrow-functions (>= 6.22.0)
node-babel-plugin-transform-es2015-destructuring (>= 6.23.0)
node-babel-plugin-check-es2015-constants (>= 6.22.0)
node-babel-plugin-transform-es2015-modules-amd (>= 6.22.0)
firefox-esr (>= 30)
node-babel-plugin-transform-es2015-sticky-regex (>= 6.22.0)
kodi-api-guilib (= 5.11.0)
python-cffi-backend-api-max (>= 9729)
node-babel-plugin-transform-es2015-modules-commonjs (>= 6.23.0)
node-babel-plugin-transform-es2015-modules-umd (>= 6.23.0)
libapt-pkg (= 1.6.1)
libcuda1 (>= 387.26)
node-babel-plugin-transform-es2015-template-literals (>= 6.22.0)
node-babel-plugin-transform-es2015-for-of (>= 6.23.0)
node-babel-plugin-transform-es2015-modules-systemjs (>= 6.23.0)
python-cffi-backend-api-min (<= 9729)   【openEuler 有对应的包， python3-cffi】
obexd-server (>= 0.47)
node-babel-plugin-transform-es2015-unicode-regex (>= 6.22.0)
node-babel-plugin-transform-es2015-classes (>= 6.23.0)
node-babel-plugin-transform-es2015-block-scoped-functions (>= 6.22.0)
node-babel-plugin-transform-es2015-block-scoping (>= 6.23.0)
python3-cffi-backend-api-min (<= 9729)
fileutils (>= 4.0-5)
node-babel-plugin-transform-es2015-function-name (>= 6.22.0)
python-pyatspi2 (>= 0.1.7)
node-babel-plugin-transform-es2015-spread (>= 6.22.0)
node-babel-plugin-transform-es2015-literals (>= 6.22.0)
node-babel-plugin-transform-es2015-parameters (>= 6.23.0)
```



```bash
# Provides中指定版本的软件包例子
node-babel-plugin-transform-es2015-modules-amd (= 6.24.1)
gir1.2-pangocairo-1.0 (= 1.40.14-1)
python3-cffi-backend-api-max (= 10495)
node-babel-plugin-transform-es2015-duplicate-keys (= 6.24.1)
debhelper-compat (= 9)
node-babel-plugin-transform-es2015-unicode-regex (= 6.24.1)
libsmbios2 (= 2.3.1-1)
gir1.2-xfixes-4.0 (= 1.56.1-1)
mailman3-core (= 3.1.1-5)
gir1.2-gobject-2.0 (= 1.56.1-1)
babeljs (= 6.26.0+dfsg-3build6)
pypy-cffi (= 1.11.2)
libapt-inst (= 1.6.1)
```



### 3.3 包名映射后是否能够保证是一个包含的状态（重要）

```bash
1、depend: libc6 (>= 2.14)
	1-1: 如果想要完全替换这一个依赖，需要保证替换后 软件依赖libc6 的信息被完全包含， 包名映射是否能够满足这一点[?]
    1-2：如果满足也仅仅是在包的维度进行映射
2、举例：debian: libjemalloc1 与 openEuler：jemalloc
	2-1: 这两个软件包属于同一个上游软件包 
	2-2: libjemalloc1 提供 libjemalloc.so.1, jemalloc 提供 libjemalloc.so.2
3、x2openEuler 经验：
	3-1：当一个动态库libxxx.a.b.c的小版本改变后，其中的函数可能会发生变化，这时要分析某个二进制所依赖的外部函数是否在差异函数里面
	3-2：从数据库统计所得，centos-openEuler 动态库差异函数在1-2w，ubuntu-openEuler 动态库差异函数在10-20w
```



### 3.4 软件的breaks、conflicts 这些字段是否能直接映射





