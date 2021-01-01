# 作者：蔡不菜
# 时间：2020/10/2 13:54

# 变量名 赋值运算符 值

"""
变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greetingmessage会引发错误。
不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print。
变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。
注意：就目前而言，应使用小写的Python变量名。在变量名中使用大写字母虽然不会导致错误，但避免使用大写字母是个不错的主意
"""

name = '蔡不菜'
print(name)
print('标识:', id(name))
print('类型:', type(name))
print('值:', name)

print('------------------')
n = 'Jack'
print(n)
n = 'Jane'
print(n)
