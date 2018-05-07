from urllib import request,parse
import json,time,random,hashlib

#post 提交的URL
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


S = 'fanyideskweb'
n = 'hello'
r = str(int(time.time()*1000) + random.randint(1,10))
D = 'rY0D^0\'nM0}g5Mm1z%1G4'

sign = hashlib.md5((S + n + r + D).encode('utf-8')).hexdigest()

# 定义请求的参数，并编码转换
data = {
    'i': 'hello',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': r,
    'sign': sign,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'true'
    }
data = parse.urlencode(data)

#设置hearders头信息
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length':len(data),
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=526407400@59.111.179.141; OUTFOX_SEARCH_USER_ID_NCOO=847303816.8260163; _ga=GA1.2.657009975.1522566068; JSESSIONID=aaa9Ds3WCiZj1fcmgOHmw; fanyi-ad-id=43155; fanyi-ad-closed=1; ___rl__test__cookies=1525280939015',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }

req = request.Request(url,data=bytes(data,encoding="utf-8"),headers=headers)
res = request.urlopen(req)

# 解析结果
str_json = res.read().decode("utf-8")
print(str_json)
myjson = json.loads(str_json)

print(myjson)
