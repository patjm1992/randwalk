from graphics import *
from random import random
import time
import math

'''
	Write a graphical program to trace a random walk in two
	dimensions.

	Allow the step to be taken in *any* direction.

	INPUT:  number of steps.
	OUTPUT: a drawn line as the walker moves

	Use a 100 x 100 grid with the walker beginning in the middle.
'''

height = 500
width = 500



def gui():
	win = GraphWin("Let's take a walk!", height, width)
	win.setBackground("White")
	center = Point(height / 2, width / 2)
	center.draw(win)

def generate_direction():
	return random() * 2 * math.pi


# Text user interface prototype
gui()

time.sleep(10)