'''
@Author: your name
@Date: 2019-12-04 10:48:26
@LastEditTime: 2019-12-04 11:57:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\pageElement\setPage.py
'''
# 进入设置
def click_set(driver):
    driver.find_element_by_id('net.reead.home:id/rl_set').click()
# 个人信息 id 
def click_rl_edit_profile(driver):
    driver.find_element_by_id('net.reead.home:id/rl_edit_profile').click()
# 个人信息-男 id 
def click_tv_man(driver):
    driver.find_element_by_id('net.reead.home:id/tv_man').click()
# 个人信息-女 id 
def click_tv_woman(driver):
    driver.find_element_by_id('net.reead.home:id/tv_woman').click()
# 个人信息-昵称 id 
def click_nick_name(driver):
    driver.find_element_by_id('net.reead.home:id/et_nick_name').click()
# 个人信息-生日 id 
def click_tv_birthday(driver):
    driver.find_element_by_id('net.reead.home:id/tv_birthday').click()
# 个人信息-生日-选择年 xpath
def click_year(driver):
    driver.find_element_by_xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]').click()
# 个人信息-生日-选择月 xpath
def click_month(driver):
    driver.find_element_by_xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.View[2]').click()
# 个人信息-生日-选择日 xpat
def click_tv_day(driver):
    driver.find_element_by_xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.View[3]').click()
# 个人信息-生日-选择确认 xpath
# //*[@text="确定"]
# 个人信息-选择身高 xpath  //*[@resource-id="net.reead.home:id/rl_h"]
# 个人信息-选择体重 xpath //android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]/android.widget.RelativeLayout[1]
# 个人信息-确认  id  net.reead.home:id/rl_save
# 昵称清空 position (0.908, 0.341)
# 个人信息-更换头像  id net.reead.home:id/iv_avatarDisplay
# 个人信息-选择头像 xpath  
# //*[@resource-id="net.reead.home:id/rv_photos"]/android.widget.RelativeLayout[2]/android.widget.ImageView[2]
# 个人信息-头像完成  id  net.reead.home:id/done 

# 手机号码 id net.reead.home:id/rl_change_phone
# 手机号码-提交 id net.reead.home:id/tv_bind
# 手机号码-原手机验证码 id net.reead.home:id/et_verify_code_old
# 手机号码-新手机输入框 id net.reead.home:id/et_phone
# 手机号码-新手机验证码 id net.reead.home:id/et_verify_code

# 微信-解绑 id net.reead.home:id/tv_wechatStatus
# 微信-确定id  android:id/button1
# 微信-取消 id  android:id/button2
# 微信-绑定 id  com.huawei.android.internal.app:id/icon  华为

# 意见反馈 id net.reead.home:id/rl_feed_back
# 意见反馈-输入框 classname android.widget.RelativeLayout
# 意见反馈-提交 id net.reead.home:id/tv_commit

# 检测新版本-文字 id net.reead.home:id/tv_version
# 检测新版本-检测 id net.reead.home:id/rl_check_version