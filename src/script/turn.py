
turn = 0
raizCount = 0
callCount = 0

def turnCheck(playerList):
    if(raizCount == 1 and callCount == len(playerList)-1):
        turn += 1
        raizCount = 0
        callCount = 0