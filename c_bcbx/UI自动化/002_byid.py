# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 13:42

from selenium import webdriver
import time

driver = webdriver.Chrome()  # 实例化

# demo01:
# 打开云商网站
driver.get("http://101.133.169.100/yuns/index.php")
# 窗口最大化
driver.maximize_window()
time.sleep(2)

# 点击我的购物车进行跳转
driver.find_element_by_id('cart_num').click()
time.sleep(2)

# demo02:
# 打开百度，搜索框中输入 编测编学，点击百度一下
driver.get("http://www.baidu.com")
time.sleep(2)
driver.find_element_by_id("kw").send_keys("编测编学")
time.sleep(2)
driver.find_element_by_id("su").click()
time.sleep(3)

driver.quit()

# driver.find_element_by_xpath("//div[@class='small_cart_name']/i")
