#!/usr/bin/python

#battleBots.py
#Based on battleBots.py by James Shuttleworth

#If your robots are in "robots.py" use this line...
from robot import *
#or delete it and put your classes here instead

#Change code below for the classes of your two robots

#from pygame.locals import *
import pygame
import random

#loading background image
background = pygame.image.load("bg2.bmp")
backgroundRect = background.get_rect()
#loading robot image
robo1=pygame.image.load("robo.png")
robo2=pygame.image.load("robo2.png")


w=800
h=600

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)

clock=pygame.time.Clock()
wp1=Weapon(2,3,1,1)
wp2=Weapon(1,3,2,3)
hp1=Health(10)
hp2=Health(10)
r1=RobotC(1,random.randint(0,w),random.randint(0,h),0,hp1,wp1,0,0)
r2=RobotC(2,random.randint(0,w),random.randint(0,h),0,hp2,wp2,0,0)
pause=False


def setR1(hp,dmg,acc,range1,time,wins,losses):
    global wp1
    global hp1
    global r1
    wp1=Weapon(dmg,acc,range1*20,time)
    hp1=Health(hp)
    r1=RobotC(1,random.randint(25,w),random.randint(125,h),0,hp1,wp1,wins,losses)

def setR2(hp,dmg,acc,range2,time,wins,losses):
    global wp2
    global hp2
    global r2
    wp2=Weapon(dmg,acc,range2*20,time)
    hp2=Health(hp)
    r2=RobotC(2,random.randint(25,w),random.randint(125,h),0,hp2,wp2,wins,losses)

def printStats(r,labelfont,screen):
    robot='Robot %d'%(r.id)
    name=labelfont.render(robot,True,(255,255,255))
    weaponDet='Weapon: {0} dmg, {1} range, {2}% acc, {3} load time'.format(r.wp.dmg,r.wp.range,r.wp.acc*10,r.wp.rtime)
    weapon=labelfont.render(weaponDet,True,(255,255,255))
    hpDet='Hp: {0} total Hp, {1} current Hp'.format(r.hp.level,r.hp.chp)
    hp=labelfont.render(hpDet,True,(255,255,255))
    statusDet='Status: {0}'.format(r.status)
    status=labelfont.render(statusDet,True,(255,255,255))
    hitDet='Last atack: {0}'.format(r.hitStatus)
    hit=labelfont.render(hitDet,True,(255,255,255))
    recordDet='Wins: {0}, Losses:{1}'.format(r.win,r.loss)
    record=labelfont.render(recordDet,True,(255,255,255))
    if(r.id==1):
        screen.blit(name,(20,20))
        screen.blit(weapon,(20,35))
        screen.blit(hp,(20,50))
        screen.blit(status,(20,65))
        screen.blit(hit,(20,80))
        screen.blit(record,(190,80))
    else:
        screen.blit(name,(420,20))
        screen.blit(weapon,(420,35))
        screen.blit(hp,(420,50))
        screen.blit(status,(420,65))
        screen.blit(hit,(420,80))
        screen.blit(record,(590,80))

    
def RunXY(l):
    run=random.randint(1,4)
    if run==1:
        l[0]=l[0]*2 #x
        l[1]=l[1]*2 #y
    elif run==2:
        l[0]=-l[0]  #x
        l[1]=l[1]*2 #y
    elif run==3:
        l[0]=-l[0] #x
        l[1]=-l[1] #y
    else:
        l[0]=l[0]*2 #x
        l[1]=-l[1]  #y

    return l

def pauseState(state):
    global pause
    pause=state
    print "Pause:{0}".format(pause)

def fightArena():
    robots=(r1,r2)
    pygame.init()
    pygame.mixer.music.load('laser.wav')
    window = pygame.display.set_mode((w,h))
    screen = pygame.display.get_surface() 
    labelfont=pygame.font.Font("C:\\Windows\\Fonts\\ARIALN.TTF", 14)
    run1=0 # robot is not running
    run2=0 # robot is not running
    rob1Head=[0]*2
    rob2Head=[0]*2
    
    loop=True
    while loop:
        #Clear
        screen.fill(BLACK)
        screen.blit(background, backgroundRect)
        rob1Head[0]=r1.x+10
        rob1Head[1]=r1.y+10
        rob2Head[0]=r2.x+10
        rob2Head[1]=r2.y+10

#        if r1.loadWp()!=0:  #follow enemy if weapon loaded
#           r1.step(r2.getPos()[0],r2.getPos()[1])
#       else: #run if weapon is unloaded
#            r1.step(-r2.getPos()[0],-r2.getPos[1])
#       if r1.loadWp()!=0: #follow enemy if weapon loaded
#           r2.step(r1.getPos()[0],r1.getPos()[1])
#       else: #run if weapon is unloaded
#           r2.step(-r1.getPos()[0],-r1.getPos()[1])
#===================== Robot 1==========================
        if r1.inrange(r2.getPos()[0],r2.getPos()[1]): #check if enemy in range
            if r1.loadWp()!=0:  #shoot enemy if in range
                run1=1
                bam=r1.shoot()
                pygame.mixer.music.play(0,0)
                if bam:
                    r1.hitStatus='Hit!'
                else:
                    r1.hitStatus='Miss!'
                #Draw laser green
                pygame.draw.line(screen, GREEN, rob1Head, rob2Head,3)
                if r2.hp.update(bam)==0: #end game if robot dead
                    loop=False
                    pygame.quit()
                    return 'Robot 1'
            elif run1==1 and r1.loadWp()==0: #run if weapon is unloaded
                r1.status='Run for my virtual life!'
                run1=0  #set the running state
                r1.runXY[0]=r1.x
                r1.runXY[1]=r1.y
                r1.runXY=RunXY(r1.runXY)
                r1.step(r1.runXY[0],r1.runXY[1])

            else: #keep running
                r1.step(r1.runXY[0],r1.runXY[1])

        else:
            if r1.loadWp()!=0: # follow enemy if weapon loaded
                r1.status='Chasing enemy!'
                r1.step(r2.getPos()[0],r2.getPos()[1])

            elif run1==1: #run if weapon is unloaded
                run1=0  #set the running state
                r1.runXY[0]=r1.x
                r1.runXY[1]=r1.y
                r1.runXY=RunXY(r1.runXY)
                r1.step(r1.runXY[0],r1.runXY[1])
                 
            else: #keep running
                r1.step(r1.runXY[0],r1.runXY[1])
#===================== Robot 2 ==========================
        if r2.inrange(r1.getPos()[0],r1.getPos()[1]):
            if r2.loadWp()!=0:  #shoot enemy if in range
                run2=1
                bom=r2.shoot()
                pygame.mixer.music.play(0,0)
                if bom:
                    r2.hitStatus='Hit!'
                else:
                    r2.hitStatus='Miss!'
                #draw laser red
                pygame.draw.line(screen, RED, rob1Head, rob2Head,3)
                if r1.hp.update(bom)==0: #end game if roobot dead
                    loop=False
                    pygame.quit()
                    return 'Robot 2'
            elif run2==1 and r2.loadWp()==0: #run if weapon is unloaded
                run2=0  #set the running state
                r2.status='Run for my virtual life!'
                r2.runXY[0]=r2.x
                r2.runXY[1]=r2.y
                r2.runXY=RunXY(r2.runXY)
                r2.step(r2.runXY[0],r2.runXY[1])
            else: #keep running
                r2.step(r2.runXY[0],r2.runXY[1])
                
        else:
            if r2.loadWp()!=0: # followe enemy if weapon loaded
                r2.status='Chasing enemy!'
                r2.step(r1.getPos()[0],r1.getPos()[1])
                
            elif run2==1: #run if weapon is unloaded
                run2=0  #set the running state
                r2.runXY[0]=r2.x
                r2.runXY[1]=r2.y
                r2.runXY=RunXY(r2.runXY)
                r2.step(r2.runXY[0],r2.runXY[1])
                
            else: #keep running
                r2.step(r2.runXY[0],r2.runXY[1])

        
        
        for r in robots:
            if r.id==1:
                screen.blit(robo1,r.getPos()[:2])
            else:
                screen.blit(robo2,r.getPos()[:2])
            if r.x<=25:
                r.x=25
                r.runXY[0]=-r.runXY[0]
            if r.x>=w-25:
                r.x=w-25
                r.runXY[0]=-r.runXY[0]
            if r.y<=125:
                r.y=125
                r.runXY[1]=-r.runXY[1]
            if r.y>=h-25:
                r.y=h-25
                r.runXY[1]=-r.runXY[1]
            robot='Robot %d'%(r.id)
            name=labelfont.render(robot,True,(255,255,255))
            screen.blit(name,(r.x,r.y+20))
            printStats(r,labelfont,screen)
        pygame.display.flip()         

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                loop=False
       
        clock.tick(30)

    pygame.quit()

