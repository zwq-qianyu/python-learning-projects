#函数外定义的叫做全局变量
name = "ziyichen"
def fun():
	global name
	print("inner input the global variable: ",name)
	name = "qianyu"

fun()
print("outer input the global variable: ",name)