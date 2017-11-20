import monster
from random import *
from observe import Observer

#This is a class that instantiates a neighborhood and also creates houses that have 0-10 monsters in each.
#The monsters in the house are also randomly generated and picked. The neighborhood is also created at a 
#random size.

class Neighborhood(object):
	"""Class to neighborhoodafdsjvcasdnfqwpngfqwf"""
	def __init__(self):
		"""Neighborhood Constructor."""
		self.w, self.h = randrange(4, 8), randrange(4, 8)
		
		self.grid = [[0 for x in range(self.h)] for y in range(self.w)]
	
		for i in range (self.h):
			for k in range (self.w):
				self.grid[k][i] = House(k, i, randrange(0,2))

class House(Observer):
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

			elif (monsterChoice == 1):
				temp = monster.Zombie()

			elif (monsterChoice == 2):
				temp = monster.Vampire()

			elif (monsterChoice == 3):
				temp = monster.Ghoul()

			elif (monsterChoice == 4):
				temp = monster.Werewolf()
			
			temp.register(self)
			self.monsters.append(temp)

	def update(self, something):
		print ("YAY")






