# 作者：蔡不菜
# 时间：2020/10/14 21:22

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())  # 提取第一款自行车 title()方法使首字母大写
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])  # 列的最后一个元素
print(bicycles[-3])  # 倒数第三个

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
