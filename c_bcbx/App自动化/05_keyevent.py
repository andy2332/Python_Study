# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/22 19:26

import unittest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def test_key_event(self):
        time.sleep(8)
        # 返回键
        self.driver.keyevent(4)
        self.driver.implicitly_wait(5)
        # toast提示框
        # 设置最长等待时间20s，每隔0.1s检测一次，直至控件出现
        ele = WebDriverWait(self.driver, 20, 0.1).until(
            EC.presence_of_element_located((By.XPATH, './/*[contains(@text,"再按一次返回键")]')))
        print(ele.text)
        # 再按一次返回键，退出程序
        self.driver.keyevent(4)

        """
        KEYCODE_MENU 菜单键82
        KEYCODE_BACK 返回键4
        KEYCODE_SEARCH 搜索键84
        KEYCODE_ENTER 回车键66
        KEYCODE_DEL 退格键67
        KEYCODE_FORWARD_DEL 删除键112
        ......
        """
