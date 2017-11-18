import hood
import player
import sys

import pygame
from pygame.locals import *

from random import*

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
