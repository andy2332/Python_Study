# 作者：蔡不菜
# 时间：2020/10/16 18:41

# 使用方法sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # 按字母顺序排列
print(cars)
cars.sort(reverse=True)  # 按与字母相反的顺序排列列表元素
print(cars)

# 使用函数sorted()对列表进行临时排序
cars_2 = ['bmw', 'audi', 'toyota', 'subaru']
print('原本顺序：', cars_2)
print('临时排序的顺序：', sorted(cars_2))
print('恢复原本顺序：', cars_2)

# 倒着打印
print('---------倒着打印可使用方法reverse()---------')
print(cars_2)
cars_2.reverse()
print(cars_2)

# 确定列表的长度,使用函数len()
print(len(cars_2))
