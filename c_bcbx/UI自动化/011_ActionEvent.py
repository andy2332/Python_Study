# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 14:55

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://101.133.169.100/yuns/index.php")
time.sleep(3)
# 窗口最大化
driver.maximize_window()

# 输入文本信息
# 搜索框输入 男鞋
driver.find_element_by_xpath("//form/input[1]").send_keys("男鞋")
time.sleep(2)

# 清除文本信息
# 清空搜索框中的文本信息
driver.find_element_by_xpath("//form/input[1]").clear()
time.sleep(2)

# 点击事件
# 点击秒杀
driver.find_element_by_xpath("//div[@class='nav_pub']/a[2]").click()
time.sleep(3)

driver.quit()
