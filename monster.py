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
		self.attackStrength = 0
		self.healthPoints = 0

########################################################################
#Child classes of Monster. They Set each monster to its specific type.
########################################################################
class Person(Monster):
	"""A class to store Person Information."""
	def __init__(self):
		"""Person Constructor."""
		super(Person, self).__init__()
		self.attackStrength = -1
		self.healthPoints = 100

class Zombie(Monster):
	"""A class to store Zombie Information."""
	def __init__(self):
		"""Zombie Constructor."""
		super(Zombie, self).__init__()
		self.attackStrength = randrange(10)
		self.healthPoints = randrange(50, 101)
		

class Vampire(Monster):
	"""Class to store Vampire Information."""
	def __init__(self):
		"""Vampire Constructor"""
		super(Vampire, self).__init__()
		self.attackStrength = randrange(10, 21)
		self.healthPoints = randrange(100, 201)

class Ghoul(Monster):
	"""Class to store ghoul information."""
	def __init__(self):
		"""Ghoul Constructor."""
		super(Ghoul, self).__init__()
		self.attackStength = randrange(15, 31)
		self.healthPoints = randrange(40, 81)

class Werewolf(Monster):
	"""Class to store werewolf information."""
	def __init__(self):
		"""Werewolf."""
		super(Werewolf, self).__init__()
		self.attackStrength = randrange(0, 41)
		self.healthPoints = 200
