import os
import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'
        # Appium1.6.3版本后才支持toast，之前封装的是Uiautomator，之后才是Uiautomator2
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['newCommandTimeout'] = 200

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # self.driver.quit()
        print("执行结束！")

    def test_toast(self):
        """
        toast:
        Android中的Toast是一种简易的消息提示框;
        告知用户任务状态，操作结果，例如：发送成功，加载中，删除成功;
        Toast会在屏幕所有层的最上方;
        显示时间有限，1s+左右消失。

        场景：评论帖子->点击发送->提示评论发送成功的灰黑框->1-2s后消失
        """
        # self.driver.implicitly_wait(160)
        time.sleep(8)
        # 点击第一条帖子的评论按钮
        el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/middle_view").click()
        time.sleep(5)
        # 点击评论输入框
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").click()
        time.sleep(4)
        # 输入评论内容12346
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys('123456')
        time.sleep(2)
        # 点击发送
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        # 通过xpath，text属性定位toast提示框
        # toast_loc = ("xpath", './/*[contains(@text,"评论发送成功")]')
        # 显式等待
        ele = WebDriverWait(self.driver, 20, 0.1).until(
            EC.presence_of_element_located((By.XPATH, './/*[contains(@text,"评论发送成功")]')))
        # 输出toast提示框的文本内容
        print(ele.text)
        time.sleep(2)
        self.driver.keyevent(4)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
