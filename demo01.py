import random
import urllib
from urllib import request,parse
#urlopen简单发送网络请求
ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"
]
url = "https://www.baidu.com"
header = random.choice(ua_list)
# print(header)
request = urllib.request.Request(url)
request.add_header("User-Agent",header)
#get——header()字符串参数，第一个字母大写，后面的全部小写
request.get_header("Header")

# response = urllib.request.urlopen(request)
# print(response.code)
# html = response.read()
# print(html)




#quote() 主要将中文转化为ascll码
urls = "https://www.baidu.com/s?wd=火影忍者"
url = "https://www.baidu.com/s?wd="
data = parse.quote('火影忍者')
res = url + data
print(res)


# 通过urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受
params = {'name':'冬风诉','pw':'fgmdd537'}
datas = parse.urlencode(params)
print("这是urlencode方法---"+datas)
#parse_qsl是转换成元组格式
# print(parse.parse_qsl(datas))
#通过parse_qs把url编码转回中文字典格式
print(parse.parse_qs(datas))

#unquote()  主要将ascll码转化为中文
print(parse.unquote(res))
print(type(res))
#quote()    将中文转化为ascll码
print(parse.quote(urls))

print(parse.unquote('kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn=50'))
print(parse.quote('kw=英雄联盟&ie=utf-8&pn=50'))


# urllib.error
#异常处理请求
#URLError   error,所有的request异常处理
#HTTPError  URLError子类
#    code：请求状态码     reason:错误的原因    headers：相应的报文头（头信息）

#urllib.robotparse
#Robots（机器人）协议：不是命令，单纯的文件，搜索引擎看的第一个文件

