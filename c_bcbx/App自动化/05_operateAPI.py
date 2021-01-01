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

    def test_operate_api(self):
        self.driver.implicitly_wait(60)
        time.sleep(8)

        # 控件点击：click()
        # 场景：点击关注按钮
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        ele.click()
        time.sleep(2)

        # 点击搜索按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(3)
        # 点击搜索输入框
        ele_input = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/search_input")
        ele_input.click()
        # 控件输入
        ele_input.send_keys("123456")
        time.sleep(2)
        print(ele_input.text)
        ele_input.clear()
        time.sleep(2)

        # 获取手机分辨率
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        print("手机分辨率是：" + str(height) + "*" + str(width))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
