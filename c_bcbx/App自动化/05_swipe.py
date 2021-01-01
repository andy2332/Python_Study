# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/22 21:05

import unittest
import time
from appium import webdriver


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        print("执行结束！")

    def test_swipe(self):
        self.driver.implicitly_wait(60)
        time.sleep(8)

        self.driver.swipe(500, 1000, 500, 2000)  # 手势下拉
        time.sleep(3)
        self.driver.swipe(500, 2000, 500, 1000)  # 手势上滑
        time.sleep(3)
        self.driver.swipe(500, 2000, 500, 2000, 100)  # 点击
        time.sleep(3)
        self.driver.swipe(500, 2000, 500, 2000, 3000)  # 长按
        time.sleep(3)

        # 获取手机分辨率
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        print("手机分辨率是：" + str(height) + "*" + str(width))
        # 按照手机分辨率定位
        self.driver.swipe(width * 0.463, height * 0.448, width * 0.463, height * 0.896, 100)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
