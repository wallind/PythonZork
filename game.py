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

		for monster in self.position.monsters:
			monster.getAttacked(weaponNow,self.player1.attackValue)			
			
			if (monster.healthPoints <= 0):
				monster.update_observers(False, count)

			count = count + 1

		self.player1.useWeapon(weapon)

	def getHouseData(self, field):
		if (field == "monsters"):
			return self.neighborHood.getMonsters()
			
		if (field == "flag"):
			return self.neighborHood.getFlag()

		if (field == "position"):
			tempList = [self.neighborHood.getXPos(), self.neighborHood.getYPos()]
			return tempList


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



####################################################################
#This class is what creates the pygame GUI
####################################################################
class GUI(object):
	"""Constructor for GUI"""
	def __init__(self, g):
		self.game = g
		self.message = ""

		pygame.init()
		self.myFont = pygame.font.SysFont("inconsolata", 14)
	
		self.gameBoardWidth, self.gameBoardHeight = self.game.neighborHood.w * 60, self.game.neighborHood.h * 24
		self.mainBoardWidth, self.mainBoardHeight = self.gameBoardWidth + 500, self.gameBoardHeight + 200



		self.screen = pygame.display.set_mode((self.mainBoardWidth, self.mainBoardHeight), 0, 32)


		self.mainBoard = pygame.Surface(self.screen.get_size())
		self.gameBoard = pygame.Surface((self.gameBoardWidth, self.gameBoardHeight))	
		self.textBoard = pygame.Surface((500, self.mainBoardHeight))

		self.clock = pygame.time.Clock()

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

						elif (self.game.position.flag == 1):
							self.enterHouse()
						
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
		while (not done):
			for event in pygame.event.get():
				if (event.type == KEYDOWN):
					done = True
					if (event.key == K_0):
						self.game.attack(0)
					if (event.key == K_1):
						self.game.attack(1)
					if (event.key == K_2):
						self.game.attack(2)
					if (event.key == K_3):
						self.game.attack(3)
					self.updateBoards("combat")
					
					for monst in self.game.position.monsters:
						if (type(monst) is not monster.Person):
							done = False
		self.updateBoards("moving")
		self.game.neighborHood.grid[self.game.position.x][self.game.position.y].flag = 2		

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
			temp = "Move around the neighborhood using the arrow keys and"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 50))
			temp = "kill all the monsters. Once a house has been cleared"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 70))
			temp = "The icon will change from [    ] to [[   ]]"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 90))
			temp = "Press Enter to start"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 200))
		
		elif (state == "moving"):
			temp = "Use the arrow keys to move"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 20))
			temp = "          ^"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 50))
			temp = "          |"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 70))
			temp = "       <--|-->"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 90))
			temp = "          |"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 110))
			temp = "          v"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 130))
			temp = "Press Enter to go into a"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 200))
			temp = "house and engage the monsters"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 220))
			temp = "Console: " + self.message
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 255))

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
			
			for index in range(10):	
				if (index < len(self.game.position.monsters)):
					temp = str(type(self.game.position.monsters[index]))
					temp = temp[16:-2]
			
					label = self.myFont.render(temp, 1, (255, 255, 255))
					self.textBoard.blit(label, (15, pos))

					if (type(self.game.position.monsters[index]) is not monster.Person):	
						temp ="| " + str(int(self.game.position.monsters[index].healthPoints))
					
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
			temp = "Player HP: " + str(self.game.player1.hp) + "   ["
			
			for bar in range(30):
				if (bar * 5 < self.game.player1.hp):
					temp = temp + "|"
			
				else:
					temp = temp + " "
			temp = temp + "]"
			label = self.myFont.render(temp, 1, (255, 255, 255))
			self.textBoard.blit(label, (15, 268))


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
		
		if (textState == "moving" or "init"):
			self.updateGameBoard()	

		self.mainBoard.fill((255, 170, 0))

		self.mainBoard.blit(self.textBoard, (self.gameBoardWidth, 0))
		self.mainBoard.blit(self.gameBoard, (0, (int ((self.mainBoardHeight / 2) - (self.gameBoardHeight / 2)))))
		self.screen.blit(self.mainBoard, (0, 0))

		pygame.display.update()
