# 作者：蔡不菜
# 时间：2020/10/4 22:16

name = '蔡不菜'
age = 21
print('我叫' + name + '今年' + str(age) + '岁')  # 使用+号连接字符串，将整数类型转化为str类型

print('-------str()将其他类型转化为字符串类型-------')
i = 90
f = 99.99
b = True
print(str(i), type(str(i)))
print(str(f), type(str(f)))
print(str(b), type(str(b)))

print('--------int()将其他数据类型转化为int类型----------')
f = 90.98
b = True
s1 = '90'
s2 = '90.99'
s3 = 'hello'
print(int(f), type(int(f)))  # float类型转化为int类型，截取整数部分，舍去小数部分
print(int(b), type(int(b)))
print(int(s1), type(int(s1)))
# print(int(s2), type(int(s2)))  # str类型转化为int类型，字符串不能是浮点数
# print(int(s3), type(int(s3)))  # str类型转化为int类型，字符串不能是非数字形式

print('-------float()函数，将其他数据类型转化为float类型---------')
i = 90
s1 = '90'
s2 = '90.99'
s3 = 'hello'
b = True
print(float(i), type(float(i)))
print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
# print(float(s3), type(float(s3))) #字符串中的数据如果是非数字，则不能转化
print(float(b), type(float(b)))
