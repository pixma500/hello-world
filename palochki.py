import random
import itertools
import sys

SITY=['Киев','Минск','Варшава','Иерусалим']
COUNTRE=['Украины','Белорусии','Польши','Израиля']
vopros=dict(zip(COUNTRE,SITY))
comp='Компьютер'
kol=random.randint(15,25)

class Player():

	def __init__(self,name):
		self.name=name
		print(f'Приветствую тебя {self.name}')
		print(f'Играем {kol}  палочками')
		print("Кто берет последнюю, тот победил")
		self.per_hod()
		
	def per_hod(self):
		print('Разыграем первый ход \n')
		s=random.choice(list(vopros.keys()))
		d=input(f'Введите столицу {s} ---').title()
		if vopros[s]==d:
			print(f'Правильно. Начинает {self.name}')
			d=(self.name,comp)
			return Game(d)
		else:
			print('Неправильно!!!')
			d=(comp,self.name)
			return Game(d)
		
class Game():
	def __init__(self,d):
		self.d=d
		self.s=kol
		for player in itertools.cycle(self.d):
			if player == comp:
				Game.hod_comp(self,player)
			else:
				Game.hod_chel(self,player)
            
	def hod_chel(self,player):
		self.player=player
		print('{} ходит'.format(player))
		while True:
			nl=input('Сколько берем -')
			try:
				n= int(nl)
				if not  (1<=n<=3 and n==int(nl)):
					raise ValueError()
			except ValueError as ex:
				print('неверные данные')
			else:
				self.s-=n
				print(f'осталось {self.s}')
				if self.s==0:
					print(f' {player} забрал последнюю и победил!!!!!')
					vi()
				return 
		
	def hod_comp(self,player):
		self.player=player
		print('Ходит {} '.format(player))
		if self.s%4==0:
			n=random.randint(1,2)
			print(f'Взял {n}')
			self.s-=n
			print(f'Осталось {self.s} палочек ','| '*self.s)
			print()
		else:
			n=self.s%4
			print(f'Взял {n}')
			self.s-=n
			print(f'Осталось {self.s} палочек ','|'*self.s)
			print()
		if self.s==0:
			print(f'Победил {player} ')
			vi()	

def main():
	global name
	name=input('Введите ваше имя ').title()
	name=Player(name)
def vi():
	print("Для выхода нажмите 'n',для продолжение любую кнопку")
	command = input()
	while command not in ['n']:
		Player(name)
	sys.exit()
main()
