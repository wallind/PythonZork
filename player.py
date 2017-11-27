########################################################################
# @author Mason Mahoney
# @author Douglas Wallind
########################################################################

from weapon import Weapon
from random import*

########################################################################
#This class initializes a player and randomizes his heatlh, attack value 
#and weapons in his inventory
########################################################################
class Player(object):
	def __init__(self):
		self.hp = randrange(100, 126)
		self.attackValue = randrange(10, 21)
		self.weapons = []

		for i in range(0, 4):
			self.weapons.append(Weapon(i))
		

		for i in range(0, 6):
			weaponId = randrange(0, 4)	
			tempWeapon = Weapon(weaponId)
			self.weapons[weaponId].addUses(weaponId)

	########################################################################
	#This method is used to keep track of how many uses a weapon has and if
	#it is 0 or greater it then calls the useWeapon again.
	########################################################################
	def useWeapon(self, index):
		if (self.weapons[index].uses >= 0):
			self.weapons[index].useWeapon()


	########################################################################
	#Getter method for getting attacked
	#######################################################################
	def getAttacked(self, attackVal):
		self.hp = self.hp - attackVal
		if (self.hp <= 0):
			return False
		
		else:
			return True
