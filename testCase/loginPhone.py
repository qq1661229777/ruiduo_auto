'''
@Author: HPX
@Date: 2019-11-20 15:57:14
@LastEditTime: 2019-11-21 16:28:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\testCase\loginRuiduo.py
'''
"""
登陆界面的case,登录数据来自于excel
根据用例名来区分进行不同情况的验证，并获取实际验证结果和excel里面的
预期结果进行对比
继承Driver类,获取app的driver
作者:HPX
"""

import time
#导入APP driver类
from comm.appDriver import appDriver
#导入界面元素类
import pageElement.loginPage as login_Page
#导入日志模块类
from comm.md_logger import myLog
#导入公共方法类
import comm.common as common
import unittest
import paramunittest
loginCase = common.get_excel_value('loginPhone')
@paramunittest.parametrized(*loginCase)
class _loginPhone(appDriver, unittest.TestCase):
    def setParameters(self, case_Name, user_Name, excepted, reMarks):
        self.case_Name = case_Name
        self.user_Name = user_Name
        self.excepted = excepted
        self.reMark = reMarks
    def test_Login(self):
        #设置用例名称
        self._testMethodDoc = self.case_Name
        myLog.logger().info('测试用例名称:' + self._testMethodDoc)
        myLog.logger().info('测试用例说明:' + self.reMark)
        
        # 点击手机号输入框
        login_Page.click_phone(self.driver)
        user_Namek = str(self.user_Name)
        user_NameP = user_Namek[0:12]
        myLog.logger().info('输入手机号  %s',user_NameP)
        # # 输入手机号
        login_Page.search_input(self.driver,user_NameP)
        # 点击登陆
        login_Page.click_login(self.driver)
        time.sleep(0.5)
        # 提示验证码后截图
        common.Screenshot1(self.driver)
