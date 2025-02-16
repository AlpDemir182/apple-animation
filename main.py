import pygame
import pgzrun
import time



WIDTH = 250
HEIGHT = 250

apple = Actor("apple")
count = 0
apple.x = 20
apple.y = 125

def draw():
    global count
    screen.clear()
    apple.draw()
    screen.draw.text("count: " +str(count), (20,10), color = "white", fontsize = 15)




def startanimation():
    global count
    if count < 5:
        animate(apple, pos = (230,125), duration = 2, on_finished = endanimation)
        count += 1
    



def endanimation():
    animate(apple, pos = (10,125), duration = 2, on_finished = startanimation)

#def moveforward():
    #animate(apple, pos = (230,125), duration = 2, on_finished = endanimation)

startanimation()
pgzrun.go()