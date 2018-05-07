import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#初始化学员信息的列表
student = [
	{'name':'zhangsan','age':20,'classid':'python02'},
	{'name':'lisi','age':22,'classid':'python03'},
	{'name':'wangwu','age':25,'classid':'python04'}]

def show_stu(student):
	'''
	这个函数实现学员信息输出
	'''
	if len(student)==0:
		print("========== 没有学员信息可以输出！============")
		return
	print("|{:5}|{:10}|{:5}|{:10}|".format("sid","name","age","classid"))
	print("-"*40)
	for i in range(len(student)):
		print("|{:5}|{:10}|{:5}|{:10}|".format(i+1,student[i]["name"],student[i]["age"],student[i]["classid"]))


#实现初始化界面
while True:
	print("="*20,"初始化界面","="*20)
	print("{:14} {:14}".format("1.查看学员信息","2.添加学院信息"))
	print("{:14} {:14}".format("3.删除学员信息","4.退出系统"))
	key = input("请输入你的选择：")
	if key=='1':
		print("="*20,"学员信息浏览","="*20)
		show_stu(student)
		input("按回车键继续：")
	elif key=='2':
		print("="*20,"学员信息添加","="*20)
		stu={}
		stu["name"] = input("请输入要添加的姓名：")
		stu['age']=input("请输入要添加的年龄：")
		stu['classid']=input("请输入要添加的班级号：")
		student.append(stu)
		show_stu(student)
		input("按回车键继续：")
	elif key=='3':
		print("="*20,"学员信息删除","="*20)
		showStu(stulist)
		sid = input("请输入你要删除的信息id号：")
		del stulist[int(sid)-1]
		showStu(stulist)
		input("按回车键继续：")
	elif key=='4':
		print("="*20,"你已退出系统","="*20)
		break
	else:
		print("="*20,"无效的输入","="*20)

