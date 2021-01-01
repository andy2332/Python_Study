# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 13:54

# Python中可以使用单引号（'）、双引号（"）、三引号（'''/"""）来表示字符串;
str1 = 'caituotuo'
str2 = "caituotuo"
str3 = """caituotuo"""
str4 = '''caituotuo'''
print(str1, str2, str3, str4)  # caituotuo caituotuo caituotuo caituotuo

# 字符串中含有引号
str5 = 'I am "caituotuo"'
print(str5)  # I am "caituotuo"

# 同时使用反斜杠 \ 转义特殊字符，如：换行符 \n
name = 'My name is \n cai.'
print(name)
# 运行结果：
# My name is
#  cai.

# \ 本身需要 \\ 这样的方式来表示
str6 = '\\index\\'
print(str6)  # \index

# 使用索引操作符[]或者切片操作符[:]来获取子字符串。（切片操作是一个前闭后开区间）
# 字符串的索引规则：第一个字符索引是0，最后一个字符索引是-1。
str7 = 'hello world!'
print(str7[0])  # h
print(str7[-1])  # !
print(str7[1:3])  # el
print(str7[:3])  # hel
print(str7[3:])  # lo world!
print(str7[:])  # hello world!
print(str7[::2])  # hlowrd
print(str7[::-1])  # !dlrow olleh

# +用于字符串连接运算；* 表示赋值当前字符串，与之结合的数字为复制的次数。
str8 = 'tester'
str9 = 'cai'
print(str8 + str9)  # testercai
print(str8 * 1)  # tester
print(str8 * 0)  # 空
print(str8 * 3)  # testertestertester
print(str8 * -1)  # 空

# Python没有“字符类型”这样的概念，单个字也是字符串。
str10 = 'tester'
print(type(str10[0]))  # <class 'str'>

# 格式化字符串：%s； 格式化整型：%d
name = 'caituotuo'
num = 1
print('尊敬的%s用户，您抽到的码号是%d' % (name, num))  # 尊敬的caituotuo用户，您抽到的码号是1

# 内建函数len获取字符串的长度
str11 = 'hello world!'
print(len(str11))  # 12
