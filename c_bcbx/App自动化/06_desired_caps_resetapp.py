# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/22 19:06

import os
import unittest
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "10"
        desired_caps['deviceName'] = 'Android Emulator'

        # 重置app
        desired_caps['fullReset'] = "true"
        # .apk文件的路径
        desired_caps['app'] = r"D:\Desktop\Testman_Study\apk\zuiyou518.apk"
        # desired_caps['app'] = PATH("D:\Desktop\Testman_Study\apk\zuiyou518.apk")

        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        print("执行完成!")

    def test_resetApp(self):
        pass
