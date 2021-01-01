# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 15:07

# if语句
if 2 > 3:
    print('dei')  # dei

# if else
if 2 > 3:
    print('dei')
else:
    print('bu dei')  # bu dei

# 非0 || True
if 1:
    print('非0')  # 非0

if '':
    print('非0')
else:
    print('空字符串')  # 空字符串

if []:
    print('非0')
else:
    print('空列表')  # 空列表

if {}:
    print('非0')
else:
    print('空字典')  # 空字典

x = int(input("please input x's value:"))
y = int(input("please input x's value:"))
if x > 0:
    if y > 0:
        print('x and y >０')
    else:
        print('y <= 0')
else:
    print('x <= 0')
