# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 16:39

from selenium import webdriver
import time

driver = webdriver.Chrome()
# 自己定义一段js代码，用于模拟警告框
js = "var name = prompt('请输入你的名字：'); if (name) {alert('你的名字是：' + name)};"
driver.execute_script(js)
time.sleep(2)

# demo01:
# 打印警告框上的文本内容：“请输入你的名字：”
print(driver.switch_to.alert.text)
# 输入框输入 蔡坨坨
driver.switch_to.alert.send_keys('蔡坨坨')
time.sleep(2)
# 点击确认
driver.switch_to.alert.accept()
# 打印警告框上的文本内容：“你的名字是：蔡坨坨”
print(driver.switch_to.alert.text)
time.sleep(3)
# 点击确认
driver.switch_to.alert.accept()
time.sleep(2)
driver.quit()

# # demo02:
# # 点击取消
# driver.switch_to.alert.dismiss()
