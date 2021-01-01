# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 15:57

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://101.133.169.100/yuns/index.php")

driver.find_element_by_xpath("//input[@class='but1']").send_keys("阿迪达斯斯")
time.sleep(2)

# 删除一个字符
driver.find_element_by_xpath("//input[@class='but1']").send_keys(Keys.BACK_SPACE)
time.sleep(2)

# 输入空格
driver.find_element_by_xpath("//input[@class='but1']").send_keys(Keys.SPACE)
time.sleep(2)

# 输入耐克
driver.find_element_by_xpath("//input[@class='but1']").send_keys("耐克")
time.sleep(2)

# ctrl a 全选
driver.find_element_by_xpath("//input[@class='but1']").send_keys(Keys.CONTROL, 'a')
time.sleep(2)

# ctrl x 剪切
driver.find_element_by_xpath("//input[@class='but1']").send_keys(Keys.CONTROL, 'x')
time.sleep(2)

# ctrl v 粘贴
driver.find_element_by_xpath("//input[@class='but1']").send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 回车键
driver.find_element_by_xpath("//input[@class='but1']").send_keys(Keys.ENTER)
time.sleep(3)

driver.quit()
