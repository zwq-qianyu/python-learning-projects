def mycopy(file1,file2):
	'''
	这是一个文本复制函数
	'''
	f1 = open(file1,"rb")
	f2 = open(file2,"wb")
	content = f1.readline()
	while len(content)>0:
		f2.write(content)
		content = f1.readline()
	f1.close()
	f2.close()

mycopy("./k.png","./k_copy.png")

'''
f = open("./a.txt","w")
a = ["Hello World!\n","Hello HTML!\n","Hello PHP!\n"]
f.writelines(a)
'''
# mycopy("./a.txt","./a_copy.txt")