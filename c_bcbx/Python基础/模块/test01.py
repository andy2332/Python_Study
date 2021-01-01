# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/9 22:13

def bubble_sort(ls):
    # 检测列表的数据个数
    n = len(ls)  # n=6
    # i为数据排序的轮次
    for i in range(n - 1):
        # j为列表数据的下标
        for j in range(0, n - i - 1):
            # 比较相邻两个数的大小
            if ls[j] > ls[j + 1]:
                # 相邻两个数交换位置
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    # 输出排序后的数据列表
    print(ls)
