from urllib import parse,request
from random import choice
#定义数据写入文件函数
def writefile(data,filename):
    with open(filename,'w',encoding='utf-8') as e:
        e.write(data)
        print(filename,'------保存成功')



if __name__ == '__main__':
    kw = input("请输入需要爬取的贴吧名:")
    startpage = int(input("请输入爬取的起始页:"))
    endpage = int(input("请输入爬取页面的结束页:"))
    url = "https://tieba.baidu.com/f?"
    #这里的endpage加一是因为包左不包右原则，这里如果不加一便会少爬取一页
    for page in range(startpage,endpage+1):
        #路径参数
        pn = (page - 1) * 50
        params = {'kw':kw,'ie':'utf-8','pn':pn}
        value = parse.urlencode(params)
        #将网址拼接起来
        urls = ''.join([url,value])
        #浏览器头部信息
        ua_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"
        ]
        header = choice(ua_list)
        #请求数据
        requests = request.Request(urls)
        requests.add_header('User-Agent',header)
        requests.get_header('Header')
        response = request.urlopen(requests)
        #爬取到的页面需要解码
        data = response.read().decode()
        pages = '%s.txt' %page
        writefile(data,pages)
        # print(data)