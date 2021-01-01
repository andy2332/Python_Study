# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/20 10:02

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
        print("执行完成！")

    def test_xpath(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)

        # demo01: xpath通过id定位单个元素
        # 场景：定位关注按钮，并点击
        self.driver.by_xpath(
            "//android.widget.TextView[@resource-id='cn.xiaochuankeji.tieba:id/title']").click()
        time.sleep(3)

        # demo02: xpath通过id定位多个元素
        # 定位话题按钮，并点击
        # 尽量不要用find_elements_by_xpath，查找多个元素后还需要用索引定位
        ele = self.driver.find_elements_by_xpath(
            "//android.widget.ImageView[@resource-id='cn.xiaochuankeji.tieba:id/topic']")
        ele[0].click()
        time.sleep(2)

        # demo03: xpath通过text文本定位，控件属性android.widget.ImageView
        # 点击创建
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='创建']").click()
        time.sleep(2)

        # demo04: xpath通过text文本定位，无控件属性
        # 点击关闭
        self.driver.find_element_by_xpath("//*[@text='关闭']").click()
        time.sleep(2)
        # 返回到关注页面
        self.driver.keyevent(4)
        # 点击下方最中间的+号按钮，进入话题编辑页面
        self.driver.find_elements_by_xpath(
            '//android.widget.ImageView[@resource-id="cn.xiaochuankeji.tieba:id/iconTabItem"]')[2].click()
        time.sleep(3)

        # demo05: xpath通过class查找单个元素
        # 点击创建话题中的android.widget.EditText
        self.driver.find_element_by_xpath("//*[@class='android.widget.EditText']")
        # 按一次返回键隐藏键盘
        self.driver.keyevent(4)
        time.sleep(1)
        # 再按一次返回键
        self.driver.keyevent(4)
        time.sleep(2)
        # 点击不保留
        self.driver.find_element_by_xpath("//*[@text='不保留']").click()
        time.sleep(2)

        # demo06:
        # 组合定位，多个属性，用and定位
        # 定位视频按钮，并点击
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/title' and @text='视频']").click()
        time.sleep(2)

        # demo07:
        # 通过层级定位，父级找子级，只有一个子级
        # 定位搜索按钮
        self.driver.find_element_by_xpath(
            "//android.widget.FrameLayout[@resource-id='cn.xiaochuankeji.tieba:id/search_b']/android.widget.ImageView").click()
        time.sleep(2)
        self.driver.keyevent(4)
        time.sleep(2)

        # demo08:
        # 通过层级关系，父级找子级，有多个子级，则需要加上索引，索引从1开始
        self.driver.find_element_by_xpath(
            "//android.widget.FrameLayout[@resource-id='cn.xiaochuankeji.tieba:id/search_b']/android.widget.ImageView[1]").click()
        time.sleep(2)
        self.driver.keyevent(4)
        time.sleep(3)

        # demo09:
        # 子级定位父级
        # 定位 图文 按钮
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='图文']/..").click()
        time.sleep(2)

        # demo10:
        # 定位最右按钮上的文案信息，先找到父级的父级，再找到父级的兄弟级的子级
        self.driver.find_element_by_xpath(
            "//*[@text='最右']/../../android.view.ViewGroup[2]/android.widget.ImageView").click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
