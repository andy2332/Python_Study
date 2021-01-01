# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 16:36

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_css_selector("form#form>span:nth-child(8)>input").send_keys("编测编学")
driver.find_element_by_css_selector("form#form>span:nth-child(9)>input").click()
time.sleep(3)

# 点击第一个搜索结果进入编测编学官网
driver.find_element_by_css_selector("div[class='result c-container new-pmd'][id='1']>h3>a").click()
time.sleep(3)
# 列出所有句柄
handles = driver.window_handles
print(handles)
# 打印当前句柄
print(driver.current_window_handle)
# 第一个窗口的索引是0
# 选择第二个窗口
driver.switch_to.window(handles[1])
time.sleep(2)

# 点击测试论坛
driver.find_element_by_css_selector("div[class='nexnav']>ul>:nth-child(4)>a").click()
time.sleep(3)

# 关闭当前句柄所在的窗体
driver.close()
time.sleep(3)

# 关闭所有窗体
driver.quit()
