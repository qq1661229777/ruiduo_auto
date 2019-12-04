'''
@Author: your name
@Date: 2019-11-22 11:07:04
@LastEditTime: 2019-11-22 11:07:31
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \REEAD_UI\codemsm.py
'''
import flask, json
from flask import request
import os
'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)


# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 接口的路径、请求方式
@server.route('/msg', methods=['get', 'post'])
def msg():
    # 获取通过url请求传参的数据
    msg = request.values.get('msg')
    # 获取url请求传的明文
    print(msg)
    path=os.path.abspath(os.path.dirname(os.getcwd()))
    path=path+"\\data\\yanzhengma.txt"
    f = open(path, 'w')
    f.write(msg)
    f.close()
    if msg:
        resu = {'code': 200, 'message': '成功',"msg":msg}
        return json.dumps(resu, ensure_ascii=False)
    else:
        return  json.dumps({'code': 208, 'message': '失败',"msg":msg}, ensure_ascii=False)

if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问