#this code is used to select robots from the database and make them fight
from robot import *
from fight2 import *
import pymysql

def selector(table1,table2):
    conn=pymysql.connect(host='www.freesqldatabase.com', port=3306,
                         user='sql01_64191', passwd='**********',
                         db='sql01_6419coadaf')
    cur=conn.cursor()
    cur2=conn.cursor()
    cur.execute("select * from {0} where winner is NULL".format(table1))
    for row in cur:
        cur2.execute("select * from {0} where id like {1}".format(table2,row[1]))
        for l in cur2:
            wp1=Weapon(l[2]+1,l[3]+1,l[4]+1,1)
            hp1=Health(l[1]+1)
            r1=RobotC(l[0],random.randint(0,800),random.randint(0,600),0,hp1,wp1)
        cur2.execute("select * from {0} where id like {1}".format(table2,row[2]))
        for l in cur2:
            wp2=Weapon(l[2]+1,l[3]+1,l[4]+1,1)
            hp2=Health(l[1]+1)
            r2=RobotC(l[0],random.randint(0,800),random.randint(0,600),0,hp2,wp2)
    #r1.getDetails()
    #r2.getDetails()
        winner=fight(r1,r2)
        print "Match {0}: winner is {1}".format(row[0],winner)
        cur2.execute("update {0} set winner={1} where id={2}".format(table1,winner,row[0]))

    
