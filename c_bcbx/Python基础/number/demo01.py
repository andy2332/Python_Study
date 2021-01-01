# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 13:39

# Number（数字）
# Python没有int，float这样的关键字，但是实际上数据的类型是区分int，float这样的类型的；
# Python3支持int（长整型）、float、bool、complex（复数）；
# 内置函数type()可以用来查询变量所指的对象类型。

a = 1
print(type(a))
b = 0.1
print(type(b))
c = True
print(type(c))
d = 10 + 5j
print(type(d))

# 此外，还可以用insinstance来判断
num = 222
result = isinstance(num, int)
print(result)

# 布尔值表示真（True）和假（False）
# 布尔类型的变量，也是一种特殊的整数类型，在和整数进行运算时，True被当做1，False被当作0
b1 = True
sum = b1 + 2
print(sum)  # 3
