# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 14:19

# 列表合并为字符串
b = '-'
a = ['aa', 'bb', 'cc']
print(b.join(a))  # aa-bb-cc

# 字符串拆分成列表
c = 'aa bb cc'
print(c.split(' '))
d = 'aaaa aaaaaa  .. cccc'
print(d.split())

# 判断字符串开头结尾，返回bool
str1 = 'Hello world, I am caituotuo!'
print(str1.startswith('Hello worl'))

# 换行 & strip()去除空格
name = '    I am caituotuo'
print(name, end='\n')  # print()默认end='\n'
print(name, end='---')  # 设置以---结尾
print(name.strip())
print(name)

# find() & replace()
name1 = 'my name is caituotuo'
print(name1.find('is'))  # 8
print(name1.find('aa'))  # -1,未找到返回-1
name2 = name1.replace('caituotuo', 'cai')  # replace不会改变字符串本身，知识暂时替换，需要给一个变量接收
print(name2)  # my name is cai
print(name1)  # my name is caituotuo

# isalpha() & isdigit()
str2 = 'hello123'
print(str2.isalpha())  # False

# 追加列表append()
list1 = ['a', 'b', 'c']
list1.append(123)
list1.append([2, 3])
print(list1)  # ['a', 'b', 'c', 123, [2, 3]]

# 删除列表中的元素
list1.remove('a')
print(list1)  # ['b', 'c', 123, [2, 3]]

# 列表比较大小
a1 = ['abc', 1233]
a2 = ['xyz', 789]
a3 = ['abc', 823]
print(a1 < a2)  # True
print(a2 < a3)  # False
print(a1 > a3)  # True
