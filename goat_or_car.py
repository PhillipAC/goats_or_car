import random

random.seed()

winNoSwitch = 0
winSwitch = 0

for i in xrange(1000):

    door = random.randint(0,2)
    choice = random.randint(0,2)
    
    if door != 0 and choice != 0:
        show = 0
    elif door !=1 and choice != 1:
        show = 1
    else:
        show = 2
        
    if show != 0 and choice != 0:
        switch = 0
    elif show != 1 and choice != 1:
        switch = 1
    else:
        switch = 2
        
    if door == choice:
        print "You got it without switching"
        winNoSwitch+=1
    elif door == switch:
        print "You got it by switching"
        winSwitch+=1

print "You won without switching " + str(winNoSwitch)
print "You won with swtiching " + str(winSwitch)