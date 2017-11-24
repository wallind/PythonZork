from random import *

####################################################################
#This is a class that creates the weapons in the player inventory 
#at random and also randomizes the attack multiplier of each weapon.
####################################################################
class Weapon(object):
	"""A class to store Weapon information."""
	def __init__(self, typ):
		"""Weapon Constructor"""
		typeList = ['HersheyKisses', 'SourStraws', 'ChocolateBars', 'NerdBombs']
		self.weaponType = typeList[typ]	

		self.weaponModifiers = {'HersheyKisses': [1, 1, 10], 'SourStraws': [1, 1.75, 2], 'ChocolateBars': [2, 2.4, 4], 'NerdBombs': [3.5, 5, 1]}
		

		self.modifier = uniform(self.weaponModifiers[self.weaponType][0], self.weaponModifiers[self.weaponType][1])
		self.uses = self.weaponModifiers[self.weaponType][2]
		
	########################################################################
	#This method reduced the times a weapon can be used following its use
	#on a monster.
	########################################################################
	def useWeapon(self):
		self.uses = self.uses - 1

	def addUses(self, weaponId):
		self.uses = self.uses + self.weaponModifiers[self.weaponType][2]
