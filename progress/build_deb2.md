首先尝试在openEuler环境中打出简单的`deb`包，考虑到要使依赖尽可能的少，我选择先打出`dh-di`包。根据其control文件的说明，这个包只有`debhelper`和`dh-perl`的依赖。
```bash
// 获取源码包
wget https://repo.huaweicloud.com/ubuntu/pool/main/d/dh-di/dh-di_11.dsc
wget https://repo.huaweicloud.com/ubuntu/pool/main/d/dh-di/dh-di_11.tar.xz

// 解压出源码
tar -xJf dh-di_11.tar.xz

// build
cd dh-di-11
fakeroot debian/rules build

// 打包
fakeroot debian/rules binary
```
打包过程中出现了以下错误：
```bash
Can't exec "dh_strip_nondeterminism": No such file or directory at /usr/share/perl5/vendor_perl/Debian/Debhelper/SequencerUtil.pm line 490
make: *** [debian/rules:3: binary] Error 255
```

通过查询资料，我在[https://github.com/scylladb/scylladb/commit/5bf9a03d65dea12ae63bb32c28fa611594d7e9ff](https://github.com/scylladb/scylladb/commit/5bf9a03d65dea12ae63bb32c28fa611594d7e9ff)发现了这个问题的原因和解决方法：
> dist/debian: skip running dh_strip_nondeterminism
On some Fedora environment dh build tries to run
dh_strip_nondeterminism, and fails sice Fedora does not provide such command.

只需如下修改`rules`文件:
```diff
+ override_dh_strip_nondeterminism:
+
%:
	dh $@
```

随后再次执行`fakeroot debian/rules binary`，成功打出deb包。