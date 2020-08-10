#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 20:02
# @Author  : Aquarius
# @File    : demo02.py
# @Software: PyCharm

# urllib3
# 安装模块: pip install urllib3

import urllib3

# 构建请求 ：连接池、线程安全
http = urllib3.PoolManager()
# 发送请求
# r_get = http.request('GET','https://www.baidu.com/')
# r_post = http.request('POST','https://httpbin.org/post',fields={'username':'hello'})
# 属性
# print(r_get.status) # 200
# print(r_get.data)  # 正文
# print(r_get.headers) # 请求头

# POST 解析json数据
import json

r = http.request('GET','http://httpbin.org/ip')
# 1、二进制数据
data = r.data
print(json.loads(data.decode('utf-8')))
# 所有的数据都可以：文本（评论、小说、新闻、数字。。。。），图片，视频，音乐，代码
# 大量数据解析
r = http.request('GET','http://httpbin.org/bytes/1024',preload_content=False)
# 响应：返回数据（json、html、图片/视频（流数据））
# stream数据流形式接收
for data in r.stream(5):
    print(data)

# 当作文件对象来处理   文本（评论、小说、新闻、数字。。。。）
for data in r:
    print(data)

# 2、IP 代理   10000 资源调度   代理池 + 多线程     py文件 数据库  return ip:port
proxy_pool1 = [
    {'http':'','https':''},
]
proxy_pool2 = [
    {'ip':'113.128.27.1','port':'9999'},
    {'ip':'113.128.27.1','port':'8888'}
]
proxy = urllib3.ProxyManager('http://113.128.27.1:9999')

res = proxy.request('GET','http://httpbin.org/ip')
print(res.data)

# 3、headers     headers池 + 随机提取
r = http.request('GET','http://httpbin.org/headers',headers={'key':'value'})
print(json.loads(r.data.decode('utf-8')))

# 4、get 参数
r1 = http.request('GET','http://httpbin.org/get',fields={'wd':'王者荣耀','pn':'50'})
# http://httpbin.org/get?wd=王者荣耀
print(json.loads(r1.data.decode('utf-8')))

# 5、post 参数   Query parameters
# url 进行中文转换成二进制
from urllib.parse import urlencode
post_data = urlencode({'name':'穿山乙'})
url = 'http://httpbin.org/post?' + post_data
r = http.request('POST',url)

print(json.loads(r.data.decode('utf-8')))

# 6、put/post   form data参数提交   账号密码/
r5 = http.request('POST','http://httpbin.org/post',fields={'wd':'王者荣耀','pn':'50'}) # args
print(json.loads(r5.data.decode('utf-8')))

# 7、发送 json 数据
# 请求头：content-type:application/json
data = {'name':'Hi','age':'20'}
# 数据进行转化json字符串
#json.dumps()----将Python的字典数据转换成json字符
#json.loads()----将json字符串数据转换为字典或列表
#json.load()读取文件信息
#json.dump()是写入文件
json_data = json.dumps(data).encode('utf-8')
r2 = http.request("POST",
                  "http://httpbin.org/post",
                  body=json_data,
                  headers={'Content-type':'application/json'}
                  )
print(json.loads(r2.data.decode('utf-8')))  # 提交到 data

# 8、文件提交    fields
with open('test.txt',encoding='utf-8') as fp:
    file = fp.read()
r3 = http.request("POST",
                  "http://httpbin.org/post",
                  fields={
                      'filefield':('test.txt',file)
                  })

# print(json.loads(r3.data.decode('utf-8')))  # 'files'

# 9、纯二进制数据（图片/视频/音乐）    返回值存放data
with open('b.png','rb') as fp:
    img_file = fp.read()
r4 = http.request(
    "POST",
    "http://httpbin.org/post",
    body=img_file,
    headers={'Content-type':'image/jpeg'}
)
print(json.loads(r4.data.decode('utf-8')))


