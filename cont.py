from selector import *
from finalSel import *
from Tgenround1 import *
from finalRound import *
import pymysql

conn=pymysql.connect(host='www.freesqldatabase.com', port=3306,
                    user='sql01_64191', passwd='**********',
                    db='sql01_6419coadaf')
cur=conn.cursor()
cur2=conn.cursor()

def cont():
    l1=cur.execute('select GrandWinner from final')
    if l1:
        print 'Tournament has ended!'
    else:
#==============Check first round=========
        l1=cur.execute('select * from robots2')
        l2=cur2.execute('select * from round1')
        l1+=1
        if l1/2==l2:
            print "Starting round 1...."
            selector("round1","robots2")
            
        else:
            print "Generating round 1..."
            round1('robots2','round1')
            print "Starting round 1...."
            selector("round1","robots2")
#=============Check second round==========
        l1=cur.execute('select * from round1')
        l2=cur2.execute('select * from round2')
        l1+=1
        if l1/2==l2:
            print "Starting round 2..."
            selector('round2','robots2')
        else:
            print "Generating round 2..."
            round1('round1','round2')
            print "Starting round 2..."
            selector('round2','robots2')
#==============Check third round==========
        l1=cur.execute('select * from round2')
        l2=cur2.execute('select * from round3')
        l1+=1
        if l1/2==l2:
            print "Starting round 3..."
            selector('round3','robots2')
        else:
            print "Generating round 3..."
            round1('round2','round3')
            print "Starting round 3..."
            selector('round3','robots2')
#==============Check forth round==========
        l1=cur.execute('select * from round3')
        l2=cur2.execute('select * from round4')
        l1+=1
        if l1/2==l2:
            print "Starting round 4..."
            selector('round4','robots2')
        else:
            print "Generating round 4..."
            round1('round3','round4')
            print "Starting round 4..."
            selector('round4','robots2')
#===============Check fifth round=========
        l1=cur.execute('select * from round4')
        l2=cur2.execute('select * from round5')
        l1+=1
        if l1/2==l2:
            print "Starting round 5..."
            selector('round5','robots2')
        else:
            print "Generating round 5..."
            round1('round4','round5')
            print "Starting round 5..."
            selector('round5','robots2')
#===============Check sixth round==========
        l1=cur.execute('select * from round5')
        l2=cur2.execute('select * from round6')
        l1+=1
        if l1/2==l2:
            print 'Starting semifinals...'
            selector('round6','robots2')
        else:
            print 'Generating semifinals...'
            round1('round5','round6')
            print 'Starting round 6...'
            selector('round6','robots2')
#===============Check final round==========
        l1=cur.execute('select * from round6')
        l2=cur2.execute('select * from final')
        l1+=1
        if l1/2==l2:
            print 'Starting final...'
            finalSel()
        else:
            print 'Generatin final...'
            finalRound()
            print 'Starting final...'
            finalSel()


