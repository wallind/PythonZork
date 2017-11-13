from random import *

class Weapon(object):
	"""A class to store Weapon information."""
	def __init__(self, weaponType):
		"""WeaponConstructor"""
		weaponModifiers = {'HersheyKisses': 1, 'SourStraws': [0, 2]}
		if (weaponType != 'HersheyKisses'):
			self.Modifier = randrange(weaponModifiers[weaponType][0], weaponModifiers[weaponType][1])
