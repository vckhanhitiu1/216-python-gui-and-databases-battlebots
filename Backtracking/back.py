#k - skill variable(1 health, 2 damage, 3 range, 4 accuracy)
#s - sum check
import pymysql
conn=pymysql.connect(host='www.freesqldatabase.com', port=3306,
                     user='sql01_64191', passwd='**********',
                     db='sql01_6419coadaf')
cur=conn.cursor()


def check(l):
    s=0
    for j in l:
        s+=j
    if s==6:
        cur.execute("INSERT INTO  robots2 (id ,health ,damage ,range ,accuracy)VALUES (NULL,  %d,  %d,  %d,  %d)"%(l[0],l[1],l[2],l[3]))

def back(k,l):
    if(k<4):
        for i in range(0,7):
            l[k]=i
            check(l)
            back(k+1,l)
    return 

def main():
    k=0
    l=[0]*4
    back(k,l)
    print 'Finish'
    return



main()
cur.close()
conn.close()
