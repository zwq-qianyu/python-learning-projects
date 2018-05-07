from urllib import request,parse
import json,time,random,hashlib

#post 提交的URL
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

r =  "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10)),
u = 'fanyideskweb'
d = 'hello'
f = str(int(time.time()*1000) + random.randint(1,10))
c = 'rY0D^0\'nM0}g5Mm1z%1G4'

sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

# 定义请求的参数，并编码转换
data = {
    'i': 'hello',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': f,
    'sign': sign,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'true'
    }
data = parse.urlencode(data)

#设置hearders头信息
headers={'Content-Length':len(data)}

req = request.Request(url,data=bytes(data,encoding="utf-8"),headers=headers)
res = request.urlopen(req)

# 解析结果
str_json = res.read().decode("utf-8")
print(str_json)
myjson = json.loads(str_json)

print(myjson)
