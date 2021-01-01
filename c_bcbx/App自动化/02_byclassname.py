# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/20 9:29

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

    def test_by_class_name(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)

        # demo01:通过find_element_by_class_name定位TextView控件
        # 若有多个class_name相同，则默认定位第一个
        # 场景：点击关注按钮，切换至关注页面
        ele = self.driver.find_element_by_class_name('android.widget.TextView')
        time.sleep(3)
        print(ele.text)
        # 点击关注按钮
        ele.click()
        time.sleep(5)

        # demo02:通过find_elements_by_class_name定位TextView控件
        # 场景：点击图文按钮，切换到关注页面
        # find_elements_by_class_name找到所有TextView控件
        ele = self.driver.find_elements_by_class_name('android.widget.TextView')
        # 通过一个循环获取控件的索引号
        for i in range(0, len(ele)):
            print("第" + str(i) + "个" + "是" + ele[i].text)
        ele[3].click()  # 点击图文
        time.sleep(3)
        """
        返回结果：
        第0个是关注
        第1个是推荐
        第2个是视频
        第3个是图文
        ......
        执行完成！
        """

        # demo03: 通过通过find_elements_by_class_name定位ImageView控件
        # 场景：点击话题图标，进入话题页面
        self.driver.find_elements_by_class_name("android.widget.ImageView")[1].click()
        time.sleep(2)

        # demo04:
        # 场景：点击×号退出话题页面
        self.driver.find_elements_by_class_name("android.widget.ImageView")[2].click()
        time.sleep(3)

        # demo05: 通过find_elements_by_class_name定位View控件
        # 场景：点击查看第一条帖子的详情
        self.driver.find_elements_by_class_name("android.view.View")[2].click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
