'''
@Author: HPX
@Date: 2019-11-29 16:06:25
@LastEditTime: 2019-12-04 11:19:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\pageElement\massage_remPage.py
'''
import comm.common as common
# 按摩提醒-添加提醒  
def click_iv_add(driver):
    driver.find_element_by_id('net.reead.home:id/iv_add').click()
# 按摩提醒-提醒频次 
def click_rl_week(driver):
    driver.find_element_by_id('net.reead.home:id/rl_week').click()
# 按摩提醒-提交 xpath 
def click_rl_add(driver):
    driver.find_element_by_xpath('//[@resourceid="net.reead.home:id/rl_add"]/android.widget.ImageView[1]').click()
# 按摩提醒-取消 xpath  
def click_rl_back(driver):
    driver.find_element_by_xpath('//*[@resource-id="net.reead.home:id/rl_back"]/android.widget.ImageView[1]').click()
# 按摩提醒-选择时间（上午/下午/时/分）（x，y   205，474  445,474  683,474）    xpath  //*[@text="下午"]
def click_select_time(driver):
    pass
# 按摩提醒-选择频次周日 
def click_ll_check_00(driver):
    driver.find_element_by_id('net.reead.home:id/ll_check_00').click()
# 按摩提醒-选择频次周一 
def click_ll_check_01(driver):
    driver.find_element_by_id('net.reead.home:id/ll_check_01').click()
# 按摩提醒-选择频次周日 
def click_ll_check_02(driver):
    driver.find_element_by_id('net.reead.home:id/ll_check_02').click()
# 按摩提醒-选择频次周日 
def click_ll_check_03(driver):
    driver.find_element_by_id('net.reead.home:id/ll_check_03').click()
# 按摩提醒-选择频次周日 
def click_ll_check_04(driver):
    driver.find_element_by_id('net.reead.home:id/ll_check_00').click()
# 按摩提醒-选择频次周日 
def click_ll_check_05(driver):
    driver.find_element_by_id('net.reead.home:id/ll_check_00').click()
# 按摩提醒-选择频次周日 
def click_ll_check_06(driver):
    driver.find_element_by_id('net.reead.home:id/ll_check_00').click()
# 按摩提醒-取消  
def click_tv_cancel(driver):
    driver.find_element_by_id('net.reead.home:id/tv_cancel').click()
# 按摩提醒-确认  
def click_tv_confirm(driver):
    driver.find_element_by_id('net.reead.home:id/tv_cancel').click()
# 按摩提醒-开关  
def click_sb_asr(driver):
    driver.find_element_by_id('net.reead.home:id/sb_asr').click()
# 按摩提醒-第一条  长按
# def click_id_rv(driver):
#     driver.find_element_by_xpath('//*[@resource-id="net.reead.home:id/rv"]/android.widget.RelativeLayout[1]').click()
# 按摩提醒-删除闹钟 xpath 
def click_del_Alarm(driver):
    driver.find_element_by_xpath('//*[@text="删除闹钟"]').click()



