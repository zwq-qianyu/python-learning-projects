#urllib-version
from urllib import request
import re
def paqu58(i):
    url = "http://wh.58.com/chuzu/pn"+i+"/?PGTID=0d3090a7-0009-ec1a-9b66-5f003c5a2533&ClickID=1"

    req = request.Request(url)
    res = request.urlopen(req)

    html = res.read().decode('utf-8')

    #print(html)

    print("paquzhong...")
    '''
    pic = 'lazy_src="(.*?)"'
    name = 'fcpc_zflist_gzcount.*?>(.*?)|(.*?)</a>.*?'
    huxing = '"room">(.*?)&nbsp;'
    money = '"money">.*?<b>(.*?)</b>元'
    '''
    #分析这类数据时，先分析单个的信息的正则表达式，然后将所有需要爬取的信息按照顺序连接好即可
    pat = 'lazy_src="(.*?)".*?fcpc_zflist_gzcount.*?>(.*?)</a>.*?"room">(.*?)&nbsp;.*?"money">.*?<b>(.*?)</b>元'

    #pics = re.findall(pic,html,re.S)
    #names = []
    #oldnames = re.findall(name,html,re.S)
    #huxings = re.findall(huxing,html,re.S)
    #moneys = re.findall(money,html,re.S)

    res = re.findall(pat,html,re.S)
    '''
    for name in oldnames:
        #print(name)
        if '|' in name:
            names.append(name)
    '''


    for r in list(res):
        print("图片地址: "+r[0])
        print("标题: "+r[1].strip())
        print("户型: "+r[2])
        print("价格: "+r[3]+"元")
        print("\n")
        

def main():
    i = input("Please input the page you want to get info: ")
    paqu58(i)

if __name__ == "__main__":
    main()
