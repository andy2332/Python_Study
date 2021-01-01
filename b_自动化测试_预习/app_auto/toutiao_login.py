# 作者：蔡坨坨
# 时间：2020/10/29 19:28
# 开发者头条App自动化登录
from appium import webdriver
import time
import traceback

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'D:\Desktop\Testman_Study\Web自动化\toutiao_3.7.5.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard'] = True  # 输入中文是要用到
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000

# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)

    # 根据id找到元素，并点击，id和html元素的id不同
    driver.find_element_by_id("io.manong.developerdaily:id/tab_bar_plus").click()
    time.sleep(1)
    driver.find_element_by_id("io.manong.developerdaily:id/btn_email").click()
    time.sleep(1)

    # 输入用户名、密码
    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_email")
    ele.send_keys('291151689@qq.com')
    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_password")
    ele.send_keys('123456')

    time.sleep(2)
    # 点击登录
    driver.find_element_by_id("io.manong.developerdaily:id/btn_login").click()

except:
    print(traceback.format_exc())

input('**** Press to quit..')
