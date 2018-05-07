'''
自动存取款机模拟

默认输入正确（常规），不会出现该输入数字时输入字母
'''

#实现代码中中文可读
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#定义一个字典列表，用来存放用户数据
usrs = [
	{"id":"1","name":"Alice","password":"123456","balance":"1200000"},
	{"id":"2","name":"Bob","password":"123456","balance":"300000"},
	{"id":"3","name":"Taylor","password":"987654","balance":"1314000"},
	{"id":"4","name":"Eric","password":"987654","balance":"9865000"}]

print("\n\n"," "*12,"自动存取款机模拟"," "*12,"\n")
while True:
	#登陆界面及用户登陆操作
	print("="*18,"登录","="*18)
	name = input("请输入你的用户名：")
	if name == "q":
		print(" "*11,"\n你已退出自动存取款机"," "*11)
		break
	for usr in usrs:
		if name in usr.values():
			passwd = input("请输入你的密码：")
			if passwd in usr.values():
				print("="*16,"欢迎登陆","="*16)
				print("你的用户名：",name,"\n")
				break
			else:
				print("\n            密码错误！\n")
	else:
		print("\n此用户不存在，请检查你的输入后重新输入!\n     （ 输入q结束该系统 ）")
		print("")
		continue

	#用户正确后打印操作界面
	while True:
		#打印主页面
		print("{:10} {:9} {:8}".format(" ","1.存钱","2.取钱"))
		print("{:10} {:8} {:8}".format(" ","3.查询余额","4.退出"))
		print("-"*42)
		key = input("请选择你想进行的操作：")
		#对输入进行判断
		if key=="1":
			print("="*18,"存钱","="*18)
			print("你的余额：",usr["balance"],"\n")
			inc = input("请输入你要存入的金额大小：")
			usr["balance"] = str(int(usr["balance"])+int(inc))
			print("你的余额：",usr["balance"],"\n")
			input("按任意键继续...")
		elif key=="2":
			print("="*18,"取钱","="*18)
			print("你的余额：",usr["balance"],"\n")
			dec = int(input("请输入你要取出的金额大小："))
			balan = int(usr["balance"])
			if dec > balan or dec < 0:
				print(" "*12,"余额不足！")
			else:
				usr["balance"] = str(balan-dec)
				print("你的余额：",usr["balance"],"\n")
			input("按任意键继续...")
		elif key=="3":
			print("="*16,"查询余额","="*16)
			print("你的余额：",usr["balance"],"\n")
			input("按任意键继续...")
		elif key=="4":
			print("="*12,"你已退出个人系统","="*12,"\n\n")
			break
		else:
			print("="*13,"无效的键盘输入","="*13)
