# 作者：蔡不菜
# 时间：2020/10/16 19:20

# 函数和方法的区别
# 函数要手动传self，方法不用
# 函数用类名去调用，方法用对象去调用


class Foo(object):
    def __init__(self):
        self.name = '旺财'

    def func(self):
        print(self.name)


obj = Foo()
obj.func()
Foo.func(obj)

# 判断函数和方法的方式
from types import FunctionType, MethodType

obj = Foo()
print(isinstance(obj.func, FunctionType))
print(isinstance(obj.func, MethodType))  # 说明是个方法

print(isinstance(Foo.func, FunctionType))
print(isinstance(Foo.func, MethodType))  # 说明是个函数
