#导入相应的模块
import pygame
from pygame.locals import *
import time,random 

class Explode:
	'''爆炸类'''
	def __init__(self,screen_temp,plane):
		self.screen = screen_temp
		self.images = [pygame.image.load("./images/"+str(i)+".png") for i in range(1,7)]
		self.x = plane.x
		self.y = plane.y

	def display(self):
		for i in range(6):
			self.screen.blit(self.images[i],(self.x,self.y))
			pygame.display.update()
			time.sleep(0.04)
			

class HeroPlane:
	'''玩家飞机（英雄）'''
	def __init__(self,screen_temp):
		self.x = 200
		self.y = 400
		self.screen = screen_temp
		self.image = pygame.image.load("./images/me.png")
		self.bullet_list = [] #用于存放玩家的子弹列表

	def display(self,enemylist):
		'''绘制玩家飞机'''
		#绘制子弹
		for b in self.bullet_list:
			b.display()
			if b.hero_move():
				self.bullet_list.remove(b)
		self.screen.blit(self.image,(self.x,self.y))
		# 遍历所有敌机所有子弹,并执行碰撞检测
		for enemy in enemylist:
			for bo in enemy.bullet_list:
				if bo.x>self.x+12 and bo.x<self.x+94 and bo.y>self.y+14 and bo.y<self.y+56:
					enemy.bullet_list.remove(bo)
					return True
		
	def move_left(self):
		'''左移动飞机'''
		self.x -= 5
		if self.x <= 0:
			self.x=0

	def move_right(self):
		'''右移动飞机'''
		self.x += 5
		if self.x>=406:
			self.x=406

	def fire(self):
		self.bullet_list.append(Bullet(self.screen,self.x,self.y))
		print(len(self.bullet_list))


class Bullet:
	'''子弹类'''
	def __init__(self,screen_temp,x,y):
		self.x = x+53
		self.y = y
		self.screen = screen_temp
		self.image = pygame.image.load("./images/pd.png")

	def display(self):
		'''绘制子弹'''
		self.screen.blit(self.image,(self.x,self.y))
	
	def hero_move(self):
		'''玩家发出子弹的移动'''
		self.y -= 10
		# 如果出了视线范围，移除，防止占用计算机资源
		if self.y <=-20:
			return True

	def enemy_move(self):
		'''敌机子弹的移动'''
		self.y += 10
		# 如果出了视线范围，移除，防止占用计算机资源
		if self.y >=580:
			return True


class EnemyPlane:
	'''敌机类'''
	def __init__(self,screen_temp):
		self.x = random.choice(range(408))
		self.y = -75
		self.screen = screen_temp
		self.image = pygame.image.load("./images/e"+str(random.choice(range(3)))+".png")
		self.bullet_list = [] #用于存放敌机的子弹列表

	def fire(self):
		self.bullet_list.append(Bullet(self.screen,self.x,self.y+75))  #加75，保证子弹是从敌机头部发出，而不是尾部
		print(len(self.bullet_list))

	def display(self):
		'''绘制敌机'''
		#绘制子弹
		for b in self.bullet_list:
			b.display()
			if b.enemy_move():
				self.bullet_list.remove(b)
		self.screen.blit(self.image,(self.x,self.y))
	
	def move(self,hero):
		self.y += 4
		#敌机出屏幕
		if self.y>568:
			return True
		# 遍历所有玩家发出的子弹,并执行碰撞检测
		for bo in hero.bullet_list:
			if bo.x>self.x+12 and bo.x<self.x+92 and bo.y>self.y+20 and bo.y<self.y+60:
				hero.bullet_list.remove(bo)
				return True


def key_control(hero_temp):
	'''键盘控制函数'''
	#执行退出操作
	for event in pygame.event.get():
		if event.type == QUIT:
			print("exit()")
			exit()
	#获取按键信息
	pressed_keys = pygame.key.get_pressed()
	#print(pressed_keys)
	#做判断，并执行对象的操作
	if pressed_keys[K_LEFT] or pressed_keys[K_a]:
		print("Left...")
		hero_temp.move_left()

	elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
		print("Right...")
		hero_temp.move_right()

	if pressed_keys[K_SPACE]:
		print("space...")
		hero_temp.fire()


def main():
	'''主程序函数 '''
	# 创建游戏窗口，
	screen = pygame.display.set_mode((512,568),0,0)

	# 设置窗口标题
	pygame.display.set_caption("飞机大战")

	# 创建一个游戏背景
	background = pygame.image.load("./images/bg2.jpg")

	# 创建玩家飞机（英雄）
	hero = HeroPlane(screen)

	m = -968
	enemylist = [] #存放敌机的列表
	while True:
		#绘制画面
		screen.blit(background,(0,m))
		m+=2
		if m>=-200:
			m = -968

		#绘制玩家飞机
		if hero.display(enemylist):
			#这里添加玩家飞机爆照效果
			#创建爆炸对象
			bomb = Explode(screen,hero)
			bomb.display()
			print("GG! You dead!")
			break;
            
		#执行键盘控制
		key_control(hero)

		#随机绘制敌机
		if random.choice(range(50))==10:
			enemylist.append(EnemyPlane(screen))
		#遍历敌机并绘制移动
		for em in enemylist:
			em.display()
			if random.choice(range(50))==10:
				em.fire()
			if em.move(hero):
				#这里添加敌机爆照效果
				#创建爆炸对象
				bomb = Explode(screen,em)
				bomb.display()
				enemylist.remove(em)

		#更新显示
		pygame.display.update()

		#定时显示
		time.sleep(0.04)


#判断当前是否是主运行程序，并调用
if __name__ == "__main__":
	main()
