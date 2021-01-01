# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/20 9:29

import os
import unittest
import time
from appium import webdriver


class AndroidTests(unittest.TestCase):
    def setUp(self):
        """ 初始化 """

        # 定义一个desired_caps字典
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 平台名称 Android或iOS
        desired_caps['platformVersion'] = '10'  # 系统版本号 设置->关于手机->Android版本 10
        desired_caps['deviceName'] = 'Android Emulator'  # 设备名称，一般写Android Emulator就行
        desired_caps['noReset'] = 'True'  # 不重置

        # 获取appPackage和appActivity
        # 打开cmd
        # 输入adb shell dumpsys activity top | findstr "ACTIVITY"
        # ACTIVITY cn.xiaochuankeji.tieba/.ui.base.SplashActivity 9df8d05 pid=27957
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'  # app的包名，cn.xiaochuankeji.tieba
        desired_caps['appActivity'] = '.ui.base.SplashActivity'  # app当前活动界面，.ui.base.SplashActivity

        # 输入中文
        # desired_caps['unicodeKeyboard'] = 'True'  # 安装appium自带输入法
        # desired_caps['resetKeyboard'] = 'True'  # 重置键盘，修改默认输入法

        # Appium REST http interface listener started on 0.0.0.0:4723
        # Appium Server 地址及端口号
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # self.driver.quit()
        print("执行完成！")

    def test_element_by_class_name(self):
        time.sleep(8)
        self.driver.implicitly_wait(60)
        time.sleep(5)

        # demo01: driver.find_elements_by_class_name、TextView控件
        # 场景：点击关注按钮，切换到关注页面

        # driver.find_elements_by_class_name找到所有TextView控件
        ele = self.driver.find_elements_by_class_name('android.widget.TextView')
        # 通过一个循环获取控件的索引号
        for i in range(0, len(ele)):
            print("第" + str(i) + "个" + "是" + ele[i].text)
        ele[0].click()  # 点击关注
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

        # demo02: ImageView控件
        # 场景：点击话题图标，进入话题页面
        ele2 = self.driver.find_elements_by_class_name("android.widget.ImageView")
        ele2[1].click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
