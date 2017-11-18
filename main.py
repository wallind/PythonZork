#!/usr/bin/env python3

from game import Game
from game import GUI

if __name__ == "__main__":
	testGame = Game()
	testGUI = GUI(testGame)
	testGUI.run()
