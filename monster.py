from random import *
from observe import Observable

########################################################################
#This is the monster class that creates each monster individually, sets 
#their health, and their attack strength at random.
########################################################################
class Monster(Observable):
	"""A class to store Monster Information."""
	def __init__(self):
		"""Monster Constructor."""
		Observable.__init__(self)
		self.attackRange = []
		self.healthPoints = 0
	########################################################################
	#This is the get attacked method which checks to see if the monster is 
	#of a certain type and can be attacked by a specific weapon. If it can
	#then its health is deducted by the attack value multiplied by the 
	#weapons attack modifier.
	########################################################################
	def getAttacked(self, weapon, attackVal):
		if (weapon.weaponType == 'SourStraws'):
			if (type(self) is Zombie):
				self.healthPoints = self.healthPoints - (2 * weapon.modifier * attackVal)
			elif (type(self) is Werewolf):
				return	
			else:
				self.healthPoints = self.healthPoints - (weapon.modifier * attackVal)
		
		if (weapon.weaponType == 'HersheyKisses'):
			self.healthPoints = self.healthPoints - (weapon.modifier * attackVal)

		if (weapon.weaponType == 'ChocolateBars'):
			if (type(self) is Zombie or type(self) is Werewolf):
				return
			else:
				self.healthPoints = self.healthPoints - (weapon.modifier * attackVal)

		if (weapon.weaponType == 'NerdBombs'):
			if (type(self) is Ghoul):
				self.healthPoints = self.healthPoints - (5 * weapon.modifier * attackVal)
			else:
				self.healthPoints = self.healthPoints - (weapon.modifier * attackVal)


########################################################################
#Child classes of Monster. They Set each monster to its specific type.
########################################################################
class Person(Monster):
	"""A class to store Person Information."""
	def __init__(self):
		"""Person Constructor."""
		super(Person, self).__init__()
		self.attackRange = [-1, -1]
		self.healthPoints = 100

class Zombie(Monster):
	"""A class to store Zombie Information."""
	def __init__(self):
		"""Zombie Constructor."""
		super(Zombie, self).__init__()
		self.attackRange = [0, 11]
		self.healthPoints = randrange(50, 101)
		

class Vampire(Monster):
	"""Class to store Vampire Information."""
	def __init__(self):
		"""Vampire Constructor"""
		super(Vampire, self).__init__()
		self.attackRange = [10, 21]
		self.healthPoints = randrange(100, 201)

class Ghoul(Monster):
	"""Class to store ghoul information."""
	def __init__(self):
		"""Ghoul Constructor."""
		super(Ghoul, self).__init__()
		self.attackRange = [15, 31]
		self.healthPoints = randrange(40, 81)

class Werewolf(Monster):
	"""Class to store werewolf information."""
	def __init__(self):
		"""Werewolf."""
		super(Werewolf, self).__init__()
		self.attackRange = [0, 41]
		self.healthPoints = 200
