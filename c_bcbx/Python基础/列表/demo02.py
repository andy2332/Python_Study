# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2021/1/15 11:26

# 可以使用[:]切片操作得到列表或元组的子集。这个动作和字符串操作是一样的。
a_list = [1, 3.666, [1, 2, 3], {"name": 20, 20: 10}, 4, (1, 2, 3, 4), "string", True]
print(a_list[0:2])  # 从0索引开始，取两个 [1, 3.666]
print(a_list[:])  # [1, 3.666, [1, 2, 3], {'name': 20, 20: 10}, 4, (1, 2, 3, 4), 'string', True]
print(a_list[::-1])  # 反转 [True, 'string', (1, 2, 3, 4), 4, {'name': 20, 20: 10}, [1, 2, 3], 3.666, 1]

a_tuple = (1, 2, 3, 4)
# 列表和元组唯一的区别是：列表中的元素可以修改，但是元组中的元素不能修改。
a_list[0] = 0
print(a_list)  # [0, 3.666, ...]

a_tuple[0] = 0  # TypeError: 'tuple' object does not support item assignment
