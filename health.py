#!/usr/bin/env python
class Health(object):
    def __init__(self,level):
       self.level=level
       self.chp=level
    def update(self,hit):
       self.chp=self.chp-hit
       if self.chp>=0:
           return 1
       else:
           return 0
    def getDet(self):
        print "Total Hp:{0}, Remaining Hp:{1}".format(self.level,self.chp)
