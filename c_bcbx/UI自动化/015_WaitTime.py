# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 16:01

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://101.133.169.100/yuns/index.php")

# 隐式等待时间
# 添加等待时间，强制等待
time.sleep(2)

# 相当于最大等待时间，如果只用了2秒就加载出来,则无需等待10秒便继续执行后面的操作
# 存在这种情况：第一个页面有的元素在第二个页面也有，可能会出现原本要在第二个页面查找的元素，但是返回的元素是第一个页面的元素
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@class='but1']").send_keys("女装")
time.sleep(3)

# 显示等待
ele = WebDriverWait(driver, 15, 0.5).until(EC.presence_of_element_located(
    (By.XPATH, "//input[@class='but1']")))
ele.clear()
ele.send_keys("李林")
time.sleep(3)

# until_not
# ele2 = WebDriverWait(driver, 15, 0.5).until_not(EC.presence_of_element_located(
#     (By.XPATH, "//input[@class='but1']")))

driver.quit()
