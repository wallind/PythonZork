from random import *

class Monster(object):
	"""A class to store Monster Information."""
	def __init__(self):
		"""Monster Constructor."""
		self.attackStrength = 0
		self.healthPoints = 0


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
		self.healthPoints = randrange(50, 100)
		

class Vampire(Monster):
	"""Class to store Vampire Information."""
	def __init__(self):
		"""Vampire Constructor"""
		super(Vampire, self).__init__()
		self.attackStrength = randrange(10, 20)
		self.healthPoints = randrange(100, 200)

class Ghoul(Monster):
	"""Class to store ghoul information."""
	def __init__(self):
		"""Ghoul Constructor."""
		super(Ghoul, self).__init__()
		self.attackStength = randrange(15, 30)
		self.healthPoints = randrange(40, 80)

class Werewolf(Monster):
	"""Class to store werewolf information."""
	def __init__(self):
		"""Werewolf."""
		super(Werewolf, self).__init__()
		self.attackStrength = randrange(0, 40)
		self.healthPoints = 200
