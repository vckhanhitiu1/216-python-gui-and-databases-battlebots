#!/usr/bin/env python
class Weapon(object):
    def __init__(self,dmg,acc,range,rtime):
        self.dmg=dmg
        self.acc=acc
        self.range=range
        self.rtime=rtime
    def getDet(self):
        print "Dmg: {0}, Acc: {1}, Range:{2}, R-Time:{3}".format(
            self.dmg,self.acc,self.range,self.rtime)