import hood
import player
import sys
import monster

import pygame
from pygame.locals import *

from random import*

#This is the game class that holds an instance of a player and a neighborhood and also creates our pygame GUI

class Game(object):
	"""sdgadhg"""
	def __init__(self):
		"""constructornfwerqfgwe"""
		self.neighborHood = hood.Neighborhood()
		self.player1 = player.Player()
		
		count = 0
			
		while(True):
			try:
				count = count + 1
				self.position = self.neighborHood.grid[randrange(self.neighborHood.h)][randrange(self.neighborHood.w)]
				if (self.position.flag != 1):
					break
				if (count == 400):
					raise Exception("No Empty House")
			except Exception:
				self.neighborHood = hood.Neighborhood()
	
	def show(self):
		output = []
		for i in range (self.neighborHood.h):
			temp = ""
			for k in range(self.neighborHood.w):
				if ((self.neighborHood.grid[k][self.neighborHood.h - i - 1]).flag == 1):
					temp = temp + " [ "
					if ((self.neighborHood.h - i - 1) == self.position.y and k == self.position.x):
						temp = temp + "X ] "
					else:
						temp = temp + "  ] "
				elif ((self.neighborHood.h - i - 1) == self.position.y and k == self.position.x):
					temp = temp + "   X   "
				else:
					temp = temp + "       "
			output.append(temp)
		return output


	def move(self, direction):
		if (direction == "up"):
			try:
				if (self.neighborHood.grid[self.position.x][self.position.y + 1].flag == 1):
					self.position = self.neighborHood.grid[self.position.x][self.position.y + 1]
				else:
					self.position = self.neighborHood.grid[self.position.x][self.position.y + 1]
					print ("No house here")
			except IndexError:
				print ("Cant move up")
		if (direction == "down"):
			try:
				if ((self.position.y - 1) < 0):
					raise IndexError()	
				
				if (self.neighborHood.grid[self.position.x][self.position.y - 1].flag == 1):
					self.position = self.neighborHood.grid[self.position.x][self.position.y -1]
				else:
					self.position = self.neighborHood.grid[self.position.x][self.position.y - 1]
					print ("No house here")
			except IndexError:
				print ("Cant move down")
		if (direction == "left"):
			try:
				if ((self.position.x - 1) < 0):
					raise IndexError()

				if (self.neighborHood.grid[self.position.x - 1][self.position.y].flag == 1):
					self.position = self.neighborHood.grid[self.position.x - 1][self.position.y]
				else:
					self.position = self.neighborHood.grid[self.position.x - 1][self.position.y]
					print ("No house here")
			except IndexError:
				print ("Cant move left")
		if (direction == "right"):	
			try:
				if (self.neighborHood.grid[self.position.x + 1][self.position.y].flag == 1):
					self.position = self.neighborHood.grid[self.position.x + 1][self.position.y]
				else:
					self.position = self.neighborHood.grid[self.position.x + 1][self.position.y]
					print ("No house here")
			except IndexError:
				print ("Cant move right")

		self.show()

	#needs some work but got a start on it for the most part. also couldnt test it so theres
	#most likely some errors in there, also need to get it to recognize which house it is in on the grid
	def attack(self):
		monsters = []
		weapons = []

		self.monsters = hood.House().monsters
		self.weapons = player.weapons

		for i in monsters:
			for x in weapons:
				if(monsters[i] == monster.Zombie() && self.weapons[x] == "SourStraws"):
					#self.player1.hp = self.player1.hp - self.Zombie().attackStrength
					self.Zombie().healthPoints = self.Zombie().healthPoints - self.player1.weapons[x]*2
					print("attacked a Zombie")
					print("Zombies heatlh = " + Zombie().healthPoints)
					print("Your health = " + player1.healthPoints)
				elif(monsters[i] == monster.Zombie()):
					#self.player1.hp = self.player1.hp - self.Zombie().attackStrength
					self.Zombie().healthPoints = self.Zombie().healthPoints - self.player1.weapons[x]
					print("attacked a Zombie")
					print("Zombies heatlh = " + Zombie().healthPoints)
					print("Your health = " + player1.healthPoints)
				elif(monsters[i] == monster.Vampire() && self.weapons[x] != "ChocolateBars"):
					#self.player1.hp = self.player1.hp - self.Vampire().attackStrength
					self.Vampire().healthPoints = self.Vampire().healthPoints - self.player1.weapons[x]
					print("attacked a Vampire")
					print("Vampire heatlh = " + Vampire().healthPoints)
					print("Your health = " + player1.healthPoints)
				elif(monsters[i] == monster.Ghoul() && self.weapons[x] == "NerdBombs"):
					#self.player1.hp = self.player1.hp - self.Ghoul().attackStrength
					self.Ghoul().healthPoints = self.Ghoul().healthPoints - self.player1.weapons[x]*5
					print("attacked a Ghoul")
					print("Ghouls heatlh = " + Ghoul().healthPoints)
					print("Your health = " + player1.healthPoints)	
				elif(monsters[i] == monster.Ghoul()):
					#self.player1.hp = self.player1.hp - self.Ghoul().attackStrength
					self.Ghoul().healthPoints = self.Ghoul().healthPoints - self.player1.weapons[x]
					print("attacked a Ghoul")
					print("Ghouls heatlh = " + Ghoul().healthPoints)
					print("Your health = " + player1.healthPoints)	
				elif(monsters[i] == monster.Werewolf() && self.weapons[x] != "ChocolateBars" && self.weapons[x] != "SourStraws"):
					#self.player1.hp = self.player1.hp - self.Werewolf().attackStrength
					self.Werewolf().healthPoints = self.Werewolf().healthPoints - self.player1.weapons[x]
					print("attacked a Werewolf")
					print("Werewolf heatlh = " + Werewolf().healthPoints)
					print("Your health = " + player1.healthPoints)	
				elif(monsters[i] == monster.Person()):	
					self.player1.hp = self.player1.hp - self.Person().attackStrength	

	#if the monster dies then it must be turned into a person
	def deadMonster(self):


	#method that checks to see if the player is alive
	def isPlayerAlive(self):
		if(player1.healthPoints <= 0):
			("You are now dead, it was a good run")
			system.exit()	


class GUI(object):
	"""asfdjasdfas"""
	def __init__(self, g):
		self.game = g

		pygame.init()

		
		self.gameBoardWidth, self.gameBoardHeight = self.game.neighborHood.w * 67, self.game.neighborHood.h * 24
		self.mainBoardWidth, self.mainBoardHeight = self.gameBoardWidth + 300, self.gameBoardHeight + 200



		self.screen = pygame.display.set_mode((self.mainBoardWidth, self.mainBoardHeight), 0, 32)


		self.mainBoard = pygame.Surface(self.screen.get_size())
		self.gameBoard = pygame.Surface((self.gameBoardWidth, self.gameBoardHeight))	
		self.textBoard = pygame.Surface((300, self.mainBoardHeight))

		self.clock = pygame.time.Clock()

		self.updateBoards()

	def run(self):
		while (True):	
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				elif (event.type == KEYDOWN):
					if (event.key == K_UP):
						self.game.move("up")
						self.updateBoards()
					if (event.key == K_DOWN):
						self.game.move("down")
						self.updateBoards()

					if (event.key == K_RIGHT):
						self.game.move("right")
						self.updateBoards()

					if (event.key == K_LEFT):
						self.game.move("left")
						self.updateBoards()
	
	def updateTextBoard(self):
		self.textBoard.fill((255, 170, 0))

		rectangle = pygame.Rect(10, 10, 280, self.mainBoardHeight - 20)
		pygame.draw.rect(self.textBoard, (0, 0 , 0), rectangle)

	def updateGameBoard(self):
		tempVar = self.game.show()
		pos = 10

		self.gameBoard.fill((255, 170, 0))
		for str in tempVar:
			myFont = pygame.font.SysFont("monospace", 15)
			label = myFont.render(str, 1, (0, 0, 0))
			self.gameBoard.blit(label, (10, 10 + pos))
			pos = pos + 20
	

		rectangle =  pygame.Rect(9, 9, self.gameBoardWidth - 15, self.gameBoardHeight - 10)
		pygame.draw.rect(self.gameBoard, (0, 0, 0), rectangle, 2)
		

	def updateBoards(self):
		self.updateTextBoard()
		self.updateGameBoard()

		self.mainBoard.fill((255, 170, 0))

		self.mainBoard.blit(self.textBoard, (self.gameBoardWidth, 0))
		self.mainBoard.blit(self.gameBoard, (0, (int ((self.mainBoardHeight / 2) - (self.gameBoardHeight / 2)))))
		self.screen.blit(self.mainBoard, (0, 0))

		pygame.display.update()
