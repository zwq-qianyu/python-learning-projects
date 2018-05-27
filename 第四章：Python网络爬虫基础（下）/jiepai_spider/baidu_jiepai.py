#爬取百度“街拍”图片
import requests
import re

def getPic(m):

    headers = {
        'Accept': 'text/plain, */*; q=0.01',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': 'BDqhfp=%E8%A1%97%E6%8B%8D%26%260-10-1undefined%26%260%26%261; PSTM=1516725201; uc_login_unique=f898075f5ac3518a5f88b03176cb95c2; uc_recom_mark=cmVjb21tYXJrXzI1MTY4NDY3; pgv_pvi=8438014976; FP_UID=07a7fad0bcb2397681eb8629e93e3bbf; BDUSS=RXRXBnfjZ-UE9BTE1lT2g0a250fjAwTGp5WlF4WXlWS3NHd3JnNzRTV1VPZmxhQVFBQUFBJCQAAAAAAAAAAAEAAAALg8Wx6PfS3eW3MgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJSs0VqUrNFaYm; __cfduid=d7b5314e4dcdd57f9ab29063e8e3d1edb1525186956; locale=zh; cflag=13%3A3; BAIDUID=68B7A1A6C26F1B9EF2F671F6A7D982EF:FG=1; BIDUPSID=9AE65AFBA0C82DBF5A4E273B95AC28EE; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=null; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E8%A1%97%E6%8B%8D%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm',
        'Host': 'image.baidu.com',
        'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%A1%97%E6%8B%8D&oq=%E8%A1%97%E6%8B%8D&rsp=-1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }

    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%97%E6%8B%8D&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E8%A1%97%E6%8B%8D&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn="+str(m)+"&rn=30&gsm=1e&1526217119597="

    res =requests.get(url,headers=headers)

    html = res.text

    pat = '"ObjURL":"(.*?)jpg"'

    items = re.findall(pat,html,re.S)   #re.S,可以解决获取的东西跨行的问题
    
    for v in items:
        v = v + "jpg"
        a = v.split('\\')
        v = a[0]
        for i in a:
            v = v + i
        v = v.split(":")[1] + ":" + v.split(":")[2]
        #v = "http://" + v
        if "imgtn" in v:    #将部分不可加载图片的链接去掉
            print(v)
            head = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                #'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Host': 'img4.imgtn.bdimg.com',
                'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT',
                'If-None-Match': '99c2e9536873d1fad17baafed32a7b5e',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
                }
            try:
                response = requests.get(v,headers=head)
                if m != 0:  #将第一章图片去掉---无法加载
                    with open("./baidu_pic/p"+str(m)+".jpg", 'wb') as f:
                        f.write(response.content)
                        f.flush()
                m += 1
            except Exception as err:
                print(err)
            
def main():
    for i in range(5):     #爬取5页的图片
        getPic(30*i)
        

if __name__ == "__main__":
    main()


