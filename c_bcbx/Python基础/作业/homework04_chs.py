# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 18:08

# 4.用python实现冒泡算法，给你一个包含若干值的列表，将他们从小到大排序输出（不能用sort或者sorted,自己用代码实现）
# eg:
# maopao([2,1,8,4,3,6])
# 输出结果：[1,2,3,4,6,8]
# 冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。它重复地走访过要排序的元素列，
# 依次比较两个相邻的元素，如果顺序（如从大到小、首字母从Z到A）错误就把他们交换过来。


def bubble_sort(ls):
    # 检测列表的数据个数
    n = len(ls)  # n=6
    # i为数据排序的轮次
    # 第一轮:i=0
    for i in range(n - 1):
        # j为列表数据的下标
        # 第一轮:①j=0 ②j=1 ③j=2 ④j=3 ⑤j=4
        for j in range(0, n - i - 1):
            # 比较相邻两个数的大小
            # 第一轮:①ls[0]>ls[1]:True ②ls[1]>ls[2]:False ③ls[2]>ls[3]:True ④ls[3]>ls[4]:True ⑤ls[4]>ls[5]:True
            if ls[j] > ls[j + 1]:
                # 相邻两个数交换位置
                # 第一轮:①[1,2,8,4,3,6] ②[1,2,8,4,3,6] ③[1,2,4,8,3,6] ④[1,2,4,3,8,6] ⑤[1,2,4,3,6,8],第一轮结束最大值在最右边
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    # 输出排序后的数据列表
    print(ls)


def list_into_int(ls):
    for n in range(len(ls)):
        int(ls[n])
        print(ls)
    return ls



ls = [2, 1, 8, 4, 3, 6]
bubble_sort(ls)
# 运行结果：
# [1, 2, 3, 4, 6, 8]
