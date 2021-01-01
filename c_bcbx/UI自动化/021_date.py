# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/16 21:01

# 情况一：
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index")
driver.maximize_window()
time.sleep(3)

# 找到时间控件，并将其内容清空
driver.find_element_by_id("HD_CheckIn").clear()
time.sleep(2)
# 将入住时间设置为2020-12-18
driver.find_element_by_id("HD_CheckIn").send_keys("2020-12-18")
time.sleep(2)

# 找到退房时间控件，将其赋给变量check_out
check_out = driver.find_element_by_id("HD_CheckOut")
time.sleep(1)
# 将内容清空
check_out.clear()
time.sleep(2)
# 退房日期设置为2020-12-20
check_out.send_keys("2020-12-20")
time.sleep(2)

driver.quit()
