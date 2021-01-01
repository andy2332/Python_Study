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

    def test_attribute(self):
        self.driver.implicitly_wait(60)
        time.sleep(8)

        # 获取当前活动页面
        current_activity = self.driver.current_activity
        print(current_activity)

        # 定位搜索按钮，赋值给ele_search
        ele_search = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b")

        # 获取控件的属性值
        # 获取控件的className
        print(ele_search.get_attribute("className"))
        # 获取控件的resourceId
        print(ele_search.get_attribute("resourceId"))

        # 判断控件是否显示
        print(ele_search.is_displayed())
        # 判断控件是否可用
        print(ele_search.is_enabled())

        """
        .ui.home.page.PageMainActivity
        android.widget.ImageView
        cn.xiaochuankeji.tieba:id/ic_search_b
        True
        True
        执行结束！
        """


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
