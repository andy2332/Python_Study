# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 17:24

# 2.提醒用户依次输入数学、语文、英语、综合四门的成绩，按照输入的成绩排序，告诉用户“您的最高的一门成绩是：”xx （不用告诉用户是哪一科）
math = int(input('请输入数学成绩：'))
chinese = int(input('请输入语文成绩：'))
english = int(input('请输入英语成绩：'))
comprehensive = int(input('请输入综合成绩：'))
ls = [math, chinese, english, comprehensive]
# 排序方法1,sorted()函数返回一个新的list
print("您的最高的一门成绩是:", sorted(ls)[-1])
# 排序方法2,sort()函数对已存在的列表ls进行操作
# ls.sort()
# print("您的最高的一门成绩是:", ls[-1])

# 运行结果
# 请输入数学成绩：90
# 请输入语文成绩：88
# 请输入英语成绩：85
# 请输入综合成绩：80
# 您的最高的一门成绩是: 90
