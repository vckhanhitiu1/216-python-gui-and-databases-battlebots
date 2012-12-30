#================Tournament generator=========
#Generate the matches for the robots
import random
import pymysql


  
def check(l):
    ok=0
    for i in l:
        if i==1:
            ok=1
    return ok
        
def generate(l,cur,lenght,table2,table1):
#==================Robot1 ==========================
    r1=random.randint(1,lenght)
    if(l[r1]==1): #check oponent to see if available
        l[r1]=0
    else:
        while (l[r1]==0): #keep looking for an available robot
            r1=random.randint(1,lenght)
    l[r1]=0
    cur.execute("select winner from {0} where id={1}".format(table1,r1))
    for idRob in cur:
        r1=idRob[0]
#==================Robot2 ==========================
    if check(l)==0:
        r2=random.randint(1,lenght)
       
    else :           
        r2=random.randint(1,lenght)
        if(l[r2]==1): #check oponent to see if available
            l[r2]=0
        else:
            while (l[r2]==0): #keep looking for a second robot
                r2=random.randint(1,lenght)
        l[r2]=0
        if table1!='robots2':
            cur.execute("select winner from {0} where id={1}".format(table1,r2))
            for idRob in cur:
                r2=idRob[0]
    cur.execute("INSERT INTO  {0} (id , robot1, robot2) VALUES (NULL,  {1}, {2})".format(table2,r1,r2))

    return check(l)

def round1(table1,table2):
    conn=pymysql.connect(host='www.freesqldatabase.com', port=3306,
                    user='sql01_64191', passwd='cr1mina',
                    db='sql01_6419coadaf')
    cur=conn.cursor()
    lenght=cur.execute("select * from {0}".format(table1))
    l=[1]*(lenght+1) #store if a robot has a match already planned
    l[0]=0
    loop=generate(l,cur,lenght,table2,table1)
    while(loop):
        loop=generate(l,cur,lenght,table2,table1)
    print "===The END==="

def clearDB():
    conn=pymysql.connect(host='www.freesqldatabase.com', port=3306,
                    user='sql01_64191', passwd='cr1mina',
                    db='sql01_6419coadaf')
    cur=conn.cursor()
    cur.execute("TRUNCATE TABLE  round1")
    cur.execute("TRUNCATE TABLE  round2")
    cur.execute("TRUNCATE TABLE  round3")
    cur.execute("TRUNCATE TABLE  round4")
    cur.execute("TRUNCATE TABLE  round5")
    cur.execute("TRUNCATE TABLE  round6")
    cur.execute("TRUNCATE TABLE  final")
    
    
