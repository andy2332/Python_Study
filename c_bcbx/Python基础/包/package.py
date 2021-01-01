# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/12 22:23

# 包（Package）
# 当我们代码量进一步变大时，光拆分成多个文件已经不足以满足需求，
# 还需要能按照一定的目录结构层次化的组织这些模块，同时包也可以解决模块之间的名字冲突问题。

# 例如，我们可以以下面的方式组织代码结构：
# test.py
# bao_package/
#       add.py
#       divide.py
#       __init__.py
# 在bao_package目录中增加一个__init__.py文件，bao_package这个目录就成了包。
# 可以在test.py中import bao_package中的模块

from c_bcbx.Python基础.包.bao_package import add, divide

# 调用add.py文件
add
# 调用divide.py文件
divide

# __init__.py 是在包加载的时候会进行执行，负责一些包的初始化操作，一般是空文件即可。
