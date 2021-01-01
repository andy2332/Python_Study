# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/9 21:52

list01 = [1, 2, 3]
try:
    print(list01[2])  # IndexError: list index out of range，try except捕获异常，后面程序正常运行

    handle = open(r'test02.txt', 'r', encoding='utf-8')  # No such file or directory: 'test02.txt'
except Exception as error:
    # except IndexError:
    print(error)
    print(type(error))
    if str(error) == 'list index out of range':
        print('IndexError')
    elif str(error) == "[Errno 2] No such file or directory: 'test02.txt'":
        print('FileNotFoundError')

# print(list01[3])  # 没有抛异常，后面的程序无法运行

print('成功捕获异常')
