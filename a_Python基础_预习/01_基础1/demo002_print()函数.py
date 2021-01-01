# 作者：蔡不菜
# 时间：2020/10/1 11:25

# print()函数
# 向目的地输出内容；
# 输出的内容可以是数字、字符串、表达式；
# 目的地有IDLE、控制台、文件

# 可以输出数字
print(520)
print(3.14)
print("----------------------")

# 可以输出字符串
print("hello,world!")
print('hello,world!')
print("----------------------")

# 含有运算符的表达式
print(3 + 5)
print("----------------------")

# 将数据输出到文件中
# 注意：1.所指定的盘符必须存在 2.使用file=
# a+：若文件不存在则创建文件，若存在则在文件内容后面继续追加
fp = open('D:/Desktop/Python_Study_Code/print_file.txt', 'a+')
print('hello,world!', file=fp)
fp.close()

# 不进行换行输出（输出内容在一行中）:使用逗号间隔
print('hello', 'world', 'python', '!')
