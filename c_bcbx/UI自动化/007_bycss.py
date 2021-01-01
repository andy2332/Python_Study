# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/13 14:07

from selenium import webdriver
import time

driver = webdriver.Chrome()

# 打开云商网站
driver.get("http://101.133.169.100/yuns/index.php")
driver.maximize_window()
time.sleep(2)

# demo01:
# 绝对路径，使用 > 分隔，在搜索框中输入童装
driver.find_element_by_css_selector("html>body>div>div>div>div>form>input:nth-child(1)").send_keys("童装")
time.sleep(2)

# demo02:
# 绝对路径，使用 空格 分隔，点击“家装节”进行跳转
driver.find_element_by_css_selector("html body div.logo_bar div div.sch div.schhot a:nth-child(2)").click()
time.sleep(2)

# demo03:
# 绝对路径，使用 > 加 空格 分隔，点击“T恤男2016”进行跳转
driver.find_element_by_css_selector("html body div.logo_bar div > div.sch > div.schhot > a:nth-child(5)").click()
time.sleep(2)

# demo04:
# 相对路径，通过class选择器定位元素，清空搜索框中的文本信息
# class选择器： .
driver.find_element_by_css_selector("input.but1").clear()
time.sleep(2)

# demo05:
# 通过class选择器定位元素，在搜索框中输入女装
driver.find_element_by_css_selector(".but1").send_keys("女装")
time.sleep(2)

# demo06:
# 通过class选择器定位元素，点击搜索按钮
driver.find_element_by_css_selector(".but2").click()
time.sleep(2)

# demo07:
# 通过id选择器定位元素，点击购物车
# id选择器： #
driver.find_element_by_css_selector("i#cart_num").click()
time.sleep(2)

# demo08:
# first-child，点击首页跳转至首页
driver.find_element_by_css_selector(".help>a:first-child").click()
time.sleep(2)

# demo09:
# 通过id选择器定位元素，点击购物车
driver.find_element_by_css_selector("#cart_num").click()
time.sleep(2)

# demo10:
# last-child，点击联系客服进行跳转
driver.find_element_by_css_selector(".help>a:last-child").click()
time.sleep(2)

# demo11:
# 通过属性定位，注意与XPath区别，在搜索框输入拖鞋
driver.find_element_by_css_selector("input[placeholder='请输入你要查找的关键字']").send_keys("拖鞋")
time.sleep(2)

# demo12:
# 通过多个属性定位，注意与XPath区别，清空搜索框中的文本信息
driver.find_element_by_css_selector("input[name='key'][class='but1']").clear()
time.sleep(2)

# demo13:
# 倒序 nth-last-child()，点击首页进行跳转
driver.find_element_by_css_selector(".help>a:nth-last-child(3)").click()
time.sleep(2)

# demo14:
# 在搜索框中输入球鞋
driver.find_element_by_css_selector("div[class='schbox']>form>input:nth-child(1)").send_keys("球鞋")

# demo15:
# css_selector 不区分干儿子和亲儿子，
# 若一个标签下有多个同级标签，虽然这些同级标签的tag name不一样，但是他们是放在一起排序的
# 打开百度，在搜索框中输入 编测编学 ，点击百度一下
driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_css_selector("form#form>span:nth-child(8)>input").send_keys("编测编学")
driver.find_element_by_css_selector("form#form>span:nth-child(9)>input").click()
time.sleep(3)

# demo16；
# 点击第一个搜索结果进入编测编学官网
driver.find_element_by_css_selector("div[class='result c-container new-pmd'][id='1']>h3>a").click()
time.sleep(3)
# 列出所有句柄
handles = driver.window_handles
print(handles)
# 打印当前句柄
print(driver.current_window_handle)
# 第一个窗口的索引是0
driver.switch_to.window(handles[1])
time.sleep(2)

# demo17:
# 点击测试论坛
driver.find_element_by_css_selector("div[class='nexnav']>ul>:nth-child(4)>a").click()
time.sleep(3)

# demo18:
# 点击 编测编学软件实战训练班学习大纲
driver.find_element_by_css_selector("#portal_block_48_content>h5>a").click()
time.sleep(5)

# 关闭当前窗口
driver.close()
time.sleep(3)

# 关闭所有窗口
driver.quit()

# tag = driver.find_elements_by_tag_name("input")
