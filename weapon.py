from random import *

class Weapon(object):
	"""A class to store Weapon information."""
	def __init__(self, typ):
		"""WeaponConstructor"""
		self.weaponType = typ
		weaponModifiers = {'HersheyKisses': 1, 'SourStraws': [1, 1.75, 2], 'ChocolateBars': [2, 2.4, 4], 'NerdBombs': [3.5, 5, 1]}
		
		if (typ != 'HersheyKisses'):
			self.Modifier = uniform(weaponModifiers[typ][0], weaponModifiers[typ][1])
		else:
			self.Modifier = 1
