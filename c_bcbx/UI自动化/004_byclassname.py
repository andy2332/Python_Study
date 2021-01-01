# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/15 16:26

from selenium import webdriver
import time

driver = webdriver.Chrome()

# 打开云商网站
driver.get("http://101.133.169.100/yuns/index.php")
driver.maximize_window()
time.sleep(2)

# demo01:
# 搜索框中输入 女装
driver.find_element_by_class_name("but1").send_keys("女装")
time.sleep(2)

# demo02:
# 点击搜索
driver.find_element_by_class_name("but2").click()
time.sleep(3)

# 注意：如果class name是一个复合类（带有空格），则无法定位到元素
# 可以使用复合类的部分单词去定位，但是不建议，因为可能会定位到多个元素
# driver.get("http://www.baidu.com")
# time.sleep(2)
# driver.find_element_by_class_name("bg s_btn btn_h btnhover")  # NoSuchElementException

driver.quit()
