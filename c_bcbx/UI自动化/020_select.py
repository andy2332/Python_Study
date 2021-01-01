# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/16 20:49

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# select控件
#
# <select id="J_roomCountList">
#   <option selected="selected" value="1">1间</option>
# 	<option value="2">2间</option>
#    ...
# </select>

driver = webdriver.Chrome()

# 打开携程旅游网站
driver.get("https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index")
driver.maximize_window()
time.sleep(3)

# 找到select控件，将其赋给变量s
s = driver.find_element_by_id("J_roomCountList")

# 方法一：
# select_by_visible_text
# 比如：
# <option value="2">2间</option>
# option中间的文本
Select(s).select_by_visible_text("2间")
time.sleep(2)

# 方法二：
# select_by_index
# 下标是从0开始
# 选择4间
Select(s).select_by_index(3)
time.sleep(2)

# 方法三：
# select_by_value
# 选择6间
Select(s).select_by_value("6")
time.sleep(3)

driver.quit()
