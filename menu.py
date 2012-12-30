from Tkinter import *
#import battlebots game logics
from battleBots import *
from updater import *
from cont import *
from start import *
import sys
from hof import *

class GridApp:
    def __init__(self, parent=0):
        self.mainframe = Frame(parent)
        leftframe=Frame(self.mainframe)
        leftframe.grid(row=0,column=0)
        midframe=Frame(self.mainframe)
        midframe.grid(row=0,column=2)
        rightframe=Frame(self.mainframe)
        rightframe.grid(row=0,column=4)
#Storage variables
        self.hp1=1
        self.dmg1=1
        self.acc1=2
        self.range1=1
        self.Rtime1=1
        self.hp2=1
        self.dmg2=1
        self.acc2=2
        self.range2=1
        self.Rtime2=1
        self.lock1=False
        self.lock2=False
        self.robWin='No battle yet'
#Title widgets creation
        self.Robot1=Label(leftframe,text='Robot 1',background = 'WHITE')
        self.Robot2=Label(midframe,text='Robot 2',background = 'WHITE')
        self.Arena=Label(rightframe, text='BattleBots Arena',background = 'WHITE')
        self.tournament=Label(rightframe, text='Tournament', bg='WHITE')
#Position title widgets
        self.Robot1.grid(row=0,column=0,columnspan=2, sticky=NSEW)
        self.Robot2.grid(row=0,column=0,columnspan=2, sticky=NSEW)
        self.Arena.grid(row=0,column=0,columnspan=5, sticky=NSEW)
        self.tournament.grid(row=4,column=0,columnspan=5,sticky=NSEW)
#Buton and label widgets for robot1
        self.hp1B=Button(leftframe,text='Hp:',command=self.hp1UP)
        self.hp1Value=Label(leftframe,text='%d'%(self.hp1))
        self.dmg1B=Button(leftframe,text='Damage:',command=self.dmg1UP)
        self.dmg1Value=Label(leftframe,text='%d'%(self.dmg1))
        self.acc1B=Button(leftframe,text='Accuracy:',command=self.acc1UP)
        self.acc1Value=Label(leftframe,text='%d'%(self.acc1))
        self.range1B=Button(leftframe,text='Range:',command=self.range1UP)
        self.range1Value=Label(leftframe,text='%d'%(self.range1))
        self.lock1B=Button(leftframe,text='Lock',command=self.lockR1,bg='red')
        self.reset1=Button(leftframe,text='Reset',command=self.reset1UP)
        self.pts1=self.hp1+self.dmg1+self.acc1+self.range1-4
        self.points1=Label(leftframe,text='Points used: {0}\n Weapon load time: {1}'.format(self.pts1,self.Rtime1))
#Button and label widgets robot2
        self.hp2B=Button(midframe,text='Hp:',command=self.hp2UP)
        self.hp2Value=Label(midframe,text='%d'%(self.hp2))
        self.dmg2B=Button(midframe,text='Damage:',command=self.dmg2UP)
        self.dmg2Value=Label(midframe,text='%d'%(self.dmg2))
        self.acc2B=Button(midframe,text='Accuracy:',command=self.acc2UP)
        self.acc2Value=Label(midframe,text='%d'%(self.acc2))
        self.range2B=Button(midframe,text='Range:',command=self.range2UP)
        self.range2Value=Label(midframe,text='%d'%(self.range2))
        self.lock2B=Button(midframe,text='Lock',command=self.lockR2,bg='red')
        self.reset2=Button(midframe,text='Reset',command=self.reset2UP)
        self.pts2=self.hp2+self.dmg2+self.acc2+self.range2-4
        self.points2=Label(midframe,text='Points used: {0}\n Weapon load time: {1}'.format(self.pts2,self.Rtime2))
#Button and label widgets for Arena Control
        self.fight=Button(rightframe, text='Fight!',command=self.launch,bg='red')
        self.label1=Label(rightframe,text='--->')
        self.label2=Label(rightframe,text='    <---  ')
        self.exit=Button(rightframe, text='  Exit  ',command=self.quitGame)
        self.winner=Label(rightframe,text='   Winner is: \n {0}'.format(self.robWin))


#Button widgets for Tournament
        self.Start=Button(rightframe,text='Start!',command=startT)
        self.Continue=Button(rightframe,text='Continue',command=cont)
        self.seeWinners=Button(rightframe,text='See winners',command=hof)
        

#Position robot1 widgets
        self.hp1B.grid(row=1,column=0, sticky=NSEW)
        self.hp1Value.grid(row=1,column=1, sticky=NSEW)
        self.dmg1B.grid(row=2,column=0, sticky=NSEW)
        self.dmg1Value.grid(row=2,column=1, sticky=NSEW)
        self.acc1B.grid(row=3,column=0, sticky=NSEW)
        self.acc1Value.grid(row=3,column=1, sticky=NSEW)
        self.range1B.grid(row=4,column=0, sticky=NSEW)
        self.range1Value.grid(row=4,column=1, sticky=NSEW)
        self.points1.grid(row=5,column=0, columnspan=2)
        self.lock1B.grid(row=6,column=0, sticky=NSEW)
        self.reset1.grid(row=6,column=1, sticky=NSEW)

#Position robot2 widgets
        self.hp2B.grid(row=1,column=0, sticky=NSEW)
        self.hp2Value.grid(row=1,column=1, sticky=NSEW)
        self.dmg2B.grid(row=2,column=0, sticky=NSEW)
        self.dmg2Value.grid(row=2,column=1, sticky=NSEW)
        self.acc2B.grid(row=3,column=0, sticky=NSEW)
        self.acc2Value.grid(row=3,column=1, sticky=NSEW)
        self.range2B.grid(row=4,column=0, sticky=NSEW)
        self.range2Value.grid(row=4,column=1, sticky=NSEW)
        self.points2.grid(row=5,column=0, columnspan=2)
        self.lock2B.grid(row=6,column=0, sticky=NSEW)
        self.reset2.grid(row=6,column=1, sticky=NSEW)
        
#Position Arena widgets
        self.fight.grid(row=1,column=1,columnspan=3,sticky=NSEW)
        self.label1.grid(row=1,column=0,sticky=NSEW)
        self.exit.grid(row=2,column=1,columnspan=3,sticky=NSEW)
        self.label2.grid(row=1,column=4,sticky=NSEW)
        self.winner.grid(row=3,column=1,columnspan=3,sticky=NSEW)

#Position Tournament Buttons
        self.Start.grid(row=5,column=0,columnspan=2,sticky=NSEW)
        self.Continue.grid(row=5,column=3,columnspan=2,sticky=NSEW)
        self.seeWinners.grid(row=6,column=1,columnspan=3, sticky=NSEW)

# Position the widgets within the frame
        xsize, ysize = leftframe.grid_size()
        for i in range(0, ysize):
            leftframe.grid_rowconfigure(i, minsize=50, weight=1)
            midframe.grid_rowconfigure(i, minsize=50, weight=1)
            rightframe.grid_rowconfigure(i, minsize=50, weight=1)
        for i in range(xsize):
            leftframe.grid_columnconfigure(i, minsize=50, weight=1)
            midframe.grid_columnconfigure(i, minsize=50, weight=1)            
            rightframe.grid_columnconfigure(i, minsize=50, weight=1)
# set up the main window
        self.mainframe.grid()
# set the title
        self.mainframe.master.title("Battle Bots Arena")

#update functions for robot1 labels
    def hp1UP(self):
        if self.pts1<14:
            self.hp1+=1
            self.hp1Value.configure(text='%d'%(self.hp1))
            self.hp1Value.update_idletasks()
            self.points1UP()
        
    def dmg1UP(self):
        if self.pts1<14:
            self.dmg1+=1
            self.dmg1Value.configure(text='%d'%(self.dmg1))
            self.dmg1Value.update_idletasks()
            self.points1UP()
        
    def acc1UP(self):
        if self.pts1<14 and self.acc1<9:
            self.acc1+=1
            self.acc1Value.configure(text='%d'%(self.acc1))
            self.acc1Value.update_idletasks()
            self.points1UP()

    def range1UP(self):
        if self.pts1<14:
            self.range1+=1
            self.range1Value.configure(text='%d'%(self.range1))
            self.range1Value.update_idletasks()
            self.points1UP()

    def points1UP(self):
        self.pts1=self.hp1+self.dmg1+self.range1+self.acc1-4
        if self.pts1>6:
            self.Rtime1=self.pts1-6+1
            self.lock1Green()
        elif self.pts1==6:
            self.lock1Green()
        self.points1.configure(text='Points used: {0}\n Weapon load time: {1}'.format(self.pts1,self.Rtime1))
        self.points1.update_idletasks()

    def reset1UP(self):
        self.hp1=1
        self.dmg1=1
        self.acc1=2
        self.range1=1
        self.Rtime1=1
        self.lock1=False
        self.hp1Value.configure(text='%d'%(self.hp1))
        self.hp1Value.update_idletasks()        
        self.dmg1Value.configure(text='%d'%(self.dmg1))
        self.dmg1Value.update_idletasks()
        self.acc1Value.configure(text='%d'%(self.acc1))
        self.acc1Value.update_idletasks()
        self.range1Value.configure(text='%d'%(self.range1))
        self.range1Value.update_idletasks()
        self.lock1B.configure(bg='red')
        self.lock1B.update_idletasks()
        self.fightUP()
        self.points1UP()

    def lock1Green(self):
        self.lock1B.configure(bg='green')
        self.lock1B.update_idletasks()

#update functions for robot2 labels
    def hp2UP(self):
        if self.pts2<14:
            self.hp2+=1
            self.hp2Value.configure(text='%d'%(self.hp2))
            self.hp2Value.update_idletasks()
            self.points2UP()
        
    def dmg2UP(self):
        if self.pts2<14:
            self.dmg2+=1
            self.dmg2Value.configure(text='%d'%(self.dmg2))
            self.dmg2Value.update_idletasks()
            self.points2UP()
        
    def acc2UP(self):
        if self.pts2<14 and self.acc2<9:
            self.acc2+=1
            self.acc2Value.configure(text='%d'%(self.acc2))
            self.acc2Value.update_idletasks()
            self.points2UP()

    def range2UP(self):
        if self.pts2<14:
            self.range2+=1
            self.range2Value.configure(text='%d'%(self.range2))
            self.range2Value.update_idletasks()
            self.points2UP()

    def points2UP(self):
        self.pts2=self.hp2+self.dmg2+self.range2+self.acc2-4
        if self.pts2>6:
            self.Rtime2=self.pts2-6+1
            self.lock2Green()
        elif self.pts2==6:
            self.lock2Green()
        self.points2.configure(text='Points used: {0}\n Weapon load time: {1}'.format(self.pts2,self.Rtime2))
        self.points2.update_idletasks()

    def reset2UP(self):
        self.hp2=1
        self.dmg2=1
        self.acc2=2
        self.range2=1
        self.Rtime2=1
        self.lock2=False
        self.hp2Value.configure(text='%d'%(self.hp2))
        self.hp2Value.update_idletasks()        
        self.dmg2Value.configure(text='%d'%(self.dmg2))
        self.dmg2Value.update_idletasks()
        self.acc2Value.configure(text='%d'%(self.acc2))
        self.acc2Value.update_idletasks()
        self.range2Value.configure(text='%d'%(self.range2))
        self.range2Value.update_idletasks()
        self.lock2B.configure(bg='red')
        self.lock2B.update_idletasks()
        self.fightUP()
        self.points2UP()

    def lock2Green(self):
        self.lock2B.configure(bg='green')
        self.lock2B.update_idletasks()

#Fight button gets red after each fight
    def fightRed(self):
        self.fight.configure(bg='red')
        self.fight.update_idletasks()

#Battle bots arena buttons functions
    def lockR1(self):
        if self.pts1>=6:
            wins,losses=checkR(self.hp1,self.dmg1,self.acc1,self.range1,self.Rtime1)
            setR1(self.hp1,self.dmg1,self.acc1,self.range1,self.Rtime1,wins,losses)
            self.lock1=True
            self.lock1B.configure(bg='yellow')
            self.lock1B.update_idletasks()
            self.fightUP()

    def lockR2(self):
        if self.pts2>=6:
            wins,losses=checkR(self.hp2,self.dmg2,self.acc2,self.range2,self.Rtime2)
            setR2(self.hp2,self.dmg2,self.acc2,self.range2,self.Rtime2,wins,losses)
            self.lock2=True
            self.lock2B.configure(bg='yellow')
            self.lock2B.update_idletasks()
            self.fightUP()

        
    def launch(self):
        if self.lock1==True and self.lock2==True:
            self.robWin=fightArena()
            if self.robWin=='Robot 1':
                updateWin(self.hp1,self.dmg1,self.acc1,self.range1)
                updateLoss(self.hp2,self.dmg2,self.acc2,self.range2)
            elif self.robWin=='Robot 2':
                updateWin(self.hp2,self.dmg2,self.acc2,self.range2)
                updateLoss(self.hp1,self.dmg1,self.acc1,self.range1)
            self.winner.configure(text='   Winner is: \n {0}'.format(self.robWin),bg='cyan')
            self.winner.update_idletasks()
            self.lock1=False
            self.lock2=False
            self.lock1Green()
            self.lock2Green()
            self.fightRed()

    def fightUP(self):
        if self.lock1==True and self.lock2==True:
            self.fight.configure(bg='green')
        else:
            self.fight.configure(bg='red')

    def quitGame(self):
        sys.exit()

#instantiate the GridApp class
app = GridApp()
app.mainframe.mainloop()

