#this code is used to select robots from the database and make them fight
from robot import *
from fight2 import *
import pymysql
def finalSel():
    conn=pymysql.connect(host='www.freesqldatabase.com', port=3306,
                         user='sql01_64191', passwd='**********',
                         db='sql01_6419coadaf')
    cur=conn.cursor()
    cur2=conn.cursor()
    cur.execute("select * from final where GrandWinner is NULL")
    for row in cur:
        cur2.execute("select * from robots2 where id like %d"%row[1])
        for l in cur2:
            wp1=Weapon(l[2]+1,l[3]+1,l[4]+1,1)
            hp1=Health(l[1]+1)
            r1=RobotC(l[0],random.randint(0,800),random.randint(0,600),0,hp1,wp1)
        cur2.execute("select * from robots2 where id like %d"%row[2])
        for l in cur2:
            wp2=Weapon(l[2]+1,l[3]+1,l[4]+1,1)
            hp2=Health(l[1]+1)
            r2=RobotC(l[0],random.randint(0,800),random.randint(0,600),0,hp2,wp2)
    #r1.getDetails()
    #r2.getDetails()
        winner=fight(r1,r2)
        print "Match {0}: Grand winner is {1}".format(row[0],winner)
        cur2.execute("update final set GrandWinner={0} where id={1}".format(winner,row[0]))
        cur2.execute("update robots2 set GrandTitle=GrandTitle+1 where id={0}".format(winner,row[0]))
        

