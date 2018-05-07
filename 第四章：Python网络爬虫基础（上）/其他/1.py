from urllib import request,error
import re

url = "http://www.csu.edu.cn/"

try:
	res = request.urlopen(url)
	html = res.read().decode("utf-8")
        #'<LI style="width:117px"><A title="(.*?)" href="(.*?)" style="width:117px;">.*?</A> </LI>'
	pat = '<A title="(.*?)" href="(.*?)" style="width:117px;">.*?</A>'
	dlist = re.findall(pat,html)

	for v in dlist:
	    print(v[0]+":"+v[1])
except error.HTTPError as e:
	print(e.reason)
	print(e.code)
except error.URLError as e:
	print(e.reason)
except Exception as e:
	print(e)
