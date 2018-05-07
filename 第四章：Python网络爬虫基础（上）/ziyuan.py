from urllib import request
import re

url = "https://gitee.com/wizardforcel/w3school"

req = request.Request(url)
res = request.urlopen(req)
html = res.read().decode("utf-8")

pat = '<h2>&#x000A;<a id=".*?" class="anchor" href=".*?"></a>(.*?)</h2>&#x000A;<ul class="task-list">&#x000A;<li>最后更新：(.*?)</li>&#x000A;<li>在线浏览&#x000A;<ul class="task-list">&#x000A;<li><a href="(.*?)">(.*?)</a></li>&#x000A;</ul>&#x000A;</li>&#x000A;<li>PDF版&#x000A;<ul class="task-list">&#x000A;<li><a href="(.*?)">下载地址一</a></li>&#x000A;<li><a href="(.*?)">下载地址二</a></li>&#x000A;<li><a href="(.*?)">下载地址三</a></li>&#x000A;</ul>&#x000A;</li>&#x000A;</ul>&#x000A;'
dlist = re.findall(pat,html)

for v in dlist:
    print(v[0])
    print(v[3]+":"+v[2])
    print("download1: "+v[4])
    print("download2: "+v[5])
    print("download3: "+v[6])
    #print(v)
    print("\n")
