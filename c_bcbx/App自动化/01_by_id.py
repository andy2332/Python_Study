# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2020/12/18 22:00

import unittest
import time
from appium import webdriver


class AndroidTests(unittest.TestCase):
    def setUp(self):
        """ 初始化 """
        desired_caps = {}  # 定义一个desired_caps字典
        desired_caps['platformName'] = 'Android'  # 平台名称 Android或iOS
        desired_caps['platformVersion'] = '10'  # 系统版本号 设置->关于手机->Android版本 10
        desired_caps['deviceName'] = 'Android Emulator'  # 设备名称，一般写Android Emulator就行
        desired_caps['noReset'] = 'True'  # 不重置

        # 获取appPackage和appActivity
        # 打开cmd
        # 输入adb shell dumpsys activity top | findstr "ACTIVITY"
        # ACTIVITY cn.xiaochuankeji.tieba/.ui.base.SplashActivity 9df8d05 pid=27957
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'  # app的包名，cn.xiaochuankeji.tieba
        desired_caps['appActivity'] = '.ui.base.SplashActivity'  # app首个活动界面，.ui.base.SplashActivity

        # 输入中文
        # desired_caps['unicodeKeyboard'] = 'True'  # 安装appium自带输入法
        # desired_caps['resetKeyboard'] = 'True'  # 重置键盘，修改默认输入法

        # Appium REST http interface listener started on 0.0.0.0:4723
        # Appium Server 地址及端口号
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # self.driver.quit()
        print("执行结束！")

    def test_element_by_id(self):
        self.driver.implicitly_wait(60)

        # demo01: find_element_by_id，如果id相同，则默认定位第一个
        # 场景：点击关注按钮，切换至关注页面
        ele = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        print(ele.text)
        ele.click()
        time.sleep(2)

        # demo02:
        # 场景：点击话题按钮，切换到话题页面
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/topic").click()
        time.sleep(3)

        # demo03:
        # 场景：点击×号，退出话题页面，返回关注页面
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/ic_search_b").click()
        time.sleep(2)

        # demo04: find_elements_by_id
        # 场景：点击图文按钮，切换至图文页面
        # 获取所有id为cn.xiaochuankeji.tieba:id/title的控件
        ele = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        # 通过一个循环，确认要定位的控件是第几个
        for i in range(0, len(ele)):
            print("第" + str(i) + "个" + "是" + ele[i].text, end=" ")  # 第0个是关注 第1个是推荐 第2个是视频 第3个是图文 执行结束！
        # 点击图文，图文控件的索引为3
        ele[3].click()

        # demo05:
        # 场景：点击第一条帖子的用户头像
        self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/avatar_view_avatar")[0].click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
