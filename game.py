import hood
import player
import sys

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
				print ("Re initializing Game (no empty houses)")
				self.neighborHood = hood.Neighborhood()
	
		print ("\n\n\nStarting Position")
		print ("\n\nX position: " + str(self.position.x))
		print ("\nY position: " + str(self.position.y))		

		
		print ("\n\n\nWidth and Height of Grid")
		print ("\n\n'W': " + str(self.neighborHood.w))
		print ("\n'H': " + str(self.neighborHood.h))		

	





	def show(self):
		for i in range (self.neighborHood.h):
			for k in range(self.neighborHood.w):
				sys.stdout.write(" [ ")
				if ((self.neighborHood.h - i - 1) == self.position.y and k == self.position.x):
					sys.stdout.write("X ] ")
				else:
					sys.stdout.write("  ] ")
			sys.stdout.write("\n")


	def move(self, direction):
		if (direction == "up"):
			try:
				if (self.neighborHood.grid[self.position.y + 1][self.position.x].flag == 1):
					self.position = self.neighborHood.grid[self.position.y + 1][self.position.x]
				else:
					self.position = self.neighborHood.grid[self.position.y + 1][self.position.x]
					print ("No house here")
			except IndexError:
				print ("Cant move up")
		if (direction == "down"):
			try:
				if ((self.position.y - 1) < 0):
					raise IndexError()	
				
				if (self.neighborHood.grid[self.position.y - 1][self.position.x].flag == 1):
					self.position = self.neighborHood.grid[self.position.y - 1][self.position.x]
				else:
					self.position = self.neighborHood.grid[self.position.y - 1][self.position.x]
					print ("No house here")
			except IndexError:
				print ("Cant move down")
		if (direction == "left"):
			try:
				if ((self.position.x - 1) < 0):
					raise IndexError()

				if (self.neighborHood.grid[self.position.y][self.position.x - 1].flag == 1):
					self.position = self.neighborHood.grid[self.position.y][self.position.x - 1]
				else:
					self.position = self.neighborHood.grid[self.position.y][self.position.x - 1]
					print ("No house here")
			except IndexError:
				print ("Cant move left")
		if (direction == "right"):	
			try:
				if (self.neighborHood.grid[self.position.y][self.position.x + 1].flag == 1):
					self.position = self.neighborHood.grid[self.position.y][self.position.x + 1]
				else:
					self.position = self.neighborHood.grid[self.position.y][self.position.x + 1]
					print ("No house here")
			except IndexError:
				print ("Cant move right")

		self.show()

