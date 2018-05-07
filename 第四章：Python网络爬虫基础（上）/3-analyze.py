from urllib import request
import re,os

getinfo = []
for page in range(1,11):  #循环，获取10个页面的数据
	#获取每一页的url
    url = "http://maoyan.com/board/4?offset=" + str(10*(page - 1))
    #封装、打开并获取网页html代码
    req = request.Request(url)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')

    '''
    xuhao = 'board-index-(.*?)">'
    picAndName = '<img data-src="(.*?)" alt="(.*?)" class'
    actor = '主演：(.*?)</p>'
    releasetime = '上映时间：(.*?)</p>'
    score = 'integer">(.*?)</i>.*?>(.*?)</i>'

    xuhaos = re.findall(xuhao,html)
    print(xuhaos)
    picAndNames  = re.findall(picAndName,html)
    for i in picAndNames:
        print(i)
    actors = re.findall(actor,html,re.S)
    for i in actors:
        print(i.strip())
    releasetimes  = re.findall(releasetime,html)
    for i in releasetimes:
        print(i)
    scores  = re.findall(score,html)
    for i in scores:
        print(i[0]+i[1])
    '''
    #正则匹配表达式
    pat = 'board-index-(.*?)">.*?<img data-src="(.*?)" alt="(.*?)" class.*?主演：(.*?)</p>.*?上映时间：(.*?)</p>.*?integer">(.*?)</i><i class="fraction">(.*?)</i>'
    #获取匹配结果
    result = re.findall(pat,html,re.S)
    #将每一页的匹配结果加入到一个列表中，方便后面对数据进行处理
    getinfo += result

filename = 'movie_info.txt'
#在当前目录下创建一个pic目录，用来存放爬取到的图片
os.mkdir('./pic')

#以文件对象的方式打开文件
with open(filename,'w',encoding='utf8') as file_object:
    file_object.write("猫眼电影TOP100电影信息\n\n")
    x = 1   #用来按照电影排名对图片进行命名
    for i in getinfo:
    	'''依次对100条数据进行处理'''
        print(i)
        #将每条数据的信息写入 movie_info.txt 文件
        file_object.write("序号: "+i[0]+"; 电影名称: "+i[2]+"; 主演: "+i[3].strip()+"; 时间: "+i[4].strip()+"; 评分: "+i[5]+i[6]+";\n图片下载地址: "+i[1]+"\n\n")
        pic_url = i[1].strip()   #图片的url
        #根据 url 下载图片并存入指定目录中
        request.urlretrieve(pic_url,'./pic/%s.jpg'%x)
        x += 1
        print('\n')
