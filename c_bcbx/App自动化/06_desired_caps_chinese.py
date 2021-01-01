# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/22 18:44

import unittest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AndroidTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "10"
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        # 输入中文
        desired_caps['unicodeKeyboard'] = 'True'  # 安装appium自带输入法
        desired_caps['resetKeyboard'] = 'True'  # 重置键盘，修改默认输入法

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        print("执行完成!")

    def test_chinese(self):
        time.sleep(8)
        # 点击第一条帖子的评论按钮
        el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/middle_view").click()
        time.sleep(5)
        # 点击评论输入框
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").click()
        time.sleep(4)
        # 输入评论内容12346
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/etInput").send_keys('真不错！')
        time.sleep(2)
        # 点击发送
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/send").click()
        # 通过xpath，text属性定位toast提示框
        # toast_loc = ("xpath", './/*[contains(@text,"评论发送成功")]')
        # 显式等待
        ele = WebDriverWait(self.driver, 20, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, './/*[contains(@text,"评论发送成功")]')))
        # 输出toast提示框的文本内容
        print(ele.text)
        time.sleep(2)
        self.driver.keyevent(4)
