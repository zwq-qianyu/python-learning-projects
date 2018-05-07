import pymysql
#保证可以跨平台读取、执行包含中文的代码
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#stu表信息操作类
class stu_operate:
	def __init__(self):
		'''
		构造函数，实现数据库的连接
		'''
		#self.stu = stu
		#打开数据库连接
		self.db = pymysql.connect(host="localhost",user="root", password ="",db="stu",charset="utf8")
		#使用cursor()创建一个游标对象 cursor
		self.cursor = self.db.cursor()

	def findAll(self):
		'''
		这个函数实现数据库的查询
		'''
		sql = "select * from stu"
		try:
			#执行sql操作
			self.cursor.execute(sql)
			#解析结果
			data = self.cursor.fetchall()
			for i in data:
				print(i)
		except Exception as err:
			print("SQL执行错误！原因：",err)

	def delete(self,id):
		'''
		这个函数实现数据库中数据ID为id的删除
		'''
		self.id = id
		sql = "delete from stu where id=%d"%(self.id)
		try:
			#执行sql操作
			m = self.cursor.execute(sql)
			# 事务提交
			self.db.commit()
			print("成功删除条数：",m)
			
		except Exception as err:
			#事务回滚
			self.db.rollback()
			print("SQL执行错误！原因：",err)

	def insert(self,data):
		'''
		这个函数是实现在数据库中添加data数据
		'''
		#定义sql语句
		self.data = data
		sql = "insert into stu(name,age,classid) values('%s','%d','%s')"%(self.data)
		try:
			#执行sql操作
			m = self.cursor.execute(sql)
			# 事务提交
			self.db.commit()
			print("成功添加条数：",m)
			
		except Exception as err:
			#事务回滚
			self.db.rollback()
			print("SQL执行错误！原因：",err)

	def __del__(self):
		'''
		析构函数，实现数据库的关闭
		'''
		self.db.close()


op = stu_operate()
op.findAll()
data = ('zhaoliu',30,'python04')
op.insert(data)
op.findAll()
op.delete(5)
op.findAll()