# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/7 17:47

# 操作符
# Python中支持 + - * / % （加、减、乘、除、取余）这样的操作符
a = 1
b = 2
print(a + b)  # 3
print(a - b)  # -1
print(a * b)  # 2
print(a / b)  # 0.5
print(a % b)  # 1

# // 是地板除，无论操作数类型如何，都会对结果进行取地板运算（向下取整）
print(a // b)  # 0

# ** 表示乘方运算
c = 3
print(c ** 3)  # 27

# 比较运算符，>、<、==、>=、<=、!= ，返回一个布尔值。
print(2 < 3)  # True
print(2 > 3)  # False
print(2 == 3)  # False
print(2 >= 3)  # False
print(2 <= 3)  # True
print(2 != 3)  # True

# 逻辑运算符and、or、not

# 字符串之间可以使用== 或者 ！= 来判断字符串的内容是否相同。
'test' == 'tester'  # False
'test' != 'tester'  # True

# 字符串之间也可以比较大小，这个大小的结果取决于字符串的字典序
# 从小到大 0-9 A-Z a-z
'a' < 'bb'  # True
