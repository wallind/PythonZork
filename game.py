import hood
import player
from random import*

class Game(object):
	"""sdgadhg"""
	def __init__(self):
		"""constructornfwerqfgwe"""
		self.neighborHood = hood.Neighborhood()
		self.player1 = player.Player()
		while(True):
			self.position = self.neighborHood.grid[randrange(self.neighborHood.h)][randrange(self.neighborHood.w)]
			if (self.position != 0):
				break
		print ("\n\n\nStarting Position")
		print ("\n\nX position: " + str(self.position.x))
		print ("\nY position: " + str(self.position.y))		

		
		print ("\n\n\nWidth and Height of Grid(Maybe not in that order :P")
		print ("\n\n'W': " + str(self.neighborHood.w))
		print ("\n'H': " + str(self.neighborHood.h))		


	def move(self, direction):
		if (direction == "up"):
			try:
				if (self.neighborHood.grid[self.position.y + 1][self.position.x].flag == 1):
				
					self.position = self.neighborHood.grid[self.position.y + 1][self.position.x]
					print ("\n\n\nPosition After Move ")
					print ("\n\nX position: " + str(self.position.x))
					print ("\nY position: " + str(self.position.y))
				else:
					self.position = self.neighborHood.grid[self.position.y + 1][self.position.x]
					print ("No house here")
					return
			except IndexError:
				print ("Cant move up")
		if (direction == "down"):
			try:
				if ((self.position.y - 1) < 0):
					raise IndexError()	
				if (self.neighborHood.grid[self.position.y - 1][self.position.x].flag == 1):
					self.position = self.neighborHood.grid[self.position.y - 1][self.position.x]
					print ("\n\n\nPosition After Move ")
					print ("\n\nX position: " + str(self.position.x))
					print ("\nY position: " + str(self.position.y))
				else:
					self.position = self.neighborHood.grid[self.position.y - 1][self.position.x]
					print ("No house here")
					return
			except IndexError:
				print ("Cant move down")
		if (direction == "left"):
			try:
				if ((self.position.x - 1) < 0):
					raise IndexError()
				if (self.neighborHood.grid[self.position.y][self.position.x - 1].flag == 1):
					self.position = self.neighborHood.grid[self.position.y][self.position.x - 1]
					print ("\n\n\nPosition After Move ")
					print ("\n\nX position: " + str(self.position.x))
					print ("\nY position: " + str(self.position.y))
				else:
					self.position = self.neighborHood.grid[self.position.y][self.position.x - 1]
					print ("No house here")
					return
			except IndexError:
				print ("Cant move left")
		if (direction == "right"):	
			try:
				if (self.neighborHood.grid[self.position.y][self.position.x + 1].flag == 1):
				
					self.position = self.neighborHood.grid[self.position.y][self.position.x + 1]
					print ("\n\n\nPosition After Move ")
					print ("\n\nX position: " + str(self.position.x))
					print ("\nY position: " + str(self.position.y))
				else:
					self.position = self.neighborHood.grid[self.position.y][self.position.x + 1]
					print ("No house here")
					return
			except IndexError:
				print ("Cant move right")


