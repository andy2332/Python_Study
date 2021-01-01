# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/9 23:02

# 猜数字游戏：
# 代码中生成一个随机整数.
# 然后用户输入数字后,
# 程序提示用户的输入是高了还是低了,
# 直到用户猜中这个数字, 游戏结束.
# 提示, random模块的randint函数能够帮助我们生成随机整数。

from random import randint

correct_num = randint(1, 20)  # 随机生成一个大于等于1，小于等于20的整数
is_quit = 'n'  # 设置变量is_quit，用于判断是否退出游戏
print('请输入一个1-20的整数(输入q/Q/666可直接退出游戏):')
while is_quit != 'y':
    try:
        guess_num = input()  # 用于获取用户输入的值

        if guess_num.upper() == 'Q':  # upper()，用户若输入q，则自动转换成Q
            guess_num = 666  # 设置一个随机字符串，作为退出循环的条件
        guess_num = int(guess_num)  # 若用户输入的值为整数，则转换为int类型

        if guess_num == correct_num:
            print('恭喜你，猜对了,你真棒呀呀呀！')
            is_quit = input('您要退出游戏吗？ y/n :')
            while is_quit != 'y' and is_quit != 'n':
                is_quit = input('只能输入 y/n ，请重新输入:')
            if is_quit == 'n':
                correct_num = randint(1, 20)
                print('请输入一个1-20的整数(输入q/Q/666可直接退出游戏):')
        elif 1 <= guess_num < correct_num:
            print('猜小了，哈哈哈，请重新输入:')
        elif correct_num < guess_num <= 20:
            print('猜大了，哈哈哈，请重新输入:')
        elif guess_num == 666:
            is_quit = 'y'  # 用于退出循环，结束游戏
        else:
            # 若输入整数不在1-20范围内，则提示用户重新输入
            print('您输入的整数不在1-20范围内，请重新输入:')
    except ValueError:  # 若输入非整数类型，捕获异常
        print('您输入的不是一个整数，请重新输入:')

print('游戏结束！')
