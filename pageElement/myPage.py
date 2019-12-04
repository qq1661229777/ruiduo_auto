'''
@Author: HPX
@Date: 2019-11-20 13:52:35
@LastEditTime: 2019-12-04 13:59:33
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\pageElement\myPage.py
'''
import comm.common as common
import time
# 我的 标题
def click_my(driver):
    driver.find_element_by_id('net.reead.home:id/ll_user_profile').click()
# 瑞币入口
def click_ll_coin(driver):
    driver.find_element_by_id('net.reead.home:id/ll_coin').click()
# 头像入口
def click_avatar(driver):
    driver.find_element_by_id('net.reead.home:id/iv_avatar').click()
# 我的设备
def click_device_manager(driver):
    driver.find_element_by_id('net.reead.home:id/rl_device_manager').click()
# 按摩记录
def click_record(driver):
    driver.find_element_by_id('net.reead.home:id/rl_record').click()
# 我的瑞币
def click_ruibi(driver):
    driver.find_element_by_id('net.reead.home:id/rl_ruibi').click()
# 按摩提醒
def click_alarm(driver):
    driver.find_element_by_id('net.reead.home:id/rl_alarm').click()
# 设置
def click_set(driver):
    driver.find_element_by_id('net.reead.home:id/rl_set').click()
# 关于我们
def click_about_us(driver):
    driver.find_element_by_id('net.reead.home:id/rl_about_us').click()
# 我的设备-添加设备
def click_iv_scan(driver):
    driver.find_element_by_id("net.reead.home:id/iv_scan").click()
# 我的设备—解绑设备
def click_tv_remove(driver):
    driver.find_element_by_id('net.reead.home:id/tv_remove').click()
# 我的设备-进入设备
def click_tv_connectDevice(driver):
    driver.find_element_by_id('net.reead.home:id/tv_connectDevice').click()
# 我的设备-备注名   
def click_tv_bake(driver):
    driver.find_element_by_id('net.reead.home:id/tv_bake').click()
# 我的设备-设置备注名-确定   
def send_et_bark(driver,text):
    driver.find_element_by_id('net.reead.home:id/et_bark').send_keys(text)
    time.sleep(1)
    driver.find_element_by_id('net.reead.home:id/bt_ok').click()    
# 我的设备-设置备注名-取消 
def click_bt_cancel(driver,text):
    driver.find_element_by_id('net.reead.home:id/et_bark').send_keys(text)
    driver.find_element_by_id('net.reead.home:id/bt_cancel').click()
#  我的设备-产品说明书
def click_rl_pdf(driver):
    driver.find_element_by_id("net.reead.home:id/rl_pdf").click()
# 我的设备-手电筒   
def click_iv_light(driver):
    driver.find_element_by_id('net.reead.home:id/iv_light').click()
# 按摩记录-数据展示按钮  
def click_group_item(driver):
    driver.find_element_by_id('net.reead.home:id/group_item_indicator').click()
# 按摩记录-统计   
def click_iv_statistics(driver):
    driver.find_element_by_id('net.reead.home:id/iv_statistics').click()
# 我的瑞币-瑞币明细   
def click_rl_ruibiDetail(driver):
    driver.find_element_by_id('net.reead.home:id/rl_ruibiDetail').click()
# 我的瑞币-相关规则   
def click_rl_rule(driver):
    driver.find_element_by_id('net.reead.home:id/rl_rule').click()


