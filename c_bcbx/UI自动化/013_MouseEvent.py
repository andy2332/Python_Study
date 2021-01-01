# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 15:38

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://101.133.169.100/yuns/index.php")
time.sleep(2)
# 窗口最大化
driver.maximize_window()

ele = driver.find_element_by_link_text("母婴玩具")
time.sleep(3)

# 把鼠标移动到某一个控件上 .perform()使动作生效
ActionChains(driver).move_to_element(ele).perform()
time.sleep(3)

driver.find_element_by_link_text("营养辅食").click()
time.sleep(3)

# # 右击
# ActionChains(driver).context_click(ele).perform()
#
# # 双击
# ActionChains(driver).double_click(ele).perform()

# # 拖动控件
# source = driver.find_element_by_link_text("")
# target = driver.find_element_by_link_text("")
# ActionChains(driver).drag_and_drop(source, target)

# # 偏移
# ActionChains(driver).drag_and_drop_by_offset(source, 100, 0)

driver.quit()
