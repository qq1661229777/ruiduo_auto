'''
@Author: HPX
@Date: 2019-11-18 16:42:58
@LastEditTime: 2019-11-29 15:47:58
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\pageElement\loginPage1.py
'''
"""
登陆界面的元素
"""
import comm.common as common
#登录名
def setUserName(driver,userName):
    driver.find_element_by_id('net.reead.home:id/et_phonemail').send_keys(userName)
# #获取验证码
# def setUserPwd(driver, userPwd):
#     driver.find_element_by_name('password').send_keys(userPwd)
# 判定是否第一次安装
def is_login(driver):
    isExist = common.isElementExist(1, driver, 'splash_first_btn')
    return isExist
# 登录按钮
def click_login(driver):
    driver.find_element_by_id('net.reead.home:id/tv_login').click()
# 点击手机号输入框
def click_phone(driver):
    driver.find_element_by_id('net.reead.home:id/et_phone').click()
#  输入手机号
def search_input(driver,text):
    driver.find_element_by_id('net.reead.home:id/et_phone').send_keys(text)
#验证码输入框
def click_verify_code(driver):
    driver.find_element_by_id('net.reead.home:id/et_verify_code').click()
#  输入验证码
def search_verifyinput(driver,text):
    driver.find_element_by_id('net.reead.home:id/et_verify_code').send_keys(text)
#用户协议
def click_userAgreement(driver):
    driver.find_element_by_id('net.reead.home:id/tv_userAgreement').click()
#获取验证码
def click_btn(driver):
    driver.find_element_by_id('net.reead.home:id/count_down_btn').click()
#微信登录
def click_wx(driver):
    driver.find_element_by_id('net.reead.home:id/iv_wechat').click()
    driver.find_element_by_id('com.huawei.android.internal.app:id/icon').click()

#清空功能(待补充)

'''
判断是否有系统弹窗
0：text
1: id
2:name
'''
def sys_playPermiss(driver):
    isExist = common.isElementExist(1, driver, 'tv_des')
    return isExist





#音乐类型选择
# def select_type(driver):
#     driver.find_element_by_xpath("//*[@text='Country']").click()
#     driver.find_element_by_xpath("//*[@text='Jazz']").click()
# # 判断音乐类型数据是否拉取到
# def is_Type(driver):
#     isExist = common.isElementExist(0, driver, '//*[@text="Country"]')
#     return isExist
#音乐类型保存按钮
# def click_save(driver):
#     driver.find_element_by_id('customized_btn').click()
# #音乐类型界面的下一步按钮
# def click_skip(driver):
#     driver.find_element_by_id('customized_skip_txt').click()