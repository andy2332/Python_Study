# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 14:51

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://101.133.169.100/yuns/index.php")
time.sleep(3)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 设置浏览器的宽600和高800
driver.set_window_size(600, 800)
time.sleep(3)

driver.quit()
