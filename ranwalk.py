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

height = 200
width = 200

def main():
	window, center = gui()
	print("Walker is at: ", center)
	while True:
		steps = eval(input("How many steps do you want to take? "))
		ran_walk(steps, window, center)
		print("Walker is at ")

def gui():
	win = GraphWin("Let's take a walk!", height, width)
	win.setBackground("White")
	center = Point(height / 2, width / 2)
	center.draw(win)
	return win, center

def generate_direction():
	return random() * 2 * math.pi

def new_point(direction):
	pass


def ran_walk(steps, win, walker):

	# Center
	x = y = height / 2

	# Loop over the number of steps, getting a new angle for each step
	# and calculating new (x, y) coordinates to move to, then draw that
	# line between the new (x, y) and the previous (x, y).
	for i in range(steps):
		angle = generate_direction()

		x_change = math.cos(angle)
		y_change = math.sin(angle)

		# this moves the walker, but doesn't draw it yet
		#walker.move(x_change, y_change)

		new_x = x + x_change
		new_y = y + y_change

		new_line = Line(Point(x, y), Point(new_x, new_y))
		new_line.draw(win)

		# 'Save' a new x and y position
		x = new_x
		y = new_y



if __name__ == '__main__': main()