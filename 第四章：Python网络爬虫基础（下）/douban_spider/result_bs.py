import requests
import time,json
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def getPage(url):
    '''爬取指定url页面'''
    headers = {
        'Referer': 'https://book.douban.com/top250?start=25',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    #执行爬取
    res = requests.get(url,headers = headers)
    if res.status_code == 200:
        return res.text
    else:
        return 0

def parsePage(content):
    '''解析爬取网页中的结果，并返回内容'''
    #初始化，返回一个BeautifulSoup对象
    soup = BeautifulSoup(content,"lxml")
    #解析网页中一部一部的电影信息
    items = soup.find_all(name="table", attrs={'width': '100%'})
    #遍历并解析每部电影
    for item in items:
        yield {
            'pic': item.find(name="img").attrs['src'],
            '电影名': item.select("a")[1].attrs['title'],
            '作者、价格等': item.find(name="p",attrs={'class':'pl'}).string,
            '评分': item.find(name="span",attrs={'class':'rating_nums'}).string,
            '经典语录': item.find(name="span",attrs={'class':'inq'}).string
                }


def writeFile(content,m):
    '''将解析后的信息写入文件中'''
    with open("./result_bs.txt",'a',encoding="utf-8") as f:
        f.write(str(m) + json.dumps(content,ensure_ascii=False) + "\n\n")
    myjson = json.loads(json.dumps(content,ensure_ascii=False))
    imurl = myjson['pic']
    #存储图片
    urlretrieve(imurl,"./mypic_bs/p"+str(m)+".jpg")

def main(offset,m):
    '''主函数，负责爬取一页的内容'''
    url = "https://book.douban.com/top250?start="+str(offset)
    html = getPage(url)
    if html:
            for item in parsePage(html):
                writeFile(item,m)
                m += 1

if __name__ == '__main__':
    m = 1
    for i in range(10):
        main(i,m)
        m += 25
        time.sleep(1)
