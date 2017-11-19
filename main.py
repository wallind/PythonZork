#!/usr/bin/env python3

from game import Game
from game import GUI

#This is the main method that creates an insatnce of the game and how the game is played through.

if __name__ == "__main__":
	testGame = Game()
	testGUI = GUI(testGame)
	testGUI.run()
