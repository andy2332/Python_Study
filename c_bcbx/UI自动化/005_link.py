# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/15 17:44

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://101.133.169.100/yuns/index.php")
driver.maximize_window()
time.sleep(2)

# demo01:
# 点击 T恤男2016
# 精确匹配超链接载体
driver.find_element_by_link_text("T恤男2016").click()
time.sleep(2)

# demo02；
# 点击联系客服
driver.find_element_by_link_text("联系客服").click()
time.sleep(2)

# demo01:
# 点击 9.9抢大牌
# partial_link_text 模糊匹配超链接载体
driver.find_element_by_partial_link_text("抢大牌").click()
time.sleep(2)

# demo02:
# 点击 家装节
driver.find_element_by_partial_link_text("家装").click()
time.sleep(2)

driver.quit()
