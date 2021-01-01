# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/17 15:40

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://101.133.169.100:8088/")
driver.maximize_window()
time.sleep(2)

# 登录悟空crm系统
# 输入用户名15059224492
driver.find_element_by_name("username").send_keys("15059224492")
# 输入密码123456
driver.find_element_by_name("password").send_keys("123456")
driver.implicitly_wait(10)
# 点击登录
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[4]/div/button').click()
driver.implicitly_wait(10)

# 将鼠标移动到 快速创建
ele = driver.find_element_by_css_selector('.create-button-container>span>div>div.button-name')
ActionChains(driver).move_to_element(ele).perform()
driver.implicitly_wait(10)
# 点击审批
driver.find_element_by_xpath('/html/body/div[2]/div/div/p[2]').click()
driver.implicitly_wait(10)
# 选择请假审批
driver.find_element_by_css_selector('.vux-flexbox.vux-flex-row > div:nth-child(2)').click()
driver.implicitly_wait(3)
#
driver.find_element_by_xpath('//form/div[1]/div/div/div[1]/input').click()
time.sleep(2)
# 请假类型选择其他
driver.find_element_by_xpath('//ul/li[8]/span').click()
driver.implicitly_wait(3)

# 输入审批内容
driver.find_element_by_xpath('//form/div[2]/div/div[1]/input').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//form/div[2]/div/div[1]/input').send_keys("请假审批")
driver.implicitly_wait(5)

# 开始时间
# 点击开始时间的选择日期框
driver.find_element_by_xpath('//form/div[3]/div/div[1]/input').click()
driver.implicitly_wait(10)
# 点击选择日期框
driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[1]/div/input').click()
driver.implicitly_wait(3)
# 输入日期
driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[1]/div/input').send_keys("2020-12-16")
driver.implicitly_wait(3)
# 点击选择时间框
driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[2]/div[1]/input').click()
driver.implicitly_wait(10)
# 清空时间框
driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[2]/div[1]/input').clear()
driver.implicitly_wait(10)
# 输入时间
driver.find_element_by_xpath('//div[5]/div[1]/div/div[1]/span[2]/div[1]/input').send_keys("00:00:00")
driver.find_element_by_xpath('//div[5]/div[2]/button[2]/span').click()
driver.implicitly_wait(10)

# 结束时间
# 点击结束时间的选择日期框
driver.find_element_by_xpath('//form/div[4]/div/div[1]/input').click()
driver.implicitly_wait(10)
# 点击选择日期框
driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[1]/div/input').click()
driver.implicitly_wait(10)
# 输入日期
driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[1]/div/input').send_keys("2020-12-15")
driver.implicitly_wait(10)
# 点击选择时间框
driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[2]/div[1]/input').click()
driver.implicitly_wait(10)
# 清空时间框
driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[2]/div[1]/input').clear()
driver.implicitly_wait(10)
# 输入时间
driver.find_element_by_xpath('//div[6]/div[1]/div/div[1]/span[2]/div[1]/input').send_keys("00:00:00")
driver.find_element_by_xpath('//div[6]/div[2]/button[2]/span').click()
driver.implicitly_wait(10)

# 输入时长1
driver.find_element_by_xpath('//form/div[5]/div/div[1]/input').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//form/div[5]/div/div[1]/input').send_keys(1)
driver.implicitly_wait(10)

# 滚动条移动到底部
# div中内嵌的滚动条
js = 'document.querySelector("body > div.c-view > div > div.el-card__body > div > div.crm-create-flex").scrollTop=10000'
driver.execute_script(js)
time.sleep(3)

# 选择员工
driver.find_element_by_xpath('//form/div/div/span/div[2]/div/div').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[2]/div[1]/label[1]/span[2]/div/div/div/div').click()
driver.implicitly_wait(10)

# 点击 保存
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[3]/button[2]/span').click()
driver.implicitly_wait(10)

# driver.quit()

# 审批结束时间早于开始时间
text = driver.find_element_by_xpath('/html/body/div[8]/p').text
print(text)
