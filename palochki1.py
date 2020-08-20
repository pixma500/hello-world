import random
import itertools


def take_coins(coins):
	while True:
		raw_coins = input('возьмите палочки[{},{} или {}]'.format(1,2,3))
		try:
			coins = int(raw_coins)
			if not 1 <= coins <= 3:
				raise ValueError()
		except ValueError as ex:
			print('неверные данные')
		else:
			return coins

def game(coins, players,l):
	players = random.sample(players, len(players))
	print(f'Играем {coins} палочками')
	for player in itertools.cycle(players):
			print('{} ходит'.format(player))
			if player=='Комп':
				if l==1:
					coins=take_comp1(coins)
				else:
					coins=take_comp2(coins)
			else:
				coins -= take_coins(coins)
			print()
			print('осталось {} палочек'.format(coins))
			if coins == 0:
				print('игрок {} выиграл'.format(player))
				break
			
def take_comp2(coins):
	if coins%4==0:
		c=int(random.randint(1,2))
	else:
		c=int(coins%4)
	print(f'Комп берет {c} палочек')
	coins-=c
	return coins
	
def take_comp1(coins):
	if coins<10:
		if coins%4==0:
			c=int(random.randint(1,2))
		else:
			c=int(coins%4)
	else:
		c=int(random.randint(1,3))
	print(f'Комп берет {c} палочек')
	coins-=c
	return coins


if __name__ == '__main__':
	n=input('Введите имя ').title()
	l=int(input('Уровень 1.легкий, 2.трудный'))
	game(coins=random.randint(15,25), players=[n, 'Комп'],l=l)

