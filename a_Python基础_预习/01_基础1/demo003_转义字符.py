# 作者：蔡不菜
# 时间：2020/10/2 13:27

# 转义字符
# \ + 转义功能的首字母 例如：\n n-->newline的首字母表示换行

print('hello\nworld')  # \n 换行

print('hello\tworld')  # \t tab键，水平制表符
print('helloooo\tworld')  # \t tab键,占四个空格的位置

print('hello\rworld')  # \r 回车键，world将hello进行了覆盖

print('hello\bworld')  # \b 退格，将o退没了

print('http:\\\\www.baidu.com')  # \\ 表示斜杠   \\\\ 表示双斜杠

print('小明说:\'我吃饱了!\"')  # \' 单引号 \" 双引号

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
print(r'hello\tworld')

# 注意：最后一个字符不能是反斜杠
# print(R'helloworld\')
