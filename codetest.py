'''
@Author: your name
@Date: 2019-11-18 17:02:29
@LastEditTime: 2019-11-21 09:40:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\codetest.py
'''

import time
from appium import webdriver

desired_caps = { }
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '127.0.0.1:4723'
# desired_caps['unicodeKeyboard']= "True"#使用unicode输入法
# desired_caps['resetKeyboard']= "True"#重置输入法到初始状态
desired_caps['noReset'] = "True"  # 启动app时不要清除app里的原有的数据
desired_caps['appPackage'] = 'com.reead.dealer'
desired_caps['appActivity'] = 'com.reead.dealer.MainActivity'
desired_caps['newCommandTimeout'] = '600'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
print('test_something click ------ ')
X = driver.get_window_size()['width']
Y = driver.get_window_size()['height']
print(X,Y)
driver.find_element_by_xpath('//*[@text="18874862102"]').click()
driver.find_element_by_xpath('//*[@resource-id="android:id/content"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]').click()
driver.find_element_by_xpath('//*[@text="请输入账号"]').send_keys (18874862102)
time.sleep(2)
print('输入密码')
driver.find_element_by_link_text('请输入密码').click()
driver.find_element_by_link_text('请输入密码').send_keys (123456)

driver.find_element_by_xpath('//*[@text="登录"]').click()
driver.save_screenshot('123.png')



