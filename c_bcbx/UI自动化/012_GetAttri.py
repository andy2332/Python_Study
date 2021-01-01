# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 15:03

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://101.133.169.100/yuns/index.php")
time.sleep(3)
# 窗口最大化
driver.maximize_window()

# 获取控件的尺寸
size = driver.find_element_by_xpath("//input[@class='but1']").size
print(type(size))
print("搜索框的高是：", size['height'])
print("搜索框的宽是：", size["width"])

# 获取控件上的文本信息
text = driver.find_element_by_xpath("//div[@class='schhot']/a[2]").text
print("获取控件上的文本信息：", text)

# 获取空间的属性值
href = driver.find_element_by_xpath("//div[@class='schhot']/a[2]").get_attribute('href')
print(href)

# 判断控件是否在页面中显示出来
dis = driver.find_element_by_xpath("//div[@class='schhot']/a[2]").is_displayed()
if dis == True:
    print("家装节按钮加载出来了！")
    driver.find_element_by_xpath("//div[@class='schhot']/a[2]").click()
    time.sleep(2)
else:
    time.sleep(5)
    driver.find_element_by_xpath("//div[@class='schhot']/a[2]").click()
    time.sleep(2)

# 清空文本框中的内容
driver.find_element_by_xpath("//input[@class='but1']").clear()
time.sleep(2)

# 在输入框输入文本信息，判断回显信息是否与输入一致
driver.find_element_by_xpath("//input[@class='but1']").send_keys("test")
time.sleep(2)
value = driver.find_element_by_xpath("//input[@class='but1']").get_attribute("value")
if value == "test":
    print("输入信息是test")
else:
    print("输入信息不是test")

time.sleep(3)
driver.quit()
