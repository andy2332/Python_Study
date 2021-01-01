# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 15:31

# 循环字符串
name = 'caituotuo'
for n in name:
    print(n)

# 循环列表
lists = [1, 1.5, True, 5 + 10j, 'cai', (1, 2, 3)]
for list in lists:
    print(list)

dicts = {'id': 666, 'name': 'caituotuo', 'sex': 'boy'}
for dict in dicts:
    print(dict)
for k in dicts.keys():
    print(k)
for v in dicts.values():
    print(v, end=' ')  # 666 caituotuo boy
print('\n')
for k, v in dicts.items():
    print(k, end=' ')
    print(v, end=' ')  # id 666 name caituotuo sex boy

print('\n')
for n in range(1, 5):  # 左闭右开
    print(n)
# 1
# 2
# 3
# 4