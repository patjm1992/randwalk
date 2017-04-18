# random walk - works as written
# rev3 try to loop and add on to new point

#create window with center point of 100/2 , 100/2

from graphics import*
X = 200 #increased window size to see path walked better
Y = 200
win = GraphWin("Let's take a walk", X, Y)
center = Point (X/2, Y/2)
center.draw(win)

#generate random direction to take
#and loop for n steps


from random import random

def genDir():
    angle = random()*2*math.pi
    return(angle)

import math
def newPoint(dir):
    x = 0
    y = 0
    x = x + math.cos(dir)
    y = Y + math.sin(dir)
    p = Point(x,y)
    p.draw(win)
    return(x,y)

#print intro to program purpose & get # steps to take
def main():
    print ("This program generates a random path to walk")
    print ("and cacluates the ending distance from the start")
    n = eval(input("How many steps do you want to take each time? "))
    p1 = Point(200/2, 200/2)
    for i in range (n):
        dir = genDir()
        x,y = newPoint(dir)
        print(x, y)
        
        
        
main()


    

#walk n steps in random direction & print point

#loop n steps in another random direction until total number steps =100

#calculate distance from last point to center point

#print distance
