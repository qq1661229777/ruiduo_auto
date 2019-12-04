'''
@Author: HPX
@Date: 2019-12-04 14:17:30
@LastEditTime: 2019-12-04 14:40:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\pageElement\homePage.py
'''
import comm.common as common
# 设备标题 id 
def click_ll_my_device(driver):
    driver.find_element_by_id('net.reead.home:id/ll_my_device').click()
# 签到日历 id 
def click_iv_carding(driver):
    driver.find_element_by_id('net.reead.home:id/iv_carding').click()
# 扫一扫 id 
def click_iv_code_scan(driver):
    driver.find_element_by_id('net.reead.home:id/iv_code_scan').click()
# 按摩数据 id 
def click_RelativeLayout(driver):
    driver.find_element_by_id('android.widget.RelativeLayout').click()
# 连接设备    position 	(0.663, 0.707) 
# x, y	285, 1311
def click_iv_device(driver):
    driver.find_element_by_id('net.reead.home:id/iv_device ').click()
# 滑动中间设备
def slip_iv_device(driver):
    driver.find_element_by_id('net.reead.home:id/iv_device ').swipeLeft()

# 语音图标 
def click_iv_robot(driver):
    driver.find_element_by_id('net.reead.home:id/iv_robot').click()
