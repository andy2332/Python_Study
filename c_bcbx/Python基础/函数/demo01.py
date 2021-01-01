# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 16:16


def add(num=3):
    num = num + 1
    return num


num = add()
print(num)

num = add(5)
print(num)


def fun(x=1):
    y = x ** 3
    z = y + x
    return x, y, z


_, _, z = fun(2)
print(z)


# 不定长参数
def bdc(*canshu):
    print(canshu)


bdc(1, 1.5, True, 'hello')  # (1, 1.5, True, 'hello')


# 成对传参
def chengdu(**kv):
    print(kv)


chengdu(name='cai', age=21)  # {'name': 'cai', 'age': 21}
