import monster
from random import *
from observe import Observer


##########################################################################
##This is a class that instantiates a neighborhood and also creates houses 
#that have 0-10 monsters in each. The monsters in the house are also 
#randomly generated and picked. The neighborhood is also created at a 
#random size.
##########################################################################
class Neighborhood(object):
	def __init__(self):
		self.w, self.h = randrange(4, 8), randrange(4, 8)
		
		self.grid = [[0 for x in range(self.h)] for y in range(self.w)]
	
		for i in range (self.h):
			for k in range (self.w):
				self.grid[k][i] = House(k, i, randrange(0,2))

##########################################################################
#This is the house class that inherits Observer. The house class is 
#responsible for creating up to 10 monsters inside of it and randomizing
#as well what kinds of monsters are generated. The house also Observes
#the monsters within it and is notified and then updated if the monster
#inside it dies.
##########################################################################
class House(Observer):
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


	##########################################################################
	#Helper method used to notify the house if a monster dies and then update
	#the house by then removing the monster from it and turning it into a 
	#person.
	##########################################################################
	def update(self, something):
		print ("YAY")






