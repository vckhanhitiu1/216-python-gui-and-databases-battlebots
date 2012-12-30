#================Tournament generator=========
#Generate the matches for the robots
import random
import pymysql


conn=pymysql.connect(host='www.freesqldatabase.com', port=3306,
                    user='sql01_64191', passwd='**********',
                    db='sql01_6419coadaf')
cur=conn.cursor()
cur2=conn.cursor()
lenght=cur.execute("select * from round6")
    
def check(l):
    ok=0
    for i in l:
        if i==1:
            ok=1
    return ok
            
def generate(l):
    r1=random.randint(1,lenght)
    if(l[r1]==1): #check oponent to see if available
        l[r1]=0
    else:
        while (l[r1]==0): #keep looking for an available robot
            r1=random.randint(1,lenght)
    l[r1]=0
    cur2.execute("select winner from round6 where id={0}".format(r1))
    for idRob in cur2:
        r1=idRob[0]
    r2=random.randint(1,lenght)
    if(l[r2]==1): #check oponent to see if available
        l[r2]=0
    else:
        while (l[r2]==0): #keep looking for a second robot
            r2=random.randint(1,lenght)
    l[r2]=0
    cur2.execute("select winner from round6 where id={0}".format(r2))
    for idRob in cur2:
        r2=idRob[0]
    cur.execute("INSERT INTO  final (robot1, robot2) VALUES (%d,  %d)"%(r1,r2))

    return check(l)



def finalRound():
    cur.execute("TRUNCATE TABLE  final")
    l=[1]*(lenght+1) #store if a robot has a match already planned
    l[0]=0
    loop=generate(l)
    while(loop):
        loop=generate(l)
    print "===The END==="
