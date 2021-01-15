# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/7 18:13

# 列表和元组类似于C语言中的数组，使用[]来表示列表，用()来表示元组。
# 对象有序排列，通过索引读取，下标从0开始，最后一个下标为-1。
# 能保存任意数量、任意类型的Python对象，可以是数字、字符串、元祖、其他列表、字典。
a_list = [1, 3.666, [1, 2, 3], {"name": 20, 20: 10}, 4, (1, 2, 3, 4), "string", True]
print(a_list, type(a_list))
print(a_list[0], a_list[-1])

a_tuple = (1, 2, 3, 4)
print(a_tuple, type(a_tuple))

# 运行结果：
# [1, 3.666, [1, 2, 3], {'name': 20, 20: 10}, 4, (1, 2, 3, 4), 'string', True] <class 'list'>
# 1 True
# (1, 2, 3, 4) <class 'tuple'>
