# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/9 22:36

from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get('http://www.baidu.com')

time.sleep(5)

driver.quit()
