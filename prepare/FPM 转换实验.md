# FPM 转换实验------失败原因归类



## 转换失败原因归类

### 失败原因一：

```bash
error: line 57: Dependency tokens must begin with alpha-numeric, '_' or '/': Requires: libc6-dev | libc-dev {:level=>:info}
```

+ deb依赖关系里面有 竖线（|），表示竖线前后软件满足其一即可，但是转换工具不能识别



### 失败原因二：

```bash
error: line 57: Invalid version (double separator '-'): 55-gc9562a1-1~: Requires: qtchooser >= 55-gc9562a1-1~ {:level=>:info}
```

+ 有些deb的版本号，转换工具不能识别



## 转换失败的包

|                         包名                         | 失败原因 |               失败点                |
| :--------------------------------------------------: | :------: | :---------------------------------: |
|       libbz2-dev_1.0.6-8.1ubuntu0.2_amd64.deb        |  原因一  |        libc6-dev \| libc-dev        |
|      libtrilinos-teuchos12_12.12.1-5_amd64.deb       |  原因一  |      libblas3 \| libblas.so.3       |
|            puppet_5.4.0-2ubuntu3_all.deb             |  原因一  |                                     |
|               libtool_2.4.6-2_all.deb                |  原因一  |                                     |
|        libparpack2-dev_3.5.0+real-2_amd64.deb        |  原因一  |                                     |
|      libscalapack-openmpi2.0_2.0.2-4_amd64.deb       |  原因一  |                                     |
|      libnuma-dev_2.0.11-2.1ubuntu0.1_amd64.deb       |  原因一  |                                     |
| libtrilinos-trilinoscouplings12_12.12.1-5_amd64.deb  |  原因一  |                                     |
|       qdbus_4%3a4.8.7+dfsg-7ubuntu1_amd64.deb        |  原因二  |    qtchooser (>= 55-gc9562a1-1~)    |
|     libfreetype6-dev_2.8.1-2ubuntu2.2_amd64.deb      |  原因一  |                                     |
|        liblapack-dev_3.7.1-4ubuntu1_amd64.deb        |  原因一  |                                     |
|       libtrilinos-tpetra12_12.12.1-5_amd64.deb       |  原因一  |                                     |
|              ant_1.10.5-3~18.04_all.deb              |  原因一  |                                     |
|           libreadline-dev_7.0-3_amd64.deb            |  原因一  |                                     |
|           libmumps-5.1.2_5.1.2-4_amd64.deb           |  原因一  |                                     |
|     libncurses5-dev_6.1-1ubuntu1.18.04_amd64.deb     |  原因一  |                                     |
|         libsuperlu5_5.2.1+dfsg1-3_amd64.deb          |  原因一  |                                     |
|        libarpack2-dev_3.5.0+real-2_amd64.deb         |  原因一  |                                     |
|           libhypre-dev_2.13.0-2_amd64.deb            |  原因一  |                                     |
|       libtrilinos-pliris12_12.12.1-5_amd64.deb       |  原因一  |                                     |
|         liblapack3_3.7.1-4ubuntu1_amd64.deb          |  原因一  |                                     |
|      libhdf5-dev_1.10.0-patch1+docs-4_amd64.deb      |  原因二  |  ibhdf5-100 = 1.10.0-patch1+docs-4  |
|     libpetsc3.7.7_3.7.7+dfsg1-2build5_amd64.deb      |  原因一  |                                     |
|         libicu-dev_60.2-3ubuntu3.2_amd64.deb         |  原因一  |                                     |
|          libcholmod3_1%3a5.1.2-2_amd64.deb           |  原因一  |                                     |
|          libparpack2_3.5.0+real-2_amd64.deb          |  原因一  |                                     |
|         bzip2-doc_1.0.6-8.1ubuntu0.2_all.deb         |  原因一  |                                     |
|      libtrilinos-aztecoo12_12.12.1-5_amd64.deb       |  原因一  |                                     |
|    libavformat57_7%3a3.4.11-0ubuntu0.1_amd64.deb     |  原因一  |                                     |
|           ruby-deep-merge_1.1.1-1_all.deb            |  原因一  |                                     |
|          libumfpack5_1%3a5.1.2-2_amd64.deb           |  原因一  |                                     |
|        libtrilinos-nox12_12.12.1-5_amd64.deb         |  原因一  |                                     |
|         libgl2ps1.4_1.4.0+dfsg1-1_amd64.deb          |  原因一  |                                     |
|          libchromaprint1_1.4.3-1_amd64.deb           |  原因一  |                                     |
|    libncursesw5-dev_6.1-1ubuntu1.18.04_amd64.deb     |  原因一  |                                     |
|      libnetcdf-dev_1%3a4.6.0-2build1_amd64.deb       |  原因一  |                                     |
|      libglu1-mesa-dev_9.0.0-2.1build1_amd64.deb      |  原因一  |                                     |
|          libhypre-2.13.0_2.13.0-2_amd64.deb          |  原因一  |                                     |
|            scala_2.11.12-4~18.04_all.deb             |  原因一  |                                     |
|     libslepc3.7.4_3.7.4+dfsg1-2build8_amd64.deb      |  原因一  |                                     |
|       libsuitesparse-dev_1%3a5.1.2-2_amd64.deb       |  原因一  |                                     |
|         libedit-dev_3.1-20170329-1_amd64.deb         |  原因二  | Requires: libedit2 = 3.1-20170329-1 |
|  liboce-visualization-dev_0.18.2-2build1_amd64.deb   |  原因一  |                                     |
|            rake_12.3.1-1ubuntu0.1_all.deb            |  原因一  |                                     |
|          libarpack2_3.5.0+real-2_amd64.deb           |  原因一  |                                     |
|            ruby-test-unit_3.2.5-1_all.deb            |  原因一  |                                     |
|          varnish_5.2.1-1ubuntu0.1_amd64.deb          |  原因一  |                                     |
|            libspqr2_1%3a5.1.2-2_amd64.deb            |  原因一  |                                     |
|       libsuperlu-dist5_5.3.0+dfsg1-1_amd64.deb       |  原因一  |                                     |
|        libchromaprint-tools_1.4.3-1_amd64.deb        |  原因一  |                                     |
|        build-essential_12.4ubuntu1_amd64.deb         |  原因一  |                                     |
|       nginx-common_1.14.0-0ubuntu1.11_all.deb        |  原因一  |                                     |
|           nginx_1.14.0-0ubuntu1.11_all.deb           |  原因一  |                                     |
|           libp4est-sc-1.1_1.1-5_amd64.deb            |  原因一  |                                     |
|               abinit_8.0.8-4_amd64.deb               |  原因一  |                                     |
|   zlib1g-dev_1%3a1.2.11.dfsg-0ubuntu2.2_amd64.deb    |  原因一  |                                     |
|          libdeal.ii-8.5.1_8.5.1-3_amd64.deb          |  原因一  |                                     |
|       libtrilinos-epetra12_12.12.1-5_amd64.deb       |  原因一  |                                     |
|           med-config_3.0.1ubuntu1_all.deb            |  原因一  |                                     |
|   liboce-visualization11_0.18.2-2build1_amd64.deb    |  原因一  |                                     |
| ca-certificates-java_20180516ubuntu1~18.04.1_all.deb |  原因一  |                                     |
|        libtrilinos-piro12_12.12.1-5_amd64.deb        |  原因一  |                                     |
|           va-driver-all_2.1.0-3_amd64.deb            |  原因一  |                                     |
|         libhwloc-plugins_1.11.9-1_amd64.deb          |  原因一  |                                     |











## 转换成功的软件包

```bash
abinit-data-8.0.8-4.noarch.rpm
alien-8.95-1.noarch.rpm
ant-optional-1.10.5-3~18.04.noarch.rpm
augeas-lenses-1.10.1-2ubuntu1.noarch.rpm
autoconf-2.69-11.noarch.rpm
automake-1.15.1-3ubuntu2.noarch.rpm
autopoint-0.19.8.1-6ubuntu0.3.noarch.rpm
autotools-dev-20180224.1-1.noarch.rpm
bcftools-1.7-2.x86_64.rpm
bcrypt-1.1-8.1build1.x86_64.rpm
bedtools-2.26.0+dfsg-5.x86_64.rpm
binfmt-support-2.1.8-2.x86_64.rpm
binutils-dev-2.30-21ubuntu1~18.04.8.x86_64.rpm
blends-common-0.6.100ubuntu2-1.noarch.rpm
busybox-1.27.2-2ubuntu3.4.x86_64.rpm
cmake-3.10.2-1ubuntu2.18.04.2.x86_64.rpm
cmake-data-3.10.2-1ubuntu2.18.04.2.noarch.rpm
consul-0.6.4~dfsg-3.x86_64.rpm
curl-7.58.0-2ubuntu3.21.x86_64.rpm
debconf-utils-1.5.66ubuntu1-1.noarch.rpm
debugedit-4.14.1+dfsg1-2.x86_64.rpm
default-jre-headless-1.11-68ubuntu1~18.04.1.x86_64.rpm
dh-autoreconf-17-1.noarch.rpm
dh-strip-nondeterminism-0.040-1.1~build1.noarch.rpm
diamond-4.0.515-4ubuntu1.noarch.rpm
dos2unix-7.3.4-3.x86_64.rpm
doxygen-1.8.13-10.x86_64.rpm
dpkg-dev-1.19.0.5ubuntu2.4-1.noarch.rpm
enca-1.19-1.x86_64.rpm
etcd-3.2.17+dfsg-1.noarch.rpm
etcd-client-3.2.17+dfsg-1.x86_64.rpm
etcd-server-3.2.17+dfsg-1.x86_64.rpm
facter-3.10.0-4.x86_64.rpm
fakeroot-1.22-2ubuntu1.x86_64.rpm
figlet-2.2.5-3.x86_64.rpm
fonts-lato-2.0-2.noarch.rpm
fping-4.0-6.x86_64.rpm
g++-7.4.0-1ubuntu2.3.x86_64.rpm
g++-7-7.5.0-3ubuntu1~18.04.x86_64.rpm
gcc-6-base-6.5.0-2ubuntu1~18.04.x86_64.rpm
gcc-7.4.0-1ubuntu2.3.x86_64.rpm
gcc-7-7.5.0-3ubuntu1~18.04.x86_64.rpm
gfortran-7.4.0-1ubuntu2.3.x86_64.rpm
gfortran-7-7.5.0-3ubuntu1~18.04.x86_64.rpm
gir1.2-harfbuzz-0.0-1.7.2-1ubuntu1.x86_64.rpm
gmap-2017-11_15_1.x86_64.rpm
gyp-0.1+20150913git1f374df9-1ubuntu1.noarch.rpm
hdf5-helpers-1.10.0-patch1+docs_4.x86_64.rpm
i965-va-driver-2.1.0-0ubuntu1.x86_64.rpm
ibverbs-providers-17.1-1ubuntu0.2.x86_64.rpm
icu-devtools-60.2-3ubuntu3.2.x86_64.rpm
iotop-0.6-2.x86_64.rpm
iperf-2.0.10+dfsg1-1ubuntu0.18.04.2.x86_64.rpm
ipvsadm-1.28-3ubuntu0.18.04.1.x86_64.rpm
java-common-0.68ubuntu1~18.04.1-1.noarch.rpm
javascript-common-11-1.noarch.rpm
kafkacat-1.3.1-1.x86_64.rpm
ksh-93u+20120801-3.1ubuntu1.x86_64.rpm
lftp-4.8.1-1ubuntu0.2.x86_64.rpm
libaacs0-0.9.0-1.x86_64.rpm
libaec0-0.3.2-2.x86_64.rpm
libaec-dev-0.3.2-2.x86_64.rpm
libalgorithm-diff-perl-1.19.03-1.noarch.rpm
libalgorithm-diff-xs-perl-0.04-5.x86_64.rpm
libalgorithm-merge-perl-0.08-3.noarch.rpm
libamd2-5.1.2-2.x86_64.rpm
libapr1-1.6.3-2.x86_64.rpm
libaprutil1-1.6.1-2.x86_64.rpm
libarchive-cpio-perl-0.10-1.noarch.rpm
libasan4-7.5.0-3ubuntu1~18.04.x86_64.rpm
libatomic1-8.4.0-1ubuntu1~18.04.x86_64.rpm
libaugeas0-1.10.1-2ubuntu1.x86_64.rpm
libavcodec57-3.4.11-0ubuntu0.1.x86_64.rpm
libavutil55-3.4.11-0ubuntu0.1.x86_64.rpm
libbdplus0-0.1.2-2.x86_64.rpm
libblas3-3.7.1-4ubuntu1.x86_64.rpm
libblas-dev-3.7.1-4ubuntu1.x86_64.rpm
libbluray2-1.0.2-3.x86_64.rpm
libboost-atomic1.65.1-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-atomic1.65-dev-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-chrono1.65.1-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-chrono1.65-dev-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-date-time1.65-dev-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-iostreams1.65-dev-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-iostreams-dev-1.65.1.0ubuntu1-1.x86_64.rpm
libboost-log1.65.1-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-program-options1.65.1-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-regex1.65.1-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-regex1.65-dev-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-serialization1.65.1-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-serialization1.65-dev-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-serialization-dev-1.65.1.0ubuntu1-1.x86_64.rpm
libboost-system1.65-dev-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-system-dev-1.65.1.0ubuntu1-1.x86_64.rpm
libboost-thread1.65-dev-1.65.1+dfsg-0ubuntu5.x86_64.rpm
libboost-thread-dev-1.65.1.0ubuntu1-1.x86_64.rpm
libbsd-dev-0.8.7-1ubuntu0.1.x86_64.rpm
libbtf1-5.1.2-2.x86_64.rpm
libc6-2.27-3ubuntu1.6.x86_64.rpm
libc6-dbg-2.27-3ubuntu1.6.x86_64.rpm
libc6-dev-2.27-3ubuntu1.6.x86_64.rpm
libcamd2-5.1.2-2.x86_64.rpm
libc-ares2-1.14.0-1ubuntu0.1.x86_64.rpm
libccolamd2-5.1.2-2.x86_64.rpm
libc-dev-bin-2.27-3ubuntu1.6.x86_64.rpm
libcilkrts5-7.5.0-3ubuntu1~18.04.x86_64.rpm
libclang1-6.0-6.0-1ubuntu2.x86_64.rpm
libcpp-hocon0.1.6-0.1.6-1.x86_64.rpm
libcrystalhd3-0.0~git20110715.fdd2f19-12.x86_64.rpm
libcurl4-7.58.0-2ubuntu3.21.x86_64.rpm
libcurl4-gnutls-dev-7.58.0-2ubuntu3.21.x86_64.rpm
libcxsparse3-5.1.2-2.x86_64.rpm
libdeal.ii-dev-8.5.1-3.x86_64.rpm
libdeal.ii-doc-8.5.1-3.noarch.rpm
libdiscid0-0.6.2-2.x86_64.rpm
libdrm-dev-2.4.101-2~18.04.1.x86_64.rpm
libenca0-1.19-1.x86_64.rpm
libfabric1-1.5.3-1.x86_64.rpm
libfacter3.10.0-3.10.0-4.x86_64.rpm
libfakeroot-1.22-2ubuntu1.x86_64.rpm
libfftw3-bin-3.3.7-1.x86_64.rpm
libfftw3-dev-3.3.7-1.x86_64.rpm
libfftw3-long3-3.3.7-1.x86_64.rpm
libfftw3-mpi3-3.3.7-1.x86_64.rpm
libfftw3-mpi-dev-3.3.7-1.x86_64.rpm
libfftw3-quad3-3.3.7-1.x86_64.rpm
libfile-stripnondeterminism-perl-0.040-1.1~build1.noarch.rpm
libfreeimage3-3.17.0+ds1-5+deb9u1build0.18.04.1.x86_64.rpm
libfreeimage-dev-3.17.0+ds1-5+deb9u1build0.18.04.1.x86_64.rpm
libgcc-7-dev-7.5.0-3ubuntu1~18.04.x86_64.rpm
libgfortran4-7.5.0-3ubuntu1~18.04.x86_64.rpm
libgfortran-7-dev-7.5.0-3ubuntu1~18.04.x86_64.rpm
libgl1-mesa-dev-20.0.8-0ubuntu1~18.04.1.x86_64.rpm
libgl2ps-dev-1.4.0+dfsg1-1.x86_64.rpm
libgles1-1.0.0-2ubuntu2.3.x86_64.rpm
libglib2.0-dev-2.56.4-0ubuntu0.18.04.9.x86_64.rpm
libglib2.0-dev-bin-2.56.4-0ubuntu0.18.04.9.x86_64.rpm
libglvnd-core-dev-1.0.0-2ubuntu2.3.x86_64.rpm
libglvnd-dev-1.0.0-2ubuntu2.3.x86_64.rpm
libgme0-0.6.2-1.x86_64.rpm
libgmp-dev-6.1.2+dfsg-2ubuntu0.1.x86_64.rpm
libgmpxx4ldbl-6.1.2+dfsg-2ubuntu0.1.x86_64.rpm
libgnat-6-6.5.0-2ubuntu1~18.04.x86_64.rpm
libgraphblas1-5.1.2-2.x86_64.rpm
libgraphite2-dev-1.3.11-2.x86_64.rpm
libgsl23-2.4+dfsg-6.x86_64.rpm
libgslcblas0-2.4+dfsg-6.x86_64.rpm
libgsl-dev-2.4+dfsg-6.x86_64.rpm
libgsm1-1.0.13-4build1.x86_64.rpm
libharfbuzz-dev-1.7.2-1ubuntu1.x86_64.rpm
libharfbuzz-gobject0-1.7.2-1ubuntu1.x86_64.rpm
libhawtjni-runtime-java-1.15-2.noarch.rpm
libhdf5-100-1.10.0-patch1+docs_4.x86_64.rpm
libhdf5-cpp-100-1.10.0-patch1+docs_4.x86_64.rpm
libhdf5-mpi-dev-1.10.0-patch1+docs_4.x86_64.rpm
libhdf5-openmpi-100-1.10.0-patch1+docs_4.x86_64.rpm
libhts2-1.7-2.x86_64.rpm
libhttp-parser2.7.1-2.7.1-2ubuntu0.1.x86_64.rpm
libhwloc5-1.11.9-1.x86_64.rpm
libhwloc-dev-1.11.9-1.x86_64.rpm
libiberty-dev-20170913-1ubuntu0.1.x86_64.rpm
libibverbs1-17.1-1ubuntu0.2.x86_64.rpm
libibverbs-dev-17.1-1ubuntu0.2.x86_64.rpm
libice-dev-1.0.9-2ubuntu0.18.04.1.x86_64.rpm
libicu-le-hb0-1.0.3+git161113-4.x86_64.rpm
libicu-le-hb-dev-1.0.3+git161113-4.x86_64.rpm
libiculx60-60.2-3ubuntu3.2.x86_64.rpm
libitm1-8.4.0-1ubuntu1~18.04.x86_64.rpm
libjansi-java-1.16-1.noarch.rpm
libjansi-native-java-1.7-1.noarch.rpm
libjline2-java-2.14.6-1.noarch.rpm
libjpeg8-dev-8c-2ubuntu8.x86_64.rpm
libjpeg-dev-8c-2ubuntu8.x86_64.rpm
libjpeg-turbo8-dev-1.5.2-0ubuntu5.18.04.6.x86_64.rpm
libjs-async-0.8.0-3.noarch.rpm
libjs-bowser-0.7.3-2.noarch.rpm
libjs-events-1.0.2-2.noarch.rpm
libjs-inherits-2.0.3-1.noarch.rpm
libjs-is-typedarray-1.0.0-2.noarch.rpm
libjs-jquery-3.2.1-1.noarch.rpm
libjs-jssip-0.6.34-5.noarch.rpm
libjs-jstimezonedetect-1.0.6-1.x86_64.rpm
libjs-merge-1.2.0-2.noarch.rpm
libjs-node-uuid-1.4.7-5.noarch.rpm
libjsoncpp1-1.7.4-3.x86_64.rpm
libjs-rtcninja-0.6.2-2.noarch.rpm
libjs-sdp-transform-1.4.0-2.noarch.rpm
libjs-typedarray-to-buffer-3.0.3-3.noarch.rpm
libjs-underscore-1.8.3~dfsg-1ubuntu0.1.noarch.rpm
libjs-util-0.10.3-2.noarch.rpm
libjs-websocket-1.0.23-3build2.noarch.rpm
libjxr0-1.1-6build1.x86_64.rpm
libklu1-5.1.2-2.x86_64.rpm
libldl2-5.1.2-2.x86_64.rpm
libleatherman1.4.0-1.4.0+dfsg-1.x86_64.rpm
libleatherman-data-1.4.0+dfsg-1.noarch.rpm
liblsan0-8.4.0-1ubuntu1~18.04.x86_64.rpm
libltdl-dev-2.4.6-2.x86_64.rpm
liblua5.2-0-5.2.4-1.1build1.x86_64.rpm
libmail-sendmail-perl-0.80-1.noarch.rpm
libmetis5-5.1.0.dfsg-5.x86_64.rpm
libmng2-2.0.2-0ubuntu3.x86_64.rpm
libmpx2-8.4.0-1ubuntu1~18.04.x86_64.rpm
libmumps-dev-5.1.2-4.x86_64.rpm
libmunge2-0.5.13-1.x86_64.rpm
libmuparser2v5-2.2.3-6.x86_64.rpm
libmuparser-dev-2.2.3-6.x86_64.rpm
libmysqlclient20-5.7.40-0ubuntu0.18.04.1.x86_64.rpm
libnetcdf13-4.6.0-2build1.x86_64.rpm
libnetcdf-c++4-4.2-8.x86_64.rpm
libnetcdf-cxx-legacy-dev-4.2-8.x86_64.rpm
libnginx-mod-http-geoip-1.14.0-0ubuntu1.11.x86_64.rpm
libnginx-mod-http-image-filter-1.14.0-0ubuntu1.11.x86_64.rpm
libnginx-mod-http-xslt-filter-1.14.0-0ubuntu1.11.x86_64.rpm
libnginx-mod-mail-1.14.0-0ubuntu1.11.x86_64.rpm
libnginx-mod-stream-1.14.0-0ubuntu1.11.x86_64.rpm
libnl-route-3-200-3.2.29-0ubuntu3.x86_64.rpm
liboce-foundation11-0.18.2-2build1.x86_64.rpm
liboce-foundation-dev-0.18.2-2build1.x86_64.rpm
liboce-modeling11-0.18.2-2build1.x86_64.rpm
liboce-modeling-dev-0.18.2-2build1.x86_64.rpm
liboce-ocaf11-0.18.2-2build1.x86_64.rpm
liboce-ocaf-dev-0.18.2-2build1.x86_64.rpm
liboce-ocaf-lite11-0.18.2-2build1.x86_64.rpm
liboce-ocaf-lite-dev-0.18.2-2build1.x86_64.rpm
libopengl0-1.0.0-2ubuntu2.3.x86_64.rpm
libopenjp2-7-2.3.0-2build0.18.04.1.x86_64.rpm
libopenmpi2-2.1.1-8.x86_64.rpm
libopenmpi-dev-2.1.1-8.x86_64.rpm
libopenmpt0-0.3.6-1.x86_64.rpm
libossp-uuid16-1.6.2-1.5build4.x86_64.rpm
libp4est-1.1-1.1-5.x86_64.rpm
libp4est-dev-1.1-5.x86_64.rpm
libpcre16-3-8.39-9ubuntu0.1.x86_64.rpm
libpcre32-3-8.39-9ubuntu0.1.x86_64.rpm
libpcre3-dev-8.39-9ubuntu0.1.x86_64.rpm
libpcrecpp0v5-8.39-9ubuntu0.1.x86_64.rpm
libpetsc3.7.7-dev-3.7.7+dfsg1-2build5.x86_64.rpm
libpetsc3.7-dev-3.7.7+dfsg1-2build5.x86_64.rpm
libpng-dev-1.6.34-1ubuntu0.18.04.2.x86_64.rpm
libpng-tools-1.6.34-1ubuntu0.18.04.2.x86_64.rpm
libpsm-infinipath1-3.3+20.604758e7-5.x86_64.rpm
libpthread-stubs0-dev-0.3-4.x86_64.rpm
libptscotch-6.0-6.0.4.dfsg1-8.x86_64.rpm
libptscotch-dev-6.0.4.dfsg1-8.x86_64.rpm
libpython-stdlib-2.7.15~rc1-1.x86_64.rpm
libqt4-dbus-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-declarative-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-designer-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-help-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-network-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-script-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-scripttools-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-sql-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-sql-mysql-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-svg-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-test-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-xml-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqt4-xmlpatterns-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqtassistantclient4-4.6.3-7build1.x86_64.rpm
libqtcore4-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqtdbus4-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libqtgui4-4.8.7+dfsg-7ubuntu1.x86_64.rpm
libquadmath0-8.4.0-1ubuntu1~18.04.x86_64.rpm
librbio2-5.1.2-2.x86_64.rpm
librdkafka1-0.11.3-1build1.x86_64.rpm
librdmacm1-17.1-1ubuntu0.2.x86_64.rpm
librecode0-3.6-23.x86_64.rpm
librhash0-1.3.6-2.x86_64.rpm
librpm8-4.14.1+dfsg1-2.x86_64.rpm
librpmbuild8-4.14.1+dfsg1-2.x86_64.rpm
librpmio8-4.14.1+dfsg1-2.x86_64.rpm
librpmsign8-4.14.1+dfsg1-2.x86_64.rpm
libruby2.5-2.5.1-1ubuntu1.12.x86_64.rpm
libscalapack-mpi-dev-2.0.2-4.x86_64.rpm
libscalapack-openmpi-dev-2.0.2-4.x86_64.rpm
libscotch-6.0-6.0.4.dfsg1-8.x86_64.rpm
libscotch-dev-6.0.4.dfsg1-8.x86_64.rpm
libserf-1-1-1.3.9-6.x86_64.rpm
libshine3-3.1.1-1.x86_64.rpm
libsigsegv2-2.12-1.x86_64.rpm
libslepc3.7.4-dev-3.7.4+dfsg1-2build8.x86_64.rpm
libslepc3.7-dev-3.7.4+dfsg1-2build8.x86_64.rpm
libsm-dev-1.2.2-1.x86_64.rpm
libsnappy1v5-1.1.7-1.x86_64.rpm
libsoxr0-0.1.2-3.x86_64.rpm
libspooles2.2-2.2-12build1.x86_64.rpm
libspooles-dev-2.2-12build1.x86_64.rpm
libssh-gcrypt-4-0.8.0~20170825.94fa1e38-1ubuntu0.7.x86_64.rpm
libssl1.0-dev-1.0.2n-1ubuntu5.10.x86_64.rpm
libssl-dev-1.1.1-1ubuntu2.1~18.04.20.x86_64.rpm
libstdc++-7-dev-7.5.0-3ubuntu1~18.04.x86_64.rpm
libsuperlu-dev-5.2.1+dfsg1-3.x86_64.rpm
libsvn1-1.9.7-4ubuntu1.1.x86_64.rpm
libswresample2-3.4.11-0ubuntu0.1.x86_64.rpm
libsys-hostname-long-perl-1.5-1.noarch.rpm
libsz2-0.3.2-2.x86_64.rpm
libtbb2-2017~U7-8.x86_64.rpm
libtbb-dev-2017~U7-8.x86_64.rpm
libtinfo-dev-6.1-1ubuntu1.18.04.x86_64.rpm
libtrilinos-amesos12-12.12.1-5.x86_64.rpm
libtrilinos-amesos2-12-12.12.1-5.x86_64.rpm
libtrilinos-amesos2-dev-12.12.1-5.x86_64.rpm
libtrilinos-amesos-dev-12.12.1-5.x86_64.rpm
libtrilinos-anasazi12-12.12.1-5.x86_64.rpm
libtrilinos-anasazi-dev-12.12.1-5.x86_64.rpm
libtrilinos-aztecoo-dev-12.12.1-5.x86_64.rpm
libtrilinos-belos12-12.12.1-5.x86_64.rpm
libtrilinos-belos-dev-12.12.1-5.x86_64.rpm
libtrilinos-epetra-dev-12.12.1-5.x86_64.rpm
libtrilinos-epetraext12-12.12.1-5.x86_64.rpm
libtrilinos-epetraext-dev-12.12.1-5.x86_64.rpm
libtrilinos-galeri12-12.12.1-5.x86_64.rpm
libtrilinos-galeri-dev-12.12.1-5.x86_64.rpm
libtrilinos-globipack12-12.12.1-5.x86_64.rpm
libtrilinos-globipack-dev-12.12.1-5.x86_64.rpm
libtrilinos-ifpack12-12.12.1-5.x86_64.rpm
libtrilinos-ifpack2-12-12.12.1-5.x86_64.rpm
libtrilinos-ifpack2-dev-12.12.1-5.x86_64.rpm
libtrilinos-ifpack-dev-12.12.1-5.x86_64.rpm
libtrilinos-intrepid12-12.12.1-5.x86_64.rpm
libtrilinos-intrepid-dev-12.12.1-5.x86_64.rpm
libtrilinos-isorropia12-12.12.1-5.x86_64.rpm
libtrilinos-isorropia-dev-12.12.1-5.x86_64.rpm
libtrilinos-kokkos12-12.12.1-5.x86_64.rpm
libtrilinos-kokkos-dev-12.12.1-5.x86_64.rpm
libtrilinos-kokkos-kernels12-12.12.1-5.x86_64.rpm
libtrilinos-kokkos-kernels-dev-12.12.1-5.x86_64.rpm
libtrilinos-komplex12-12.12.1-5.x86_64.rpm
libtrilinos-komplex-dev-12.12.1-5.x86_64.rpm
libtrilinos-ml-dev-12.12.1-5.x86_64.rpm
libtrilinos-moertel12-12.12.1-5.x86_64.rpm
libtrilinos-moertel-dev-12.12.1-5.x86_64.rpm
libtrilinos-muelu12-12.12.1-5.x86_64.rpm
libtrilinos-muelu-dev-12.12.1-5.x86_64.rpm
libtrilinos-nox-dev-12.12.1-5.x86_64.rpm
libtrilinos-optipack12-12.12.1-5.x86_64.rpm
libtrilinos-optipack-dev-12.12.1-5.x86_64.rpm
libtrilinos-pamgen12-12.12.1-5.x86_64.rpm
libtrilinos-pamgen-dev-12.12.1-5.x86_64.rpm
libtrilinos-phalanx12-12.12.1-5.x86_64.rpm
libtrilinos-phalanx-dev-12.12.1-5.x86_64.rpm
libtrilinos-pike12-12.12.1-5.x86_64.rpm
libtrilinos-pike-dev-12.12.1-5.x86_64.rpm
libtrilinos-piro-dev-12.12.1-5.x86_64.rpm
libtrilinos-pliris-dev-12.12.1-5.x86_64.rpm
libtrilinos-rol12-12.12.1-5.x86_64.rpm
libtrilinos-rol-dev-12.12.1-5.x86_64.rpm
libtrilinos-rtop12-12.12.1-5.x86_64.rpm
libtrilinos-rtop-dev-12.12.1-5.x86_64.rpm
libtrilinos-rythmos12-12.12.1-5.x86_64.rpm
libtrilinos-rythmos-dev-12.12.1-5.x86_64.rpm
libtrilinos-sacado12-12.12.1-5.x86_64.rpm
libtrilinos-sacado-dev-12.12.1-5.x86_64.rpm
libtrilinos-shards12-12.12.1-5.x86_64.rpm
libtrilinos-shards-dev-12.12.1-5.x86_64.rpm
libtrilinos-shylu12-12.12.1-5.x86_64.rpm
libtrilinos-shylu-dev-12.12.1-5.x86_64.rpm
libtrilinos-stokhos12-12.12.1-5.x86_64.rpm
libtrilinos-stokhos-dev-12.12.1-5.x86_64.rpm
libtrilinos-stratimikos12-12.12.1-5.x86_64.rpm
libtrilinos-stratimikos-dev-12.12.1-5.x86_64.rpm
libtrilinos-teko12-12.12.1-5.x86_64.rpm
libtrilinos-teko-dev-12.12.1-5.x86_64.rpm
libtrilinos-teuchos-dev-12.12.1-5.x86_64.rpm
libtrilinos-thyra12-12.12.1-5.x86_64.rpm
libtrilinos-thyra-dev-12.12.1-5.x86_64.rpm
libtrilinos-tpetra-dev-12.12.1-5.x86_64.rpm
libtrilinos-trilinoscouplings-dev-12.12.1-5.x86_64.rpm
libtrilinos-trilinosss12-12.12.1-5.x86_64.rpm
libtrilinos-trilinosss-dev-12.12.1-5.x86_64.rpm
libtrilinos-triutils12-12.12.1-5.x86_64.rpm
libtrilinos-triutils-dev-12.12.1-5.x86_64.rpm
libtrilinos-xpetra12-12.12.1-5.x86_64.rpm
libtrilinos-xpetra-dev-12.12.1-5.x86_64.rpm
libtrilinos-zoltan12-12.12.1-5.x86_64.rpm
libtrilinos-zoltan2-12-12.12.1-5.x86_64.rpm
libtrilinos-zoltan2-dev-12.12.1-5.x86_64.rpm
libtrilinos-zoltan-dev-12.12.1-5.x86_64.rpm
libtsan0-8.4.0-1ubuntu1~18.04.x86_64.rpm
libubsan0-7.5.0-3ubuntu1~18.04.x86_64.rpm
libuv1-1.18.0-3.x86_64.rpm
libuv1-dev-1.18.0-3.x86_64.rpm
libva2-2.1.0-3.x86_64.rpm
libva-drm2-2.1.0-3.x86_64.rpm
libvarnishapi1-5.2.1-1ubuntu0.1.x86_64.rpm
libva-x11-2-2.1.0-3.x86_64.rpm
libvdpau1-1.1.1-3ubuntu1.x86_64.rpm
libx11-dev-1.6.4-3ubuntu0.4.x86_64.rpm
libx11-doc-1.6.4-3ubuntu0.4.noarch.rpm
libx11-xcb-dev-1.6.4-3ubuntu0.4.x86_64.rpm
libx264-152-0.152.2854+gite9a5903-2.x86_64.rpm
libx265-146-2.6-3.x86_64.rpm
libxau-dev-1.0.8-1ubuntu1.x86_64.rpm
libxcb1-dev-1.13-2~ubuntu18.04.x86_64.rpm
libxcb-dri2-0-dev-1.13-2~ubuntu18.04.x86_64.rpm
libxcb-dri3-dev-1.13-2~ubuntu18.04.x86_64.rpm
libxcb-glx0-dev-1.13-2~ubuntu18.04.x86_64.rpm
libxcb-present-dev-1.13-2~ubuntu18.04.x86_64.rpm
libxcb-randr0-dev-1.13-2~ubuntu18.04.x86_64.rpm
libxcb-render0-dev-1.13-2~ubuntu18.04.x86_64.rpm
libxcb-shape0-dev-1.13-2~ubuntu18.04.x86_64.rpm
libxcb-sync-dev-1.13-2~ubuntu18.04.x86_64.rpm
libxcb-xfixes0-dev-1.13-2~ubuntu18.04.x86_64.rpm
libxdamage-dev-1.1.4-3.x86_64.rpm
libxdmcp-dev-1.1.2-3.x86_64.rpm
libxext-dev-1.3.3-1.x86_64.rpm
libxfixes-dev-5.0.3-1.x86_64.rpm
libxmu-dev-1.1.2-2.x86_64.rpm
libxmu-headers-1.1.2-2.noarch.rpm
libxshmfence-dev-1.3-1.x86_64.rpm
libxt-dev-1.1.5-1.x86_64.rpm
libxvidcore4-1.3.5-1.x86_64.rpm
libxxf86vm-dev-1.1.4-1.x86_64.rpm
libyaml-cpp0.5v5-0.5.2-4ubuntu1.x86_64.rpm
libzvbi0-0.2.35-13.x86_64.rpm
libzvbi-common-0.2.35-13.noarch.rpm
linux-libc-dev-4.15.0-200.211.x86_64.rpm
lynx-2.8.9dev16-3.x86_64.rpm
lynx-common-2.8.9dev16-3.noarch.rpm
lzip-1.20-1.x86_64.rpm
lzop-1.03-4.x86_64.rpm
m4-1.4.18-1.x86_64.rpm
make-4.1-9.1ubuntu1.x86_64.rpm
manpages-dev-4.15-1.noarch.rpm
memcached-1.5.6-0ubuntu1.2.x86_64.rpm
menu-2.1.47ubuntu2.1-1.x86_64.rpm
mesa-common-dev-20.0.8-0ubuntu1~18.04.1.x86_64.rpm
mesa-va-drivers-20.0.8-0ubuntu1~18.04.1.x86_64.rpm
mesa-vdpau-drivers-20.0.8-0ubuntu1~18.04.1.x86_64.rpm
mpi-default-bin-1.10-1.x86_64.rpm
mpi-default-dev-1.10-1.x86_64.rpm
munge-0.5.13-1.x86_64.rpm
nginx-core-1.14.0-0ubuntu1.11.x86_64.rpm
nmon-16g+debian-3.x86_64.rpm
node-abbrev-1.0.9-1.noarch.rpm
node-ansi-0.3.0-2ubuntu1.noarch.rpm
node-ansi-color-table-1.0.0-1.noarch.rpm
node-archy-1.0.0-1ubuntu1.noarch.rpm
node-argparse-1.0.9-1.noarch.rpm
node-assert-plus-1.0.0-1.noarch.rpm
node-async-0.8.0-3.noarch.rpm
node-balanced-match-0.4.2-1.noarch.rpm
node-block-stream-0.0.9-1ubuntu1.noarch.rpm
node-bowser-0.7.3-2.noarch.rpm
node-brace-expansion-1.1.8-1.noarch.rpm
node-builtin-modules-1.1.1-1.noarch.rpm
node-combined-stream-0.0.5-1.noarch.rpm
node-concat-map-0.0.1-1.noarch.rpm
node-config-chain-1.1.11-1.noarch.rpm
node-cookie-jar-0.3.1-1.noarch.rpm
node-core-js-2.4.1-2.noarch.rpm
node-core-util-is-1.0.2-1.noarch.rpm
node-debug-3.1.0-1.noarch.rpm
node-delayed-stream-0.0.5-1.noarch.rpm
node-es6-promise-4.2.4-1.noarch.rpm
node-esprima-4.0.0+ds-2.noarch.rpm
node-events-1.0.2-2.noarch.rpm
node-extsprintf-1.3.0-1.noarch.rpm
node-forever-agent-0.5.1-1.noarch.rpm
node-form-data-0.1.0-1.noarch.rpm
node-fs.realpath-1.0.0-1.noarch.rpm
node-fstream-1.0.10-1ubuntu0.18.04.1.noarch.rpm
node-fstream-ignore-0.0.6-2.noarch.rpm
node-github-url-from-git-1.4.0-1.noarch.rpm
node-glob-7.1.2-4.noarch.rpm
node-graceful-fs-4.1.11-1.noarch.rpm
node-gyp-3.6.2-1ubuntu1.noarch.rpm
node-hosted-git-info-2.5.0-1.noarch.rpm
node-immediate-3.2.3+dfsg-1.noarch.rpm
node-inflight-1.0.6-1.noarch.rpm
node-inherits-2.0.3-1.noarch.rpm
node-ini-1.3.4-1.noarch.rpm
node-is-builtin-module-1.0.0-1.noarch.rpm
node-isexe-2.0.0-3.noarch.rpm
node-is-typedarray-1.0.0-2.noarch.rpm
node-jju-1.1.0-1.noarch.rpm
nodejs-8.10.0~dfsg-2ubuntu0.4.x86_64.rpm
node-js-beautify-1.7.5+dfsg-1.noarch.rpm
node-jsbn-1.1.0-1.noarch.rpm
node-jschardet-1.6.0+dfsg-1.noarch.rpm
node-js-cookie-2.2.0-1.noarch.rpm
nodejs-dev-8.10.0~dfsg-2ubuntu0.4.x86_64.rpm
nodejs-doc-8.10.0~dfsg-2ubuntu0.4.noarch.rpm
node-jsesc-2.5.1-1.noarch.rpm
node-json2module-0.0.3-1.noarch.rpm
node-json3-3.3.2-1.noarch.rpm
node-json5-0.5.1-1.noarch.rpm
node-json-buffer-3.0.0-1.noarch.rpm
node-jsonfile-4.0.0-1.noarch.rpm
node-jsonify-0.0.0-1.noarch.rpm
node-json-loader-0.5.4-1.noarch.rpm
node-json-localizer-0.0.3-1.noarch.rpm
node-jsonminify-0.4.1+dfsg1-1.noarch.rpm
node-jsonparse-1.3.1-3.noarch.rpm
node-json-parse-better-errors-1.0.1-1.noarch.rpm
node-json-parse-helpfulerror-1.0.3-2.noarch.rpm
node-json-schema-0.2.3-1.noarch.rpm
node-json-schema-traverse-0.3.1-1.noarch.rpm
node-jsonselect-0.4.0+dfsg3-1.noarch.rpm
node-json-stable-stringify-1.0.1-1.noarch.rpm
node-jsonstream-1.3.1-1.noarch.rpm
node-json-stringify-safe-5.0.0-1.noarch.rpm
node-jsprim-1.4.0-1.noarch.rpm
node-jssip-0.6.34-5.noarch.rpm
node-jstimezonedetect-1.0.6-1.x86_64.rpm
node-js-tokens-2.0.0-1.noarch.rpm
node-jsv-4.0.0+ds1-1.noarch.rpm
node-js-yaml-3.10.0+dfsg-1.noarch.rpm
node-jszip-3.1.4+dfsg-1.noarch.rpm
node-jszip-utils-0.0.2+dfsg-1.noarch.rpm
node-lie-3.1.1+dfsg-1.noarch.rpm
node-lockfile-0.4.1-1.noarch.rpm
node-lru-cache-4.1.1-1.noarch.rpm
node-merge-1.2.0-2.noarch.rpm
node-mime-1.3.4-1.noarch.rpm
node-minimatch-3.0.4-3.noarch.rpm
node-mkdirp-0.5.1-1.noarch.rpm
node-ms-2.1.1-1.noarch.rpm
node-mute-stream-0.0.7-1.noarch.rpm
node-nan-2.9.2-1.noarch.rpm
node-node-uuid-1.4.7-5.noarch.rpm
node-nopt-3.0.6-3.noarch.rpm
node-normalize-package-data-2.3.5-2.noarch.rpm
node-npmlog-0.0.4-1.noarch.rpm
node-once-1.4.0-2ubuntu1.noarch.rpm
node-osenv-0.1.4-1.noarch.rpm
node-pako-1.0.6+ds-1.noarch.rpm
node-path-is-absolute-1.0.0-1.noarch.rpm
node-proto-list-1.2.4-1.noarch.rpm
node-pseudomap-1.0.2-1.noarch.rpm
node-qs-2.2.4-1ubuntu1.noarch.rpm
node-read-1.0.7-1.noarch.rpm
node-read-package-json-1.2.4-1.noarch.rpm
node-request-2.26.1-1.noarch.rpm
node-retry-0.10.1-1.noarch.rpm
node-rimraf-2.6.2-1.noarch.rpm
node-rtcninja-0.6.2-2.noarch.rpm
node-rw-1.3.3-1.noarch.rpm
node-sdp-transform-1.4.0-2.noarch.rpm
node-semver-5.4.1-1.noarch.rpm
node-sha-1.2.3-1.noarch.rpm
node-slide-1.1.6-1.noarch.rpm
node-spdx-correct-1.0.2-1.noarch.rpm
node-spdx-expression-parse-1.0.4-1.noarch.rpm
node-spdx-license-ids-1.2.2-1.noarch.rpm
node-sprintf-js-1.1.1+ds1-2.noarch.rpm
node-tar-2.2.1-1.noarch.rpm
node-through-2.3.8-1.noarch.rpm
node-tunnel-agent-0.3.1-1.noarch.rpm
node-typedarray-to-buffer-3.0.3-3.noarch.rpm
node-underscore-1.8.3~dfsg-1ubuntu0.1.noarch.rpm
node-util-0.10.3-2.noarch.rpm
node-validate-npm-package-license-3.0.1-1.noarch.rpm
node-verror-1.10.0-1.noarch.rpm
node-websocket-1.0.23-3build2.x86_64.rpm
node-which-1.3.0-1.noarch.rpm
node-wrappy-1.0.2-1.noarch.rpm
node-yallist-2.0.0-1.noarch.rpm
npm-3.5.2-0ubuntu4.noarch.rpm
ocl-icd-libopencl1-2.2.11-1ubuntu1.x86_64.rpm
openjdk-11-jre-headless-11.0.17+8-1ubuntu2~18.04.x86_64.rpm
openmpi-bin-2.1.1-8.x86_64.rpm
openmpi-common-2.1.1-8.noarch.rpm
p7zip-16.02+dfsg-6.x86_64.rpm
petsc-dev-3.7.7+dfsg1-2build5.noarch.rpm
picard-1.4.2-1.x86_64.rpm
pigz-2.4-1.x86_64.rpm
pipexec-2.5.5-1.x86_64.rpm
pkg-config-0.29.1-0ubuntu2.x86_64.rpm
plink-1.07+dfsg-1.x86_64.rpm
po-debconf-1.0.20-1.noarch.rpm
python-2.7.15~rc1-1.x86_64.rpm
python2.7-2.7.17-1~18.04ubuntu1.10.x86_64.rpm
python2.7-minimal-2.7.17-1~18.04ubuntu1.10.x86_64.rpm
python3-distutils-3.6.9-1~18.04.noarch.rpm
python3-lib2to3-3.6.9-1~18.04.noarch.rpm
python-configobj-5.0.6-2.noarch.rpm
python-diamond-4.0.515-4ubuntu1.noarch.rpm
python-libdiscid-1.0-1build3.x86_64.rpm
python-meld3-1.0.2-2.noarch.rpm
python-minimal-2.7.15~rc1-1.x86_64.rpm
python-mutagen-1.38-1.noarch.rpm
python-pkg-resources-39.0.1-2.noarch.rpm
python-qt4-4.12.1+dfsg-2.x86_64.rpm
python-sip-4.19.7+dfsg-1ubuntu0.1.x86_64.rpm
python-six-1.11.0-2.noarch.rpm
qperf-0.4.10-1.x86_64.rpm
qt-at-spi-0.4.0-8.x86_64.rpm
qtchooser-64-ga1b6736_5.x86_64.rpm
qtcore4-l10n-4.8.7+dfsg-7ubuntu1.noarch.rpm
redis-4.0.9-1ubuntu0.2.noarch.rpm
redis-server-4.0.9-1ubuntu0.2.x86_64.rpm
redis-tools-4.0.9-1ubuntu0.2.x86_64.rpm
rpm2cpio-4.14.1+dfsg1-2.x86_64.rpm
rpm-4.14.1+dfsg1-2.x86_64.rpm
rpm-common-4.14.1+dfsg1-2.x86_64.rpm
ruby-2.5.1-1.x86_64.rpm
ruby2.5-2.5.1-1ubuntu1.12.x86_64.rpm
ruby2.5-dev-2.5.1-1ubuntu1.12.x86_64.rpm
ruby2.5-doc-2.5.1-1ubuntu1.12.noarch.rpm
ruby-augeas-0.5.0-3build6.x86_64.rpm
ruby-dev-2.5.1-1.x86_64.rpm
ruby-did-you-mean-1.2.0-2.noarch.rpm
rubygems-integration-1.11-1.noarch.rpm
ruby-json-2.1.0+dfsg-2.x86_64.rpm
ruby-minitest-5.10.3-1.noarch.rpm
ruby-net-telnet-0.1.1-2.noarch.rpm
ruby-power-assert-0.3.0-1.noarch.rpm
ruby-selinux-2.7-2build2.x86_64.rpm
ruby-shadow-2.5.0-1build1.x86_64.rpm
scala-library-2.11.12-4~18.04.noarch.rpm
scala-parser-combinators-1.0.3-3.noarch.rpm
scala-xml-1.0.3-3.noarch.rpm
shc-3.8.9b-1build1.x86_64.rpm
slepc-dev-3.7.4+dfsg1-2build8.x86_64.rpm
slurm-0.4.3-2build2.x86_64.rpm
spark-2012.0.deb-11build1.x86_64.rpm
subversion-1.9.7-4ubuntu1.1.x86_64.rpm
supervisor-3.3.1-1.1.noarch.rpm
swi-prolog-nox-7.6.4+dfsg-1build1.x86_64.rpm
tcsh-6.20.00-7.x86_64.rpm
trilinos-all-dev-12.12.1-5.x86_64.rpm
trilinos-dev-12.12.1-5.x86_64.rpm
vdpau-driver-all-1.1.1-3ubuntu1.x86_64.rpm
x11proto-core-dev-2018.4-4.noarch.rpm
x11proto-damage-dev-2018.4-4.noarch.rpm
x11proto-dev-2018.4-4.noarch.rpm
x11proto-fixes-dev-2018.4-4.noarch.rpm
x11proto-xext-dev-2018.4-4.noarch.rpm
x11proto-xf86vidmode-dev-2018.4-4.noarch.rpm
xorg-sgml-doctools-1.11-1.noarch.rpm
xtrans-dev-1.3.5-1.noarch.rpm
```



## 转换失败的软件包

```bash
```

