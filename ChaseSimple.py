import random as rand

def chaseSimple(impSpd, golemSpd, headStart, exitPosition)->bool:
    """Golem and the imp function"""
    
    #golem starts at 0
    gPos = 0
    
    #imp starts at headStart
    iPos = headStart
    
    #Get tuple values
    minGolSpd = golemSpd[0]
    maxGolSpd = golemSpd[1]
    minImpSpd = impSpd[0]
    maxImpSpd = impSpd[1]
    
    
    #if any input is negative return false
    if headStart < 0 or exitPosition < 0 or minGolSpd < 0 or maxGolSpd < 0 or minImpSpd < 0 or maxImpSpd < 0:
        return False
    
    #loop runs until golem catches up to imp or imp escapes
    while gPos < iPos and iPos < exitPosition:
        #golem moves forward in the range, golemSpd feet
        gPos += rand.randrange(minGolSpd, maxGolSpd + 1)
        #imp moves forward in range impSpd feet
        iPos += rand.randrange(minImpSpd, maxImpSpd + 1)
        
    #if the golem's position is greater than or equal to the imp's
    if gPos >= iPos:
        return False
    else:
        return True
    