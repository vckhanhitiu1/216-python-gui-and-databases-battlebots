import sys
import pygame
import pymysql

conn=pymysql.connect(host='www.freesqldatabase.com', port=3306,
                     user='sql01_64191', passwd='**********',
                     db='sql01_6419coadaf')
cur=conn.cursor()


def listChampions(screen,labelfont):
    cur.execute("select * from robots2 where GrandTitle>0 order by GrandTitle desc LIMIT 0,3")
    i=0
    for l in cur:
          i+=1
          robot='Robot %d'%(l[0])
          name=labelfont.render(robot,True,(255,255,255))
          weaponDet='Weapon: {0} dmg, {1} range, {2}% acc, {3} seconds load time'.format(l[2]+1,l[3]+1,(l[4]+1)*10,1)
          weapon=labelfont.render(weaponDet,True,(255,255,255))
          hpDet='Hp: {0} total Hp'.format(l[1]+1)
          hp=labelfont.render(hpDet,True,(255,255,255))
          titleDet='Titles: {0} Tournament Titles'.format(l[5])
          title=labelfont.render(titleDet,True,(255,255,255))
          screen.blit(name,(20,i*100+40))
          screen.blit(weapon,(20,i*100+55))
          screen.blit(hp,(20,i*100+70))
          screen.blit(title,(20,i*100+85))

def hof():
    pygame.init()
    
    background = pygame.image.load("champs.bmp")
    backgroundRect = background.get_rect()
    
    size = (width, height) = background.get_size()
    screen = pygame.display.set_mode(size)
    labelfont=pygame.font.Font("C:\\Windows\\Fonts\\ARIALN.TTF", 14)
    while 1:
         for event in pygame.event.get():
              if event.type == pygame.QUIT: pygame.quit()

         screen.blit(background, backgroundRect)
         listChampions(screen,labelfont)
         pygame.display.flip()
