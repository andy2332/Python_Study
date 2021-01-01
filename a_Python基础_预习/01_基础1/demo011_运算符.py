# 作者：蔡不菜
# 时间：2020/10/4 23:12

# 运算符的优先级（有括号要先算括号里面的）：
# 算数运算
# 位运算符
# 比较运算
# 布尔运算
# 赋值运算


# 算数运算符
# 加 + 减 - 乘 * 除 / 整数 //
# 取余 %
# 幂运算 **
print(1 + 1)
print(3 - 2)
print(3 * 4)
print(4 / 5)
print(4 // 5)

print(9 % 8)
print(3 ** 3)

print('-------整除一正一负向下取整-------')
print(9 // -4)  # -3
print(-9 // 4)  # -3

print('-------取余时 一正一负时要使用公式：余数=被除数-除数*商------')
print(-9 % 4)  # -9-4*(-3)=3

# 赋值运算符
# 运算顺序从右到左
print('------赋值运算符,运算顺序从右到左------')
i = 3 + 4
print(i)

print('-----链式赋值----')
a = b = c = 5  # 链式赋值
print(a, id(a))
print(b, id(b))
print(c, id(c))

print('----参数赋值-----')
a = 20
a += 30
print(a)

b = 23
b -= 89
print(b)

c = 23
c *= 34
print(c)

d = 2
d /= 1
print(d, type(d))

e = 6
e //= 2
print(e, type(e))

f = 5
f %= 2
print(f, type(f))

print('-------解刨赋值-------')
a, b, c = 1, 2, 3
print(a, b, c)  # 左右变量的个数和值得个数要相等，否则会报错

print('-------交换两个变量的值------')
a, b = 2, 3
print(a, b)
a, b = b, a
print(a, b)

# 比较运算符
print('------比较运算符------')
a = 20
b = 10
print(a > b)
print(a < b)
print(a == b)
print(a <= b)
print(a >= b)
print(a != b)

print('-----比较标识是否相等------')
a = 10
b = 10
c = 20
print(a == b)
print(a is b)  # True 说明a和b的id是一样的
print(a is not b)
print(a is c)

print('------两个列的比较-------')
list1 = [11, 22, 33]
list2 = [11, 22, 33]
print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)
print(id(list1))
print(id(list2))

print('------布尔运算符 and  or  not  in  not in------')
a, b = 1, 2
print(a, b)

print('-------and 只有当两边都是True时才是True--------')
print(a == b and a > b)
print(a != b and a < b)

print('-------or 只需一边是True 结果就是True-----------')
print(a == b or a < b)

print('-----not 取反-------')
b1 = True
b2 = False
print(not b1)
print(not b2)

print('-----in 与not in ------')
s = 'hello world'
print('h' in s)
print('k' in s)
print('k' not in s)

# 位运算
# 将数据转成二进制进行计算
print('------位运算 将数据转成二进制进行计算------')
print(4 & 8)  # 按位与& 同时为1时结果为1
print(4 | 8)  # 按位或| 同时为0时结果为0
print(4 << 1)  # 左移一位，相当于乘以2
print(4 << 3)  # 左移三位，相当于*2*2*2
print(4 >> 1)  # 右移一位，相当于除以2
