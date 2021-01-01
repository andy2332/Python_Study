# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/16 21:21

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.bcbxhome.com/")
driver.maximize_window()
time.sleep(2)

# 移动到页面底部
# js = "document.documentElement.scrollTop = 10000"
js = "var bottom = document.documentElement.scrollTop = 10000"
driver.execute_script(js)
time.sleep(3)

# 移动到页面中部
js = "window.scrollTo(0,document.body.scrollHeight*0.5)"
driver.execute_script(js)
time.sleep(2)

# 相对当前坐标移动 scrollBy
# 负数表示上滑，正数表示下拉
js = "window.scrollBy(0,-200)"
driver.execute_script(js)
time.sleep(2)
js = "window.scrollBy(0,300)"
driver.execute_script(js)
time.sleep(2)

# 移动到绝对坐标
js = "window.scrollTo(0,500)"
driver.execute_script(js)
time.sleep(2)
driver.find_element_by_css_selector("#portal_block_67_content > div > div.nexcousebtm > h5 > a").click()
time.sleep(2)

# 选择新窗口
driver.switch_to.window(driver.window_handles[1])
# 移动到底部
js = "document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(2)
# 再移动到顶部
driver.execute_script("document.documentElement.scrollTop=0")
time.sleep(2)

driver.quit()
