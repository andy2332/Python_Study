# 作者：蔡不菜
# 时间：2020/10/16 18:20

# 嘉宾名单
guests = ['张三', '李四', '王五']
for guest in guests:
    print(guest + ' 来吃饭啦！')

print('张三无法赴约！')
guests.remove('张三')
guests.append('赵六')
for guest in guests:
    print(guest + ' 可以赴约！')

print('找到了一个更大的餐桌，可以邀请更多的人来吃饭！')
guests.insert(0, '小王')
guests.insert(2, '小李')
guests.append('小杨')
for guest in guests:
    print(guest + ' 来吃饭啦！')

print('新买的餐桌无法及时送达，只能邀请两位嘉宾')
print(guests)
guest_1 = guests.pop()  # 默认删除最后一个
print('不好意思' + guest_1)
print(guests)
guest_2 = guests.pop()
print('不好意思' + guest_2)
print(guests)
guest_3 = guests.pop()
print('不好意思' + guest_3)
print(guests)
guest_4 = guests.pop()
print('不好意思' + guest_4)
for guest in guests:
    print(guest + ' 来吃饭呀！')

# 将名单变为空
del guests[0]
del guests[0]
print(guests)
