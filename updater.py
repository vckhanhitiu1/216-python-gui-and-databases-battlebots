import pymysql

conn=pymysql.connect(host='www.freesqldatabase.com', port=3306,
                    user='sql01_64191', passwd='**********',
                    db='sql01_6419coadaf')
cur=conn.cursor()

def checkR(hp,dmg,acc,range1,Rtime):
    l=cur.execute('select * from robots1 where health={0} and damage={1} and range={2} and accuracy={3}'.format(hp,dmg,range1,acc))
    if l:
        for row in cur:
            return (row[6],row[7])
    else:
        cur.execute('INSERT INTO robots1 (health, rtime, damage, range, accuracy) VALUES ({0},{1},{2},{3},{4})'.format(hp,Rtime,dmg,range1,acc))
        return (0,0)

def updateWin(hp,dmg,acc,range1):
    cur.execute("update robots1 set Wins=Wins+1 where health={0} and damage={1} and range={2} and accuracy={3}".format(hp,dmg,range1,acc))

def updateLoss(hp,dmg,acc,range1):
    cur.execute("update robots1 set Losses=Losses+1 where health={0} and damage={1} and range={2} and accuracy={3}".format(hp,dmg,range1,acc))

    

