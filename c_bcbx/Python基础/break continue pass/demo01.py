# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 15:50

# 查找[1,100)第一个3的倍数
for n in range(1, 100):
    if n % 3 == 0:
        print(n)
        break

for n in range(1, 100):
    if n % 3 != 0:
        continue  # 终止一次循环
    print(n)
    break

