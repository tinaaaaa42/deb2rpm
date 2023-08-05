本部分将具体地完善`spec`文件各必要字段的生成方式。
部分内容的映射需要用到已有的Package信息，见[https://repo.huaweicloud.com/ubuntu/dists/bionic](https://repo.huaweicloud.com/ubuntu/dists/bionic)，以下称为`Package池`。
相应的，也有`Source池`。

# deb2spec
## 元数据部分
### 主软件包部分
| spec   | deb来源 |
| :----: | :----:  |
| Name   | control文件中的Source |
| Version | Package池中的Version |
| Release | Package池中的Version |
| Summary | Package池中的Description |
| License | copyright文件中的License |
| URL     | control文件中的Homepage |
| Source0 | Source池中对应文件 |
| %description | control文件中的Description |
| BuildRequires | Source池中的Build-Depends |
| Requires | Package池中的Depends | 
| Conflict | Package池中的Breaks |
| Provides | Package池中的Provides |
| Recommends | Package池中的Recommends |
| %files | 脚本工具获取 |
| %changelog | changelog文件 |

依赖相关的`BuildRequires`、`Requires`、`Conflicts`、`Provides`、`Recommands`等内容需要通过包名映射进行相应转化。

### 子包部分
| spec | deb来源 |
| :---: | :---: |
| 包名  | control文件中所有Package |
| Summary | Package池中的Description |
| BuildArch | Package池中的Architecture |
| %description | control文件中的Description |
| Requires | Package池中的Depends |
| Conflict | Package池中的Breaks |
| Provides | Package池中的Provides |
| Recommends | Package池中的Recommends |
| %files | 脚本工具获取 |

## 命令阶段
### %prep
脚本工具完成解压，spec文件中无需写`%prep`

### %build
脚本工具完成build，spec文件中无需写`%build`

## %install
将所有在debian目录下子包文件夹中的文件复制到`BUILDROOT`中

# spec2deb
以下是由deb文件到spec文件的其他补充内容
## control文件
| deb | spec |
| :---: | :---: |
| Standards-Version | Version |
| Section | Group |
| Build-Depends-Arch | BuildRequires |
| BUild-Depends-Indep | BuildRequires |
| Pre-Depends | Requires |

## Source池
| Source池 | spec |
| :---: | :---: |
| Directory + Files | Source |
| Package-List | 所有子包 |