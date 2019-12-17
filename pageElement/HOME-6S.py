'''
@Author: your name
@Date: 2019-12-16 10:25:09
@LastEditTime: 2019-12-17 09:47:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\pageElement\HOME-6S.py
'''
# 开机
def start_up(driver):
    driver.find_element_by_xpath("//*[contains(@text,'开机')]").click()
# 关机
def Shutdown(driver):
    driver.find_element_by_xpath("//*[contains(@text,'关机')]").click()
# 自动模式
def auto_mode(driver):
    driver.find_element_by_xpath("//*[contains(@text,'自动模式')]").click()
# 手动模式
def Manual_mode(driver):
    driver.find_element_by_xpath("//*[contains(@text,'手动模式')]").click()
# 气囊按摩
def Airbag_massage(driver):
    driver.find_element_by_xpath("//*[contains(@text,'气囊按摩')]").click()
# 设置
def set_C(driver):
    driver.find_element_by_xpath("//*[contains(@text,'设置')]").click()

# 自动
def auto_01(driver):
    driver.find_element_by_xpath("//*[contains(@text,'疲劳恢复')]").click()
def auto_02(driver):
    driver.find_element_by_xpath("//*[contains(@text,'颈肩唤醒')]").click()
def auto_03(driver):
    driver.find_element_by_xpath("//*[contains(@text,'腰部护理')]").click()
def auto_04(driver):
    driver.find_element_by_xpath("//*[contains(@text,'经络牵引')]").click()
def auto_05(driver):
    driver.find_element_by_xpath("//*[contains(@text,'智能放松')]").click()
def auto_06(driver):
    driver.find_element_by_xpath("//*[contains(@text,'轻度舒缓')]").click()
def auto_07(driver):
    driver.find_element_by_xpath("//*[contains(@text,'女性专属')]").click()
def auto_08(driver):
    driver.find_element_by_xpath("//*[contains(@text,'温热初始')]").click()
def auto_09(driver):
    driver.find_element_by_xpath("//*[contains(@text,'音乐互动')]").click()
# 手动
def Manual_01(driver):
    driver.find_element_by_xpath("//*[contains(@text,'揉捏')]").click()
def Manual_02(driver):
    driver.find_element_by_xpath("//*[contains(@text,'敲打')]").click()
def Manual_03(driver):
    driver.find_element_by_xpath("//*[contains(@text,'揉敲')]").click()
def Manual_04(driver):
    driver.find_element_by_xpath("//*[contains(@text,'指压')]").click()
def Manual_05(driver):
    driver.find_element_by_xpath("//*[contains(@text,'推拿')]").click()
# 档位调节
def speed_Ad(driver):
    driver.find_element_by_xpath("//*[contains(@text,'速度')]").click()
def amplitude_Ad(driver):
    driver.find_element_by_xpath("//*[contains(@text,'幅度')]").click()
# 气囊部位
def Airbag_01(driver):
    driver.find_element_by_xpath("//*[contains(@text,'气压腿脚')]").click()
def Airbag_02(driver):
    driver.find_element_by_xpath("//*[contains(@text,'气压臀部')]").click()
def Airbag_03(driver):
    driver.find_element_by_xpath("//*[contains(@text,'气压肩部')]").click()
def Airbag_04(driver):
    driver.find_element_by_xpath("//*[contains(@text,'气压手部')]").click()
def Airbag_05(driver):
    driver.find_element_by_xpath("//*[contains(@text,'手动充气')]").click()
def Airbag_06(driver):
    driver.find_element_by_xpath("//*[contains(@text,'气压全身')]").click()
# 气囊调节档位
def Airbag_ld_add(driver):
    driver.find_element_by_xpath('//*[@resource-id="net.reead.home:id/iv_more_func_air_intensity_add"]').click()
def Airbag_ld_cut(driver):
    driver.find_element_by_xpath('//*[@resource-id="net.reead.home:id/iv_more_func_air_intensity_minus"]').click()
# 调节部位
def kb_up(driver):
    driver.find_element_by_xpath("//*[contains(@text,'靠背升')]").click()
def kb_drop(driver):
    driver.find_element_by_xpath("//*[contains(@text,'靠背降')]").click()
def tb_up(driver):
    driver.find_element_by_xpath("//*[contains(@text,'腿部升')]").click()
def tb_drop(driver):
    driver.find_element_by_xpath("//*[contains(@text,'腿部降')]").click()
def hea_up(driver):
    driver.find_element_by_xpath("//*[contains(@text,'加热')]").click()
def fix_po(driver):
    driver.find_element_by_xpath("//*[contains(@text,'定点')]").click()
def tr_a(driver):
    driver.find_element_by_xpath("//*[contains(@text,'腿揉')]").click()
def jg_a(driver):
    driver.find_element_by_xpath("//*[contains(@text,'脚滚')]").click()
def zero_g(driver):
    driver.find_element_by_xpath("//*[contains(@text,'零重力')]").click()


