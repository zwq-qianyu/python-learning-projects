import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def getPage(url):
    '''封装信息并获取网页'''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '__jdu=382066363; 3AB9D23F7A4B3C9B=VEE2HO6UZKFIBTFSUYYVX552WVVB2INOKW3CHSOTTRH6WBS54HGXA3W3WQCAJZMT47L2UVTVVTK6YQS4JHSEKOPOIA; pinId=whSaxOO5VD5QBZzti_3A37V9-x-f3wj7; _jrda=5; TrackID=1BvrgAUkQDi1DWj4DPXGnuIcVPExrYDupXjqBRhgs_m7-9U4IsmV5MiPtlDvWYIvYkit68xaj9oJ_z_SW5HrPnUJlclRtMWGURNSK0vsYOCGnsaTgWFMnQvL1iTfXMClN; __jda=122270672.382066363.1515181334.1524381525.1526211143.9; __jdc=122270672; __jdv=122270672|direct|-|none|-|1526211142755; PCSYCityID=1482; shshshfp=ed9f57f524cf17685061740791105583; shshshfpa=b69cfb1c-8081-194b-119f-04ec60977eab-1526211162; shshshfpb=21674bb78f42748809eb10d47a7c5da8a5af8225a5e7834817074380d7; user-key=131e5fb5-7337-4828-9600-41a359b46e50; cart-main=xx; ipLoc-djd=1-72-2819-0; cn=4; cd=0; shshshsID=77dd37cf34033d464f69e358f8c52269_18_1526212038627; __jdb=122270672.33.382066363|9.1526211143',
        'Host': 'cart.jd.com',
        'Referer': 'https://cart.jd.com/addToCart.html?rcd=1&pid=27078239860&pc=1&eb=1&rid=1526212029602&em=',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    #抓取信息
    res = requests.get(url,headers=headers)
    #获取响应内容
    html = res.content.decode('utf-8')
    return html

def parsePage(html):
    '''解析网页'''
    #设置一个空集合，用来存放数据
    content = []
    # 创建解析器
    soup = BeautifulSoup(html,"lxml")
    #找到所有需要的物品
    items = soup.find_all(name="div",attrs={'class':'goods-item'})
    #遍历所有物品，并对其解析获取所需数据
    for item in items:
        result = {}
        result['data'] = item.find(name="img").attrs['alt']
        result['img'] = item.find(name="img").attrs['src']
        content.append(result)
    return content

def writeFile(content):
    '''将内容写入到文件中'''
    with open("./jingdong_result.txt",'a',encoding='utf-8') as f:
        m = 1
        for i in content:
            print(i)
            f.write("data: " + i['data'] + "\n" + "img: " + i['img'] + "\n\n")
            imurl = "https:" + i['img']
            #save the picture
            urlretrieve(imurl,"./mypic_jingdong/p"+str(m)+".jpg")
            m += 1

def main():
    '''主函数'''
    url = "https://cart.jd.com/cart.action"
    html = getPage(url)
    content = parsePage(html)
    writeFile(content)

if __name__ == '__main__':
    main()
