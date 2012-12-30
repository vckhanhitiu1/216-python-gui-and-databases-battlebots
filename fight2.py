from robot import *
import pygame
import random

w=800

h=600

WHITE=(255,255,255)
BLACK=(0,0,0)

clock=pygame.time.Clock()

def fight(Rob1,Rob2):
#    wp1=Weapon(3,7,20,2)
#    wp2=Weapon(4,3,25,2)
#    hp1=Health(10,10)
#    hp2=Health(10,10)
    r1=Rob1
    r2=Rob2
    robots=(r1,r2)
        
    loop=True
    while loop:
        #Clear
#        if r1.loadWp()!=0:  #follow enemy if weapon loaded
#           r1.step(r2.getPos()[0],r2.getPos()[1])
#       else: #run if weapon is unloaded
#            r1.step(-r2.getPos()[0],-r2.getPos[1])
#       if r1.loadWp()!=0: #follow enemy if weapon loaded
#           r2.step(r1.getPos()[0],r1.getPos()[1])
#       else: #run if weapon is unloaded
#           r2.step(-r1.getPos()[0],-r1.getPos()[1])
#===================== Robot 1==========================
        if r1.inrange(r2.getPos()[0],r2.getPos()[1]):
            if r1.loadWp()!=0:  #shoot enemy if in range
                bam=r1.shoot()
                if r2.hp.update(bam)==0: #end game if robot dead
                    loop=False
                    return r1.id
               # else : print "R2:%d"%(r2.hp.chp)
            else: #run if weapon is unloaded
                r1.step(-r2.x,-r2.y)
        else:
            if r1.loadWp()!=0: # followe enemy if weapon loaded
                r1.step(r2.getPos()[0],r2.getPos()[1])
            else :
                r1.step(-r2.x,-r2.y)
#===================== Robot 2 ==========================
        if r2.inrange(r1.getPos()[0],r1.getPos()[1]):
            if r2.loadWp()!=0:  #shoot enemy if in range
                bom=r2.shoot()
                if r1.hp.update(bom)==0: #end game if roobot dead
                    loop=False
                    return r2.id
              #  else : print "R1:%d"%(r1.hp.chp)
            else: #run if weapon is unloaded
                r2.step(-r1.x,-r1.y)
        else:
            if r2.loadWp()!=0: # followe enemy if weapon loaded
                r2.step(r1.getPos()[0],r1.getPos()[1])
            else:
                r2.step(-r1.x,-r2.y)     
     
        clock.tick(30)
