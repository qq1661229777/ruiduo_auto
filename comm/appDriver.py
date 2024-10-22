'''
@Author: HPX
@Date: 2019-11-12 18:42:02
@LastEditTime: 2019-11-20 17:39:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Mobile_UI\comm\webDriver.py
'''
from appium import webdriver
import os
import time
import comm.runSet as runSet
from comm.md_logger import myLog

PATH = lambda p: os.path.join(os.path.split(os.path.dirname(__file__))[0], p)
countA = 1
class appDriver:
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器驱动
        cls.driver.quit()
        # cls.driver.close()
        #获取测试用例个数,如果执行完，就stop appium
        caseCount = runSet.set_suite().countTestCases()
        if countA == caseCount + 1:
            # cls.driver.removeApp("io.appium.android.ime");
            # 关闭appium服务
            os.system('start stopAppiumServer.bat')
        # pass

    # noinspection PyGlobalUndefined
    @classmethod
    def setUpClass(cls):
        global driver, countA
        #appium启动服务只运行一次
        if countA == 1:
            # 启动appium服务
            os.system('start startAppiumServer.bat')
        countA = countA + 1
        # 所有的test运行前运行一次
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': '127.0.0.1：4723',
            'appPackage': 'net.reead.home',
            'appActivity': 'net.reead.home.login.view.activity.SplashActivity',
            'unicodeKeyboard': 'True',#使用unicode方式发送字符
            'resetKeyboard': 'True',#隐藏键盘
            'noReset': 'True',  # 如果app存在,不再重新安装
            'app': PATH('./apps/ReeadHome_v3.1.2_Huawei(2).apk')
        }
        try:
            cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            myLog.logger().info('driver加载成功 %s', cls.driver)
        except Exception as e:
            myLog.logger().info('driver加载失败 %s',e)
            cls.driver.implicitly_wait(10)
            

        #cls.LIST_LATIN = "adb shell ime set com.android.inputmethod.latin/.LatinIME"
        #cls.LIST_APPIUM = "adb shell ime set io.appium.android.ime/.UnicodeIME"
