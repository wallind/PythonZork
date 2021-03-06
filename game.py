import hood
import player
import sys
import monster

import pygame
from pygame.locals import *

from random import*

####################################################################
#This is the game class that holds an instance of a player and a 
#neighborhood and also creates our pygame GUI.
####################################################################
class Game(object):
	def __init__(self):
		self.neighborHood = hood.Neighborhood()
		self.player1 = player.Player()

	########################################################################
	#This is the method that goes through a list of homes and the monsters
	#in each home and then attacks each momnster within that house.
	#######################################################################
	def attack(self, weapon):
		weaponNow = self.player1.weapons[weapon]
	
		if (weaponNow.uses == 0):
			return

		count = 0

		for monster in self.getHouseData("monsters"):
			monster.getAttacked(weaponNow,self.player1.attackValue)			
			
			if (monster.healthPoints <= 0):
				monster.update_observers(False, count)

			count = count + 1

		self.player1.useWeapon(weapon)

	########################################################################
	#This is the method that allows the monsters to attack you
	#######################################################################
	def getAttacked(self):
		monsters = self.getHouseData("monsters")
		
		for monst in monsters:
			print (monst.getAttackValue())
			self.player1.getAttacked(monst.getAttackValue())
		return True

	########################################################################
	#This is the method that tells you if there are monsters in the 
	#specific house you are at
	#######################################################################
	def getHouseData(self, field):
		if (field == "monsters"):
			return self.neighborHood.getMonsters()
			
		if (field == "flag"):
			return self.neighborHood.getFlag()

		if (field == "position"):
			tempList = [self.neighborHood.getXPos(), self.neighborHood.getYPos()]
			return tempList

	########################################################################
	#This is a setter that sets a flag on a house
	#######################################################################
	def setFlag(self, flag):
		self.neighborHood.setFlag(flag)

	########################################################################
	#This is the method that sets the position you are at and informs you
	#if you cannot move in a certain direction.
	#######################################################################
	def setPosition(self, xChange, yChange):
		posXY = self.getHouseData("position")

		if (posXY[0] + xChange < 0):
			return ("Cant move there")

		if (posXY[1] + yChange < 0):
			return ("Cant move there")

		if (not self.neighborHood.changeXPos(xChange)):
			return ("Cant move there")

		if (not self.neighborHood.changeYPos(yChange)):
			return ("Cant move there")
		
		return ""


	def gameStatus(self):
		if (self.player1.getHealthPoints() <= 0):
			return False
		
		return True


####################################################################
#This class is what creates the pygame GUI
####################################################################
class GUI(object):
	"""Constructor for GUI"""
	def __init__(self):
		self.game = Game()
		self.message = ""

		pygame.init()
		self.myFont = pygame.font.SysFont("inconsolata", 14)
	
		self.gameBoardWidth, self.gameBoardHeight = self.game.neighborHood.w * 60, self.game.neighborHood.h * 24
		self.mainBoardWidth, self.mainBoardHeight = self.gameBoardWidth + 500, self.gameBoardHeight + 200



		self.screen = pygame.display.set_mode((self.mainBoardWidth, self.mainBoardHeight), 0, 32)


		self.mainBoard = pygame.Surface(self.screen.get_size())
		self.gameBoard = pygame.Surface((self.gameBoardWidth, self.gameBoardHeight))	
		self.textBoard = pygame.Surface((500, self.mainBoardHeight))

		self.updateBoards("init")

	####################################################################
	#This method allows you to used the arrow keys to move around.
	####################################################################
	def run(self):
		playing = False
		while (True):	
			for event in pygame.event.get():
				if (event.type == QUIT):
					pygame.quit()
					sys.exit()
				
				elif (event.type == KEYDOWN):
					if (event.key == K_RETURN):
						if (not playing):
							playing = True
							self.updateBoards("moving")

						elif (self.game.getHouseData("flag") == 1):
							
							self.enterHouse()
							if (not self.game.gameStatus()):
								self.updateBoards("gameover")
								self.game = Game()
								playing = False
						
					elif (playing):
						if (event.key == K_UP):
							self.message = self.game.setPosition(0, 1)
							self.updateBoards("moving")
			
						if (event.key == K_DOWN):
							self.message = self.game.setPosition(0, -1)
							self.updateBoards("moving")
			
						if (event.key == K_RIGHT):
							self.message = self.game.setPosition(1, 0)
							self.updateBoards("moving")

						if (event.key == K_LEFT):
							self.message = self.game.setPosition(-1, 0)
							self.updateBoards("moving")



	####################################################################
	#This method is used to enter the house and start attacking the 
	#monsters within it.
	####################################################################
	def enterHouse(self):
		self.updateBoards("combat")
		done = False	
		playerAlive = True
		while (not done):
			for event in pygame.event.get():
				if (event.type == KEYDOWN):
					done = True
					if (event.key == K_0):
						self.game.attack(0)
						self.game.getAttacked()
					if (event.key == K_1):
						self.game.attack(1)
						self.game.getAttacked()
					if (event.key == K_2):
						self.game.attack(2)
						self.game.getAttacked()
					if (event.key == K_3):
						self.game.attack(3)
						self.game.getAttacked()
					self.updateBoards("combat")
				

					if (not self.game.gameStatus()):
						return 
				
					for monst in self.game.getHouseData("monsters"):
						if (type(monst) is not monster.Person):
							done = False
		self.game.setFlag(2)
		self.updateBoards("moving")
		return False

	####################################################################
	#This method updates the text being output corrctly
	####################################################################					
	def updateTextBoard(self, state):
		self.textBoard.fill((255, 170, 0))
		rectangle = pygame.Rect(10, 10, 480, self.mainBoardHeight - 20)
		pygame.draw.rect(self.textBoard, (0, 0 , 0), rectangle)

		if (state == "init"):	
			temp = "Welcome to the NeighborHood"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (20, 15))
			temp = "Move around the neighborhood using the arrow keys and kill"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 50))
			temp = "all the monsters. Once a house has been cleared the icon"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 70))
			temp = "will change from [    ] to [[   ]]"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 90))
			temp = "Press Enter to start"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 200))
		
		elif (state == "moving"):
			temp = "Use the arrow keys to move around the neighborhood. "
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 20))
			temp = "Press Enter to go into a"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 70))
			temp = "house and engage the monsters"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 90))
			temp = "Console: " + self.message
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 200))
			
			temp = "Player HP: " + str(self.game.player1.getHealthPoints()) + "   ["
			
			for bar in range(30):
				if (bar * 5 < self.game.player1.getHealthPoints()):
					temp = temp + "|"
			
				else:
					temp = temp + " "
			temp = temp + "]"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 260))

		elif (state == "combat"):
			temp = "Press the corresponding number"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 20))
			temp = "key to attack with a weapon"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 40))
			temp = "Monsters  | HP   || (NUMKEY) |  Weapon Type  | Uses Left "
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 80))
			temp = "_________________________________________________________"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 90))
			
			pos = 110
			
			monstersTemp = self.game.getHouseData("monsters")

			for index in range(10):	
				if (index < len(monstersTemp)):
					temp = str(type(monstersTemp[index]))
					temp = temp[16:-2]
			
					label = self.myFont.render(temp, 1, (255, 255, 255))
					self.textBoard.blit(label, (15, pos))

					if (type(monstersTemp[index]) is not monster.Person):	
						temp ="| " + str(int(monstersTemp[index].healthPoints))

					else:
						temp = "|"
						
					label = self.myFont.render(temp, 1, (255, 255, 255))
					self.textBoard.blit(label, (94, pos))


				if (index < len(self.game.player1.weapons)):
					temp = "||   (" +str(index) + ")    | "
					temp = temp + self.game.player1.weapons[index].weaponType
					label = self.myFont.render(temp, 1, (255, 255, 255))
					self.textBoard.blit(label, (151, pos))

					temp = "| " + str(self.game.player1.weapons[index].uses)
					label = self.myFont.render(temp, 1, (255, 255, 255))
					self.textBoard.blit(label, (375, pos))
				pos = pos + 15
			temp = "Player HP: " + str(self.game.player1.getHealthPoints()) + "   ["
			
			for bar in range(30):
				if (bar * 5 < self.game.player1.getHealthPoints()):
					temp = temp + "|"
			
				else:
					temp = temp + " "
			temp = temp + "]"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 260))

		elif(state == "gameover"):
			temp = ":(      YOU HAVE DIED!!    :("
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 20))
			temp = "Thanks for playing."
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 200))
			temp = "Press Enter to Restart"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 240))


	####################################################################
	#This method updates the game board and sizes it correctly.
	####################################################################
	def updateGameBoard(self):
		tempVar = self.game.neighborHood.show()

		pos = 15

		self.gameBoard.fill((255, 170, 0))
		for string in tempVar:
			label = self.myFont.render(string, 1, (0, 0, 0))
			self.gameBoard.blit(label, (10, pos))
			pos = pos + 20
	

		rectangle =  pygame.Rect(9, 9, self.gameBoardWidth - 15, self.gameBoardHeight - 10)
		pygame.draw.rect(self.gameBoard, (0, 0, 0), rectangle, 2)
		
	####################################################################
	#This method updates the board to the proper coloring we want.
	####################################################################
	def updateBoards(self, textState):
		self.updateTextBoard(textState)
		self.updateGameBoard()		

		self.mainBoard.fill((255, 170, 0))

		self.mainBoard.blit(self.textBoard, (self.gameBoardWidth, 0))
		self.mainBoard.blit(self.gameBoard, (0, (int ((self.mainBoardHeight / 2) - (self.gameBoardHeight / 2)))))
		self.screen.blit(self.mainBoard, (0, 0))

		pygame.display.update()
