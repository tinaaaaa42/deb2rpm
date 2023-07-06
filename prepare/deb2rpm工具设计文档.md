## 1. 需求分析

### 1.1 需求描述

1. 迁移需求： 将ubuntu （18.04, 22.04）的deb软件包，通过工具自动化转化为在openEuler 22.03-LTS上可运行的rpm软件包
2. 兼容性需求： 转化出的rpm软件包，要求通过构建测试、兼容性测试
3. 升级需求： 支持自动化迭代优化

### 1.2 依赖组件

| 组件      | 组件描述  | 可获得性 |
| --------- | ------ | --------- |
| python3    | python3 及以上版本 | 可使用 `dnf/yum` 进行安装 |
| python3-concurrent-log-handler | logging日志辅助模块，用于日志转储 | 可使用 `dnf/yum` 进行安装 |
| dpkg | 系统上处理deb软件包的基础指令 | 可只用 `dnf/yum` 进行安装 |
| dpkg-devel | 提供一些开发工具，包括 dpkg-source | 可使用 `dnf/yum` 进行安装 |
| debhelper |  提供一些构建deb包的工具 | 配置oepkgs镜像源，可使用 `dnf/yum` 进行安装 |
| ruby | ruby 2.7及以上版本 | 可使用 `dnf/yum` 进行安装 |
| ruby-devel | 提供ruby一些开发工具 | 可使用 `dnf/yum` 进行安装 |
| rubygems | ruby的包管理器，功能上类似于 apt-get、yum等 | 可使用 `dnf/yum` 进行安装 |
| fpm | linux下的一款开源打包工具，可实现deb包转换成rpm包 | 可使用 `gem` 进行安装 |

### 1.3 License

Mulan V2

## 2. 设计概述

### 2.1 整体方案分析
