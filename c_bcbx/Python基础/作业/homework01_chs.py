# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/6 17:08

# 1.提醒用户输入自己的英文名字，然后保存到字典中（以name为key）,
# 将用户输入的英文名字翻转，继续保存到刚才的字典中（以new_name为key）,
# 将字典中用户的正常的英文姓名赋值给变量real_name,
# 告知客户“您的英文名字是：” + 变量,“您的英文名字翻转是：” + 字典里获取

name = input('请输入您的英文名字：')
dic = {'name': name}
new_name = name[::-1]
dic['new_name'] = new_name
real_name = dic['name']
print('"您的英文名字是:%s"' % real_name, ',''"您的英文名字翻转是:%s"' % dic['new_name'])

# 运行结果：
# 请输入您的英文名字：heson
# "您的英文名字是:heson" ,"您的英文名字翻转是:noseh"
