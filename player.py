import weapon
from random import*

#This class initializes a player and randomizes his heatlh, attack value and weapons in his inventory

class Player(object):
	"""sedgsetdhhsdfh"""
	def __init__(self):
		"""sedgrtjhetykjrtjh"""
		self.hp = randrange(100, 126)
		self.attackValue = randrange(10, 21)
		self.weapons = []
		
		for i in range(10):
			
			temp = weapon.Weapon("error", 1)
			self.weapons.append(temp)
	def useWeapon(self, index):
		if (self.weapons[index].uses >= 0):
			self.weapons[index].useWeapon()
