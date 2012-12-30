from selector import *
from finalSel import *
from Tgenround1 import *
from finalRound import *

def startT():
    clearDB()
    print "Generating round 1..."
    round1('robots2','round1')
    print "Starting round 1..."
    selector("round1","robots2")
    print "Generating round 2..."
    round1('round1','round2')
    print "Starting round 2..."
    selector('round2','robots2')
    print "Generating round 3..."
    round1('round2','round3')
    print "Starting round 3..."
    selector('round3','robots2')
    print "Generating round 4..."
    round1('round3','round4')
    print "Starting round 4..."
    selector('round4','robots2')
    print "Generating round 5..."
    round1('round4','round5')
    print "Starting round 5..."
    selector('round5','robots2')
    print "Generating semifinals..."
    round1('round5','round6')
    print "Starting semifinals..."
    selector('round6','robots2')
    print "Generating Final..."
    finalRound()
    print "Starting Final..."
    finalSel()
