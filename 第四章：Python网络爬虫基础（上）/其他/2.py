import urllib.request
import re

url = "http://news.baidu.com/"
#伪装浏览器用户
headers = {'User-Agent':'User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
req = urllib.request.Request(url,headers=headers)

#执行请求获取响应信息
res = urllib.request.urlopen(req)

# 从响应对象中读取信息并解码
html = res.read().decode("utf-8")

#print(len(html))
#使用正则解析出新闻标题信息
pat = '<a href="(.*?)" .*? target="_blank">(.*?)</a>'
dlist = re.findall(pat,html)

# 遍历输出结果
for v in dlist:
    print(v)
    #print(v[1]+":"+v[0])
