#!/usr/bin/env python3

import sys
from game import Game
import pygame
from pygame.locals import *

if __name__ == "__main__":
	test = Game()
	test.show()

	pygame.init()


	print (test.neighborHood.w)


	
	screen = pygame.display.set_mode(((test.neighborHood.w * 65), (test.neighborHood.h * 25)), 0 , 32)
	surface = pygame.Surface(screen.get_size())	

	surface = surface.convert()
	surface.fill((255, 255, 255))
	clock = pygame.time.Clock()

	def update():
		tempVar = test.show()
		pos = 10

		surface.fill((255, 255, 255))
		for str in tempVar:
			myFont = pygame.font.SysFont("monospace", 15)
			label = myFont.render(str, 1, (0, 0, 0))
			surface.blit(label, (0, pos))
			pos = pos + 20
		
		screen.blit(surface, (0, 0))
		pygame.display.flip()
		pygame.display.update()
	
	

	while (True):	
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif (event.type == KEYDOWN):
				if (event.key == K_UP):
					test.move("up")
					update()

				if (event.key == K_DOWN):
					test.move("down")
					update()

				if (event.key == K_RIGHT):
					test.move("right")
					update()

				if (event.key == K_LEFT):
					test.move("left")
					update()

