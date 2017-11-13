import monster
from random import *

class Neighborhood(object):
	"""Class to neighborhoodafdsjvcasdnfqwpngfqwf"""
	def __init__(self):
		"""Neighborhood Constructor."""
		self.w, self.h = randrange(2, 6), randrange(2, 6)
		
		self.grid = [[0 for x in range(self.w)] for y in range(self.h)]
		
		for i in range (self.w):
			for k in range (self.h):
				houseOrNah = randrange(0, 2)
				if (houseOrNah == 1):
					self.grid[k][i] = House()

class House(object):
	"""Hpusefegfqeqwefqwef."""
	def __init__(self):
		self.monsters = []
		numMonsters = randrange(0, 11)
		
		#print (numMonsters)
		
		for i in range (numMonsters):
			monsterChoice = randrange(0, 5)
			
			#print (monsterChoice)
			
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
