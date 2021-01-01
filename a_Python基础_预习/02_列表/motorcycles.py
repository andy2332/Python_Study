# 作者：蔡不菜
# 时间：2020/10/14 21:41

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改元素
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')  # 在末尾增加一个元素
print(motorcycles)

# 动态创建列表append()
motorcycles_2 = []
motorcycles_2.append('honda')
motorcycles_2.append('yamaha')
motorcycles_2.append('suzuki')
print('动态创建c列表：', motorcycles_2)

# 插入元素insert()
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 从列表中删除元素del 删除后不再使用此元素
del motorcycles_2[0]
print(motorcycles_2)
del motorcycles_2[1]
print(motorcycles_2)

# 使用pop()方法删除元素 将元素弹出 可以继续使用它
print('-----使用pop()方法删除元素------')
motorcycles.insert(0, 'motor1')
print(motorcycles)
popped_motorcycle = motorcycles.pop()  # 默认弹出最后一个元素
print(motorcycles)
print(popped_motorcycle)
popped_motorcycle_2 = motorcycles.pop(0)  # 弹出指定位置的值
print(motorcycles)
print(popped_motorcycle_2)

# 根据值删除元素remove()函数
print('-----根据值删除元素remove()函数-----')
motorcycles_3 = ['honda', 'yamaha', 'suzuki']
print('motorcycles_3:', motorcycles_3)
motorcycles_3.remove('honda')
print(motorcycles_3)

# 使用remove()从列表中删除元素时，也可接着使用它的值
print('-------使用remove()从列表中删除元素时，也可接着使用它的值--------')
motorcycles_4 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_4)

too_expensive = 'ducati'
motorcycles_4.remove(too_expensive)
print(motorcycles_4)
print('\nA ' + too_expensive.title() + 'is too expensive for me.')
# 方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值

