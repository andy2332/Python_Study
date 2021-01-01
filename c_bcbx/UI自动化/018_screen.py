# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 16:49

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
time.sleep(3)
driver.get_screenshot_as_file(r"D:\Desktop\test01.png")

driver.quit()
