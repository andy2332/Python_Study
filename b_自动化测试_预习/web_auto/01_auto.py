# 作者：蔡坨坨
# 时间：2020/10/28 20:07

from selenium import webdriver
import time

# driver对象是WebDriver实例化对象，相当于一个遥控器；
# 将浏览器驱动所在的目录C:\driver配置到path路径下，括号里面可以为空；
# 执行步骤：打开浏览器驱动->打开浏览器
driver = webdriver.Chrome()

# 打开网址的方法get()
driver.get('http://www.51job.com')

# 设置间等待元素出现的时
driver.implicitly_wait(5)

# 等待页面元素加载完成
# time.sleep(1)

# WebElement实例对象
# 找到搜索框
ele = driver.find_element_by_id('kwdselectid')

# 输入python
ele.send_keys('python')

# 选择地区
ele = driver.find_element_by_id('work_position_input')
ele.click()

# time.sleep(1)

# 取消当前选中的城市
eles = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class=on]')
for ele in eles:
    ele.click()

# 取消当前城市
ele = driver.find_element_by_css_selector('#work_position_click_ip_location em[class=on]')
ele.click()

# 选择杭州
ele = driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200')
ele.click()

# 点击确认
ele = driver.find_element_by_id('work_position_click_bottom_save')
ele.click()

# 点击搜索
ele = driver.find_element_by_css_selector('.ush button')
ele.click()

'''
# 搜索结果分析
jobs = driver.find_elements_by_css_selector('.j_joblist div[class=t]')

# 循环遍历打印
for job in jobs:
    fields = job.find_element_by_tag_name('span')
    stringFileds = [field.text for field in fields]
    print('|'.join(stringFileds))
'''
