# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 14:46

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://101.133.169.100/yuns/index.php")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_link_text("9.9抢大牌").click()
time.sleep(3)

# 刷新
driver.refresh()
time.sleep(3)

# 回退
driver.back()
time.sleep(3)

# 前进
driver.forward()
time.sleep(3)

driver.quit()
