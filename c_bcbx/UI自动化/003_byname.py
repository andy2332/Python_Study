# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 13:53

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')

time.sleep(2)

# demo01:
# 搜索框中输入耐克
# 只有可输入的控件才能使用send_keys()方法，比如input控件。
driver.find_element_by_name('key').send_keys('耐克')
time.sleep(2)

# demo02:
# 清空搜索框中的信息
driver.find_element_by_name("key").clear()

time.sleep(3)
driver.quit()
