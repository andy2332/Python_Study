# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 14:06

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
# 打开云商网站
driver.get("http://101.133.169.100/yuns/index.php")
# 窗口最大化
driver.maximize_window()
time.sleep(2)

# demo01:
# 绝对路径
# 搜索框输入 阿迪达斯
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/input[1]").send_keys("阿迪达斯")
time.sleep(2)

# demo02:
# 绝对路径
# 点击搜索
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/input[2]").click()
time.sleep(2)

# demo03:
# 绝对路径
# 点击 芭芭鸭
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/dl/dd/a[31]").click()
time.sleep(2)

# demo04:
# 相对路径
# 搜索框输入 女装
# XPath相对路径以 // 开头，通过属性匹配 @class=
driver.find_element_by_xpath("//input[@class='but1']").send_keys("女装")
time.sleep(2)

# demo05；
# 清空搜索框中的内容
# 通过多个属性匹配，使用and连接
driver.find_element_by_xpath("//input[@class='but1' and @name='key']").clear()
time.sleep(2)

# demo06:
# 搜索框输入 童装
# 通过属性模糊匹配 [contains(@属性名,'属性值')]
driver.find_element_by_xpath("//input[contains(@placeholder,'请输入')]").send_keys("童装")

# demo07；
# 点击搜索
driver.find_element_by_xpath("//form/input[2]").click()
time.sleep(2)

# demo08:
# 点击 我的购物车
driver.find_element_by_xpath("//div[@class='small_cart_name']/i").click()
time.sleep(2)

# demo09:
# 点击现在就去购物
# 通过 * 匹配
driver.find_element_by_xpath("//*[@class='r']/a").click()
time.sleep(2)

# demo10:
# 点击登录 跳转到登录页面
driver.find_element_by_xpath("//div/a").click()
time.sleep(2)

# demo11:
# 输入用户名：15059224492
driver.find_element_by_xpath("//div[@class='binput']/input[@name='username']").send_keys("15059224492")
time.sleep(1)

# demo12；
# 输入密码：123456
driver.find_element_by_xpath("//input[@name='password']").send_keys("123456")
time.sleep(1)

# demo13:
# 点击登录按钮
driver.find_element_by_xpath("//input[@name='submit']").click()
time.sleep(2)

# demo14:
# 点击我的订单
driver.find_element_by_xpath("//div[@class='help']/a[2]").click()
time.sleep(2)

# demo15:
# 点击收货地址
driver.find_element_by_xpath("//div[@class='left']/dl/dd[3]/a").click()
time.sleep(2)

# demo16；
# 点击 新增收货地址
driver.find_element_by_xpath("//a[@id='add_address']").click()
time.sleep(2)

# demo17；
# 输入姓名：蔡坨坨
driver.find_element_by_xpath("//input[@id='recive_name']").send_keys("蔡坨坨")
time.sleep(1)
# 输入手机：15059224499
driver.find_element_by_xpath("//input[@name='mobile']").send_keys("15059224499")
time.sleep(1)

# 选择省市区
driver.find_element_by_xpath("//span[@class='area_name']").click()
time.sleep(2)
# 选择陕西省
driver.find_element_by_xpath("//div/a[27]").click()
time.sleep(2)
# 鼠标移到选择省市区
ele = driver.find_element_by_xpath("//span[@class='area_name']")
ActionChains(driver).move_to_element(ele).perform()
time.sleep(2)
# 选择西安市
driver.find_element_by_xpath("//div[@class='conbox'][2]/a[1]").click()
time.sleep(2)
# 鼠标移到选择省市区
ActionChains(driver).move_to_element(ele).perform()
time.sleep(2)
# 选择市辖区
driver.find_element_by_xpath("//div[@class='conbox'][3]/a[1]").click()
time.sleep(2)

# 输入详细地址
driver.find_element_by_xpath("//input[@placeholder='收件人详细地址']").send_keys("编测编学")
time.sleep(1)

# demo18:
# 点击确认，提示保存成功
driver.find_element_by_xpath("//div[2]/div/div[3]/a[2]").click()
time.sleep(3)

driver.quit()
