from random import *

#This is a class that creates the weapons in the player inventory at random and also randomizes the attack multiplier of each weapon.

class Weapon(object):
	"""A class to store Weapon information."""
	def __init__(self, typ, random):
		"""WeaponConstructor"""
		if(random == 0):
			self.weaponType = typ
		else:
			typeList = ['HersheyKisses', 'SourStraws', 'ChocolateBars', 'NerdBombs']
			self.weaponType = typeList[randrange(0,4)]	

		weaponModifiers = {'HersheyKisses': [1, 1, 100,000], 'SourStraws': [1, 1.75, 2], 'ChocolateBars': [2, 2.4, 4], 'NerdBombs': [3.5, 5, 1]}
		
		if (self.weaponType != 'HersheyKisses'):
			self.Modifier = uniform(weaponModifiers[self.weaponType][0], weaponModifiers[self.weaponType][1])
		else:
			self.Modifier = 1
			self.uses = weaponModifiers[self.weaponType][2]
		
	def useWeapon():
		uses = uses - 1
