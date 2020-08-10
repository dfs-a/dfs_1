from urllib.parse import urlencode, quote
from urllib.request import *
from urllib import parse
import json
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"#路径中的“_o”去掉，不然爬取不到
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
while True:
    cont = input("请输入你要查询的词典:")

    data = {
        "i": cont,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15965500158090",
        "sign": "c0e49711efcf0562eaf325bd0cb1d13b",
        "ts": "1596550015809",
        "bv": "7b07590bbf1761eedb1ff6dbfac3c1f0",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }

    rsp = Request(url,data=urlencode(data).encode(),headers=header)
    #urlopen打开一个路径
    response = urlopen(rsp)
    #decode() 方法以 encoding 指定的编码格式解码字符串。默认编码为字符串编码。
    content = response.read().decode()

    da = quote(content)
    da1 = json.loads(parse.unquote(da))
    #dumps是将dict转化成str格式，loads是将str转化成dict格式。
    # print(type(da1))
    da2 = json.dumps(da1['translateResult'][0][0]['tgt'])
    print('{}{}{}'.format(cont,'----->',da2))




