import os
import sys
import re

from typing import List

all_commands = [
    "debian/rules build",
    "dh_testroot",
    "dh_prep",
    "dh_installdirs",
    "dh_auto_install",
    "dh_install",
    "dh_installdocs",
    "dh_installchangelogs",
    "dh_installexamples",
    "dh_installman",
    "dh_installcatalogs",
    "dh_installcron",
    "dh_installdebconf",
    "dh_installemacsen",
    "dh_installifupdown",
    "dh_installinfo",
    "dh_installinit",
    "dh_isntallsystemd",
    "dh_installmenu",
    "dh_installmime",
    "dh_installmodules",
    "dh_installlogcheck",
    "dh_installlogrotate",
    "dh_installpam",
    "dh_installppp",
    "dh_installudev",
    "dh_installwm",
    "dh_installxfonts",
    "dh_bugfiles",
    "dh_lintian",
    # "dh_gconf",
    "dh_icons",
    "dh_systemduser"
    "dh_perl",
    "dh_usrlocal",
    "dh_link",
    "dh_compress",
    "dh_fixperms",
    "dh_missing",
    "dh_dwz",
    "dh_strip",
#     "dh_makeshlibs",
#     "dh_shlibdeps",
#     "dh_installdeb",
#     "dh_gencontrol",
#     "dh_md5sums",
#     "dh_builddeb",
]

class DebFiles:

    def __init__(self, path: str) -> None:
        """
        @param path: deb源码包根目录
        在path目录下执行操作获取信息
        """
        self.root_path = path
        self.rules_targets = []
        self.files = {}
        self.commands = all_commands
        # self.all_params = ""

        os.chdir(path)
        self._get_rules_targets()
        # print(self.rules_targets)
        self._refresh_commands()
        # self._exe_commands()
        self._get_packages()
        self._get_all_files()


    def _get_rules_targets(self) -> None:
        """
        解析debian/rules文件，将所有target存入self.rules_targets
        并获取dh $@后的通用参数
        """
        pattern = r'(.*?):[^=](.*)'
        pattern2 = r'dh\s+\$@\s+(.*)'
        with open("debian/rules", 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue
                match = re.search(pattern, line)
                if match:
                    self.rules_targets.append(match.group(1).strip())

                # match2 = re.search(pattern2, line)
                # if match2 and match2.group(1).strip() != None:
                #     self.all_params = match2.group(1).strip()
                
    def _refresh_commands(self) -> None:
        """
        根据rules文件中的target，修改commands的内容
        """
        to_be_changed = {}
        for c in all_commands:
            to_be_changed[c] = []

        # 获取override字段
        pattern1 = r'override_(.*)'
        pattern2 = r'(.*?)(?:-indep|-arch)'
        for target in self.rules_targets:
            match = re.search(pattern1, target)
            if match:
                match2 = re.search(pattern2, match.group(1).strip())
                if match.group(1).strip() in all_commands:
                    to_be_changed[match.group(1).strip()].append(f"debian/rules {target}")
                elif match2 and match2.group(1).strip() in all_commands:
                    to_be_changed[match2.group(1).strip()].append(f"debian/rules {target}") 
        
        # 更新命令
        for key, value_list in to_be_changed.items():
            if len(value_list) != 0:
                i = self.commands.index(key)
                self.commands = self.commands[:i] + value_list + self.commands[i+1:]
        # print(self.commands)
        # 有关清理任务
        if "override_dh_auto_clean" in self.rules_targets:
            self.commands.insert(0, "debian/rules override_dh_auto_clean")
        else:
            self.commands.insert(0, "debian/rules clean")

    def _exe_commands(self) -> None:
        for command in self.commands:
            # if command in all_commands:
            #     print(f"执行命令 fakeroot {command} {self.all_params}")
            #     os.system("fakeroot " + command + " " + self.all_params)
            # else:
            print(f"执行命令 fakeroot {command}")
            os.system("fakeroot " + command)
                
    def _get_packages(self) -> None:
        """
        从debian/control文件中获取所有子包名
        """
        pattern = r'Package:\s+(.*)'
        with open("debian/control", 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue
                match = re.search(pattern, line)
                if match:
                    self.files[match.group(1).strip()] = []
                    print(match.group(1).strip())

    def _get_all_files(self) -> None:
        """
        将子包所有的文件添加到files字典中
        """
        for p in self.files.keys():
            path = os.path.join(self.root_path, "debian", p)
            self.files[p] = self._get_all_files_under_dir(path)
        # print(self.files)
        for pac, files_list in self.files.items():
            print(f"{pac}: {len(files_list)}个文件")

    def _get_all_files_under_dir(self, path: str) -> List:
        """
        @param path   目标文件夹
        @return 目标文件夹下所有文件的列表
        """
        all_files = []
        for root, subdirs, files in os.walk(path):
            for file in files:
                abs_path = os.path.join(root, file)
                all_files.append(os.path.relpath(abs_path, path))

        return all_files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Provide one directory!")
        sys.exit()

    root_dir = os.getcwd()
    package_dir = os.path.join(root_dir, sys.argv[1])
    all_subdir = [os.path.join(package_dir, x) for x in os.listdir(package_dir)
                  if os.path.isdir(os.path.join(package_dir, x))]

    if len(all_subdir) == 1:
        DebFiles(all_subdir[0])
    # os.chdir("dh-python/dh-python-5.20220403")
    # os.system("fakeroot debian/rules clean")
    # os.system("fakeroot debian/rules build")
