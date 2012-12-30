#!/usr/bin/env python
import math
import random
from time import clock, time
from weapon import *
from health import *

class Robot(object):
    def __init__(self,id,x,y,angle,hp,wp,win=0,loss=0):
        self.id=id
        self.x=x
        self.y=y
        self.angle=angle
        self.hp=hp
        self.wp=wp
        self.time=0
        self.runXY=[0]*2
        self.status='Doing something'
        self.hitStatus='None'
        self.win=win
        self.loss=loss
    def getPos(self):
        return (self.x,self.y, self.angle)

    def forward(self,distance):
	#move forward 'distance' units along 'angle'
	#by default, an angle of '0' faces the bot to the right of the screen
        self.x=self.x+math.cos(self.angle)*distance
        self.y=self.y+math.sin(self.angle)*distance

    def inrange(self,x2,y2):
        #check to see if any of the bots are in range to shoot
        if math.sqrt(((self.x-x2)**2+(self.y-y2)**2))<self.wp.range:
            return 1
        else:
            return 0

    def loadWp(self):
        if int(time()-self.time)>self.wp.rtime:
            return 1
        else :
            return 0
        
    
    def shoot(self):
        if self.loadWp():
            self.time=time() #store moment of shooting
            if random.randint(1,101)<self.wp.acc*10:
                return self.wp.dmg
            else:
                return 0
        
        
def distance(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2+(y1-y2)**2))
    

    
class RobotC(Robot):
    def step(self,x,y):
        self.angle+=0.2*math.atan2(y-self.y,x-self.x)
        self.angle/=1.2
        self.forward(2)
    def getName(self):
        return "Almost Perfect robot"
    def getDetails(self):
        print "ID:{0}".format(self.id)
        print "Weapon:"
        self.wp.getDet()
        print "Hp:"
        self.hp.getDet()
        print "\n"

