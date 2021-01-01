# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/7 17:26

# 输入和输出
# print函数，将结果输出到标准输出（显示屏）上
# input函数，从标准输入中获取用户输入
# name = input('请输入你的姓名：')
# print('你的姓名是：', name)
# 运行结果：
# 请输入你的姓名：cai
# 你的姓名是： cai

# input返回的结果只是一个字符串，如果需要获取一个数字，需要使用int函数把字符串转换成数字。
num = input('please input a number:')
print('type:', type(num))  # type: <class 'str'>
num2 = int(num)
print('your number is:', num2, 'type:', type(num2))  # your number is: 20 type: <class 'int'>
