# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 14:40

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://101.133.169.100/yuns/index.php")
driver.maximize_window()
time.sleep(2)

# 获取网站标题
title = driver.title
print(title)

driver.find_element_by_link_text("联系客服").click()
# 获取当前页面的网址并打印
url = driver.current_url
print(url)

driver.quit()
