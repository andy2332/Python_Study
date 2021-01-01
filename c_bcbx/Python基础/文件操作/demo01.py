# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/9 21:25

# 文件操作
# 使用内建函数 open() 打开一个文件
# handle = open('file_name','r')
#
# 第一个参数file_name是文件的名字，可以是一个绝对路径，也可以是一个相对路径。
# 第二个参数是文件的打开方式，选项有：
# 'r':只读
# 'w':覆盖写
# 'a':追加写

# 方式一（使用相对路径）：
handle = open('test.txt', 'r', encoding='utf-8')  # 指定编码格式encoding，默认是gbk
# 方式二（使用绝对路径）：
# handle = open(r'test.txt', 'r', encoding='utf-8')

# # handle是一个文件句柄，是一个可迭代的对象，可以直接使用for循环按行读取文件内容
# for line in handle:
#     print(line.strip())  # strip()去除空格和换行
# # handle使用完毕，需要close掉，否则会引起资源泄露（一个进程能打开的句柄数目是有限的）
# handle.close()

# print(handle.read(3))
# # 读取一行，前面如果读过则不会重复读取，自动从未读取部分往下读
# print(handle.readline())
# # 读取所有行，将结果存储在result中，第一行的索引为0，以此类推
# result = handle.readlines()
# print(result[0].strip())
# handle.close()

# 写文件：向文件中写一段字符串。（PS：读文件的时候若文件不存在则无法读取，写文件的时候若文件不存在）
# 追加写
file_write = open('test02.txt', 'a', encoding='utf-8')
for n in range(1, 6):
    file_write.write('这是第%d行\n' % n)
file_write.close()

# # 覆盖写
# file_write = open('test01.txt', 'w', encoding='utf-8')
# for n in range(1, 6):
#     file_write.write('这是覆盖第%d行\n' % n)
# file_write.close()

# # with open文件
# with open('test01.txt', 'w', encoding='utf-8') as f:
#     for n in range(1, 6):
#         f.write('这是覆盖盖第%d行\n' % n)
