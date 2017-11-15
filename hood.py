import monster
from random import *

class Neighborhood(object):
	"""Class to neighborhoodafdsjvcasdnfqwpngfqwf"""
	def __init__(self):
		"""Neighborhood Constructor."""
		self.w, self.h = randrange(3, 7), randrange(3, 7)
		
		self.grid = [[0 for x in range(self.w)] for y in range(self.h)]
		
		for i in range (self.w):
			for k in range (self.h):
				self.grid[k][i] = House(i, k, randrange(0,2))

class House(object):
	"""Hpusefegfqeqwefqwef."""
	def __init__(self, x, y, flag):
		self.flag = flag		

		self.x = x
		self.y = y
		self.monsters = []
		numMonsters = randrange(0, 11)
		
		for i in range (numMonsters):
			monsterChoice = randrange(0, 5)
			
			if (monsterChoice == 0):
				temp = monster.Person()
				self.monsters.append(temp)

			elif (monsterChoice == 1):
				temp = monster.Zombie()
				self.monsters.append(temp)

			elif (monsterChoice == 2):
				temp = monster.Vampire()
				self.monsters.append(temp)

			elif (monsterChoice == 3):
				temp = monster.Ghoul()
				self.monsters.append(temp)

			elif (monsterChoice == 4):
				temp = monster.Werewolf()
				self.monsters.append(temp)
