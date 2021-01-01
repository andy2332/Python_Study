# 作者：蔡不菜
# 时间：2020/10/11 12:49

# 根据类来创建对象被称为实例化
# 定义了一个名为Dog的类


class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + "is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + "rolled over!")


# 实例化
my_dog = Dog('Willie', 6)
print(my_dog.name.title())
print(str(my_dog.age))
my_dog.sit()
my_dog.roll_over()
