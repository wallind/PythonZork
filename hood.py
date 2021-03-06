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
		self.posX, self.posY = randrange(0, self.w), randrange(0, self.h)

		self.grid = [[0 for x in range(self.h)] for y in range(self.w)]
	
		for i in range (self.h):
			for k in range (self.w):
				self.grid[k][i] = House(k, i, randrange(0,2))

	#######################################################################
	#Getter method for the monsters
	#######################################################################
	def getMonsters(self):
		return self.grid[self.posX][self.posY].getMonsters()

	#######################################################################
	#Setter method for the flag
	#######################################################################
	def setFlag(self, flag):
		self.grid[self.posX][self.posY].setFlag(flag)

	#######################################################################
	#Getter method for the flag
	#######################################################################
	def getFlag(self):
		return self.grid[self.posX][self.posY].getFlag()

	#######################################################################
	#Changes the postion for the X position on the grid
	#######################################################################	
	def changeXPos(self, xChange):
		if (xChange + self.posX < self.w):
			self.posX = self.posX + xChange
			return True
		return False

	#######################################################################
	#Changes the position for the Y position on the grid
	#######################################################################
	def changeYPos(self, yChange):
		if (yChange + self.posY < self.h):
			self.posY = self.posY + yChange
			return True
		return False

	########################################################################
	#This is the method that shows you where you are at in the neighborhood
	########################################################################
	def show(self):
		output = []
		for i in range (self.h):
			temp = ""
			for k in range(self.w):
				if (self.grid[k][self.h - i - 1].getFlag() == 1):
					temp = temp + " [ "
					if ((self.h - i - 1) == self.posY and k == self.posX):
						temp = temp + "X ] "
					else:
						temp = temp + "  ] "
				elif (self.grid[k][self.h - i - 1].getFlag() == 2):
					temp = temp + " [["

					if ((self.h - i - 1) == self.posY and k == self.posX):
						temp = temp + "X]] "
					else:
						temp = temp + " ]] "


				elif ((self.h - i - 1) == self.posY and k == self.posX):
					temp = temp + "   X   "
				else:
					temp = temp + "       "
			
			output.append(temp)
		return output

	#######################################################################
	#Getter for X position
	#######################################################################
	def getXPos(self):
		return self.posX

	#######################################################################
	#Getter for Y position
	#######################################################################
	def getYPos(self):
		return self.posY

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
	def update(self, alive, index):
		if (not alive):
			self.monsters[index] = monster.Person();


	#######################################################################
	#Getter for the monsters
	#######################################################################
	def getMonsters(self):
		return self.monsters

	#######################################################################
	#Getter flag for the house
	#######################################################################
	def getFlag(self):
		return self.flag

	#######################################################################
	#Setter flag for the house
	#######################################################################
	def setFlag(self, flag):
		self.flag = flag
