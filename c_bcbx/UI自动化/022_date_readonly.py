# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/16 21:07

# 情况二：
# <input readonly="readonly" value="2020-12-16" class="dp-input" data-v-8f7a73f6="">
# 时间输入框 readonly="readonly"
# 通过js代码将readonly属性去掉

from selenium import webdriver
import time

driver = webdriver.Chrome()

# demo01:
driver.get("https://www.12306.cn/index/")
driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//i[@class="icon icon-wangfan"]').click()
time.sleep(2)

# 定义一段js代码

# 1.通过getElementById找到时间控件
# js = "document.getElementById('go_date').removeAttribute('readonly')"

# 2.通过getElementsByName定位时间控件
# js = "document.getElementsByName('')[].removeAttribute('readonly')"

# 3.通过getElementsByTagName定位时间控件
js = 'document.getElementsByTagName("input")[11].removeAttribute("readonly")'

# 执行js
driver.execute_script(js)
driver.find_element_by_id("go_date").clear()
time.sleep(2)
driver.find_element_by_id("go_date").send_keys("2020-12-18")
time.sleep(2)

# demo02:
driver.get('https://hotel.meituan.com/chengdu/')
time.sleep(3)

# 定义一段js代码，将元素的readonly属性移除掉
js = "document.getElementsByTagName('input')[2].removeAttribute('readonly')"
# 执行js
driver.execute_script(js)
driver.find_elements_by_tag_name('input')[2].clear()
driver.find_elements_by_tag_name('input')[2].send_keys("2020-12-22")
time.sleep(3)

driver.quit()
