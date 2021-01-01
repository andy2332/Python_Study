# 作者：蔡不菜
# 时间：2020/10/6 20:11

# money = 1000  # 余额
# s = int(input('请输入您的取款金额:'))
# if s <= money:
#     money = money - s
#     print('余额为：', money)


# 双分支结构if  else
# while True:
#     num = int(input('请输入一个整数:'))
#     if num % 2 == 0:
#         print('该整数为偶数')
#     else:
#         print('该整数为奇数')


# 多分支结构
while True:
    score = int(input('请输入你的成绩：'))
    # 判断
    if 90 <= score <= 100:
        print('A')
    elif 80 <= score <= 89:
        print('B')
    elif 70 <= score <= 79:
        print('C')
    elif 60 <= score <= 69:
        print('D')
    elif score < 60:
        print('不及格')
    else:
        print('非法数字！')

