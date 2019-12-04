'''
@Author: your name
@Date: 2019-11-12 18:42:00
@LastEditTime: 2019-11-21 17:39:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\runCase.py
'''

import os
from comm.HTMLTestRunner import HTMLTestReport
import comm.runSet as runSet
import comm.md_config as myConfig
import comm.common as common
from comm.md_logger import myLog
path = os.path.split(os.path.dirname(__file__))[0]
if __name__ == '__main__':
      '''运行之前获取config.ini配置里面的result,0表示result文件夹下面的内容每次运行都保存下来，
      1表示只保存最后一次运行的结果'''
      result = myConfig.getResult()
      if result == 1:
            #截图文件的路径
            imPath = os.path.join(path, 'REEAD_UI','result','image')
            #日志文件的路径
            logPath = os.path.join(path, 'REEAD_UI','result','logs')
            #测试报告的路径
            reportPath = os.path.join(path, 'REEAD_UI','result','report')
            common.delFile(imPath)
            common.delFile(logPath)
            common.delFile(reportPath)
      suite = runSet.set_suite()
      #获取report的存放路径
      filePath = myLog().getReportPath()
      fb = open(filePath, 'wb')
      runner = HTMLTestReport(stream=fb, verbosity=2, title='Rui_Duo', description='Smoke Test/Regression Testing')
      runner.run(suite)
      fb.close()
      myLog.logger().info('测试用例个数 %s', suite.countTestCases())
      #测试邮件发送
      mail = runSet.send_Mail(filePath,'Rui_Duo')
      if mail:
            myLog.logger().info('邮件发送成功!')
      else:
            myLog.logger().info('邮件发送失败!')

























            

'''
                            _ooOoo_
                           o8888888o
                           88" . "88
                           (| -_- |)
                           O\  =  /O
                        ____/`---'\____
                      .'  \\|     |//  `.
                     /  \\|||  :  |||//  \
                    /  _||||| -:- |||||-  \
                    |   | \\\  -  /// |   |
                    | \_|  ''\---/''  |   |
                    \  .-\__  `-`  ___/-. /
                  ___`. .'  /--.--\  `. . __
               ."" '<  `.___\_<|>_/___.'  >'"".
              | | :  `- \`.;`\ _ /`;.`/ - ` : | |
              \  \ `-.   \_ __\ /__ _/   .-` /  /
         ======`-.____`-.___\_____/___.-`____.-'======
                            `=---='
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    佛祖保佑        永无BUG
           佛曰:
                  写字楼里写字间，写字间里程序员；
                  程序人员写程序，又拿程序换酒钱。
                  酒醒只在网上坐，酒醉还来网下眠；
                  酒醉酒醒日复日，网上网下年复年。
                  但愿老死电脑间，不愿鞠躬老板前；
                  奔驰宝马贵者趣，公交自行程序员。
                  别人笑我忒疯癫，我笑自己命太贱；
                  不见满街漂亮妹，哪个归得程序员？
'''



