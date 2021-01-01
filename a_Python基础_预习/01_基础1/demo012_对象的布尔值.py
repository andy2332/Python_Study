# 作者：蔡不菜
# 时间：2020/10/6 20:03

# Python一切皆对象，所有对象都有一个布尔值 获取对象的布尔值 使用内置函数 bool()
# 布尔值为False的对象有：False、数值0、None、空字符串、空列表、空元组、空字典、空集合

print(bool(False))

print(bool(0))
print(bool(0.0))

print(bool(None))

print(bool(''))
print(bool(""))

print(bool([]))  # 空列表
print(bool(list()))

print(bool(()))  # 空元组
print(bool(tuple()))

print(bool({}))  # 空字典
print(bool(dict()))

print(bool(set()))  # 空集合

# 其他对象的布尔值都为True
print(bool('hello'))
