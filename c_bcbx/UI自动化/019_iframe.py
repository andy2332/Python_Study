# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/15 19:51

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://mail.163.com")
driver.maximize_window()
time.sleep(2)

# 方式一：有id，name
# driver.switch_to.frame("x-URS-iframe1608033240227.6516")

# 方式二：先定位到iframe，再定位iframe里面的元素
frame = driver.find_element_by_xpath("//div[@id='loginDiv']/iframe")
driver.switch_to.frame(frame)

driver.find_element_by_xpath("//input[@data-placeholder='邮箱帐号或手机号码']").send_keys('15059224499')
driver.find_element_by_xpath('//input[@data-placeholder="输入密码"]').send_keys('123456')
time.sleep(3)

# # 切回主文档
# driver.switch_to.default_content()

# 从子frame切回到父frame
driver.switch_to.parent_frame()
# 点击企业邮箱
driver.find_element_by_xpath("//div[@class='headerNav']/a[1]").click()
time.sleep(3)

driver.quit()
