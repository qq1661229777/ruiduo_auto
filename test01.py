'''
@Author: your name
@Date: 2019-11-12 18:42:00
@LastEditTime: 2019-11-27 10:53:54
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\test01.py
'''
import comm.common as common
loginCase = common.get_excel_value('loginPhone')
print(loginCase[1])
print('------------')
print(loginCase[0])