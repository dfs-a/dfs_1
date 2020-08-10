import urllib3
from urllib.parse import urlencode
import json
#路径
http = urllib3.PoolManager()
url = "https://fanyi.baidu.com/v2transapi?"
Method = "POST"

hearder = {
    "referer":"https://fanyi.baidu.com/?aldtype=16047",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "cookie":"BIDUPSID=2E35B113A58DF790E42FB20527CB5A49; PSTM=1595998023; BAIDUID=2E35B113A58DF7901571E9FDA7D2A714:FG=1; cflag=13%3A3; delPer=0; PSINO=6; H_PS_PSSID=32288_1452_31669_32357_32327_31253_32350_32046_32394_32429_32117_26350_31639; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1596544389; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=21d8686378fb89cdaea2804a342b271e44308c5b_1596548627_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1596549009; __yjsv5_shitong=1.0_7_eecbbcdd0290338995e5337b03965570f292_300_1596549010173_14.104.115.250_fb03c169"
}
#请求头
#content_type = Content-Type: application/json; charset=utf-8
#Referer: http://fanyi.youdao.com/?keyfrom=dict2.top
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36

#提交数据
#smartresult: dict
#smartresult: rule
query_data = {
    "from":"zh",
    "to":"en"
}
quer = input("请输入你要查询的字词:")
form_data = {
    "from": "zh",
    "to": "en",
    "query": quer,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "416604.178285",
    "token": "18afa28302b15503eb967075dffe3031",
    "domain": "common"
}
# from: zh
# to: en
# query: 我爱你
# transtype: realtime
# simple_means_flag: 3
# sign: 47194.285547
# token: 18afa28302b15503eb967075dffe3031
# domain: common

req_data = urlencode(query_data)
newurl = ''.join([url,req_data])
print(newurl)
response = http.request(
    method = Method,
    url=newurl,
    headers=hearder,
    fields=form_data
)
# print(json.loads(response.data.decode('utf-8')))
result = json.loads(response.data.decode('utf-8'))
# print(result)
for data in result['trans_result']['data']:
    print(data['dst'])

