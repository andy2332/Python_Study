# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/11 21:11

# 类

# 抽象
# 抽象是指对现实世界问题和实体的本质表现、行为


# 创建一个新的类
class Tester():
    # 类的特殊方法,__init__方法里面定义的参数在实例化类的时候必须要传参
    def __init__(self, house_type):
        self.house_type = house_type

    developer = 'SOHO'

    def show_price(self, s):
        if self.house_type == '洋房':
            print('单价30000/每平米')
            print('整套的价格是：%d' % (30000 * s))
        elif self.house_type == '小高层':
            print('单价25000/每平米')
        else:
            print('单价20000/每平米')


# 实例化类
cai = Tester('洋房')
cai.show_price(100)
cai.house_type == '小高层'
