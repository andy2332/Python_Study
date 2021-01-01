# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/22 19:26

import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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

    def test_touch_action(self):
        self.driver.implicitly_wait(60)
        time.sleep(8)

        # 点击控件
        # 点击搜索控件
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b")
        TouchAction(self.driver).tap(ele).perform()
        time.sleep(3)

        # 坐标点击
        # 点击坐标(150,150)
        # 点击搜索框，出现键盘
        TouchAction(self.driver).tap(x=150, y=150).perform()
        time.sleep(2)

        # 按压某个点
        # 按压搜索框以外的空白处，键盘消失
        TouchAction(self.driver).press(x=150, y=1040).release().perform()
        time.sleep(2)

        # 返回到推荐页面
        self.driver.keyevent(4)
        time.sleep(3)

        # 长按某个点
        # 长按第一条帖子
        TouchAction(self.driver).long_press(x=500, y=600).release().perform()
        time.sleep(2)

        TouchAction(self.driver).press(x=500, y=600).release().perform()
        time.sleep(2)

        # 长按控件
        # 长按第一条帖子
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/holder_flow_rmdv")
        TouchAction(self.driver).long_press(ele).perform()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
