# 作者：蔡不菜
# 时间：2020/10/4 13:57

"""
常用数据类型
整数类型：int 99
浮点数类型：float 99.99
布尔类型：bool True False
字符串类型：str '人生苦短，我用Python'
"""

# int 可以表示正数、负数、零
print('---------------int 可以表示正数、负数、零---------------------')
n1 = 90
n2 = -90
n3 = 0
print(type(n1), n1)
print(type(n2), n2)
print(type(n3), n3)

# int型可以表示十进制、二进制、八进制、十六进制
print('---------------int型可以表示十进制、二进制、八进制、十六进制---------------------')
print('十进制', 88)
print('二进制', 0b00110101)  # 二进制以0b开头
print('八进制', 0o777765)  # 八进制咦0o开头
print('十六进制', 0x123878A)  # 十六进制以0x开头

# 浮点类型存储不精确 使用浮点数进行计算时，可能会出现小数位数不确定的情况
print('------------浮点类型存储不精确 使用浮点数进行计算时，可能会出现小数位数不确定的情况--------------')
print(1.1 + 2.2)  # 3.3000000000000003
print(1.1 + 2.1)

print('---------解决方案：导入模块decimal-----------')
# 解决方案：导入模块decimal
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))  # 3.3

# 布尔类型 表示真假 True->1 Fales->0
print('----------布尔类型 表示真假 True->1 Fales->0------------')
b1 = True
b2 = False
print(type(b1), b1)
print(type(b2), b2)
print(b1 + 1)  # 2
print(b2 + 1)  # 1

# 字符串类型
print('---------字符串类型 ----------')
s1 = '人生苦短，我用Python'
s2 = "人生苦短，我用Python"
s3 = '''人生苦短，
我用Python'''
s4 = """人生苦短，
我用Python"""
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
