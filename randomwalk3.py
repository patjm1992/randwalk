# random walk - works as written
# rev3 try to loop and add on to new point

#create window with center point of 100/2 , 100/2

from graphics import*
x = 200 #increased window size to see path walked better
y = 200
win = GraphWin("Let's take a walk", x, y)
center = Point (x/2, y/2)
center.draw(win)

#generate random direction to take
#and loop for n steps


from random import random

def genDir():
    angle = random()*2*math.pi
    return(angle)

import math



#print intro to program purpose & get # steps to take
def main():
	while True:
	    print ("This program generates a random path to walk")
	    print ("and calculates the ending distance from the start")
	    n = eval(input("How many steps do you want to take each time? "))

	    p1 = Point(200/2, 200/2) # this is the correct center (for your window size)
	    x = y = 200 / 2

	    for i in range (n):
	        dir = genDir()

	        new_x = x + math.cos(dir)
	        new_y = y + math.sin(dir)

	        new_point = Point(new_x, new_y)

	        line = Line(p1, new_point)
	        line.draw(win)

	        x = new_x
	        y = new_y
	        p1 = new_point
	        # draw the line



main()




#walk n steps in random direction & print point

#loop n steps in another random direction until total number steps =100

#calculate distance from last point to center point

#print distance
