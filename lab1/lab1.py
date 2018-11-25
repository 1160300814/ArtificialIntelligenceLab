class Monkey:
	position = ''         #猴子的位置
	BoxPosition = 'C'      #箱子的位置
	BananaPosition = 'B'   #香蕉的位置
	state1 = 0            #猴子是否在箱子上，1是在，0是不在
	state2 = 0            #猴子是否拿到香蕉,1是拿到,0是没有拿到
	def __init__(self,p,BoxPosition,BananaPosition):
		self.position = p
		self.BoxPosition = BoxPosition
		self.BananaPosition = BananaPosition
	def Goto(self,y):  #猴子走到y处
		if y == 'A' or y == 'B' or y == 'C':
			self.position = y
			return 1
		else:
			print("输入错误")
			return 0
	def Climbbox(self):      #猴子爬上箱子
		if self.position == self.BoxPosition:     #前提是箱子猴子在一起
			self.state1 = 1
			return 1
		else:
			print("错误！猴子和箱子不在一起")
			return 0
	def Grasp(self):         #猴子抓香蕉
		if self.position == self.BananaPosition and self.state1 == 1:   #前提是猴子在箱子上，在香蕉下面
			self.state2 = 1
			return 1
		elif self.position != self.BananaPosition:
			print("错误！猴子和香蕉不在一起")
		else:
			print("错误！猴子没在箱子上")
		return 0
	def Pushbox(self,y):     #猴子把箱子推到y处
		if (self.position == self.BoxPosition)and(y == 'A' or y == 'B' or y == 'C'):   #前提是箱子猴子在一起
			self.position = y
			self.BoxPosition = y
			return 1
		elif not(y == 'A' or y == 'B' or y == 'C'):
			print("输入错误")
		else:
			print("错误！猴子和箱子不在一起")
		return 0
def main():
	'''start = input("输入猴子的初始状态,例如:A00\n")            #A是猴子的位置，后两个0分别是猴子的状态1,2
	monkey = Monkey(start[0],int(start[1]),int(start[2]))
	print("初始，猴子在"+start[0]+"处，香蕉挂在B处，箱子在C处\n")'''
	monkey = Monkey('A','C','B');
	print("猴子初始在"+monkey.position+"处，香蕉挂在"+monkey.BananaPosition+"处，箱子在"+monkey.BoxPosition+"处");
	if monkey.Goto(monkey.BoxPosition):
		print("猴子走到"+monkey.BoxPosition+"处\n")
		if monkey.Pushbox(monkey.BananaPosition):
			print("猴子把箱子推到"+monkey.BananaPosition+"处\n")
			if monkey.Climbbox():
				print("猴子爬上箱子\n")
				if monkey.Grasp():
					print("猴子成功的摘到了香蕉")
main()