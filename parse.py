pitches = []
import os
from pitch import pitch
from atBat import atBat
from game import game
from status import status
import mango
import json

strikePlays = ['C','K','L','M','O','Q','S','T']
ballPlays = ['B','I','P','V']
activePlay = ['H','X','Y']
foulPlays = ['F','R']
gameStatus = status()

def parseFieldPlay(fieldPlay,isBottom):
    slashPos = fieldPlay.find('/')
    periodPos = fieldPlay.find('.')
    batterPlay = fieldPlay
    runnerPlay = None
    ignoreBatter = False

    if(slashPos > -1):
        batterPlay=batterPlay[:slashPos]

    if(periodPos != -1):
        runnerPlay = fieldPlay[periodPos+1:]
        runPlays = runnerPlay.split(';')

        starts = []
        ends = []
        for p in runPlays:
            if(p[1]=='X' and p.find('E')==-1):
                #players out
                if(p[0]=='1'):
                    gameStatus.first=False
                elif(p[0]=='2'):
                    gameStatus.second=False
                elif(p[0]=='3'):
                    gameStatus.third=False
                elif(p[0]=='B'):
                    ignoreBatter = True
                gameStatus.out+=1
            else:#if(p[1]=='-')
                start = p[0]
                end = p[2]
                starts.append(start)
                ends.append(end)

        for start in starts:
            if(start == '1'):
                gameStatus.first=False
            elif(start=='2'):
                gameStatus.second=False
            elif(start=='3'):
                gameStatus.third=False 
            elif(start=='B'):
                ignoreBatter=True

        for end in ends:
            if(end == '1'):
                gameStatus.first=True
            elif(end=='2'):
                gameStatus.second=True
            elif(end=='3'):
                gameStatus.third=True
            else:#HOME
                if(isBottom == '1'):
                    gameStatus.scoreDiff += 1
                else:
                    gameStatus.scoreDiff -= 1  
    
    csPos = batterPlay.find('CS')
    if(csPos != -1 and batterPlay.find('E') == -1):
        gameStatus.out+=1
        runner = batterPlay[csPos+2]
        if(runner == '2'):
            gameStatus.first = False
        elif(runner == '3'):
            gameStatus.second = False
        elif(runner == 'H'):
            gameStatus.third = False

    poPos = batterPlay.find('PO')
    if(poPos != -1 and batterPlay[poPos + 4] != 'E'):
        gameStatus.out+=1
        runner = batterPlay[poPos+2]
        if(runner == '1'):
            gameStatus.first = False
        elif(runner == '2'):
            gameStatus.second = False
        elif(runner == '3'):
            gameStatus.third = False
        elif(runner == 'C'):
            #runner was caught stealing
            #an out was already accounted for, so we need to subtract one
            gameStatus.out-=1
            
    if(ignoreBatter == False):
        if(batterPlay[0]=='S' 
            or batterPlay[:2]=='HP'  
            or batterPlay[:2]=='FC' 
            or batterPlay[0]=='C' and len(batterPlay) == 1 
            or batterPlay[0]=='E'
            or batterPlay[:2]=='IW' 
            or batterPlay[0]=='W'):
            gameStatus.first = True
        elif(batterPlay[0]=='D'):
            gameStatus.second = True
        elif(batterPlay[0]=='T'):
            gameStatus.third = True
        elif(batterPlay[0]=='H'):
            if(isBottom == '1'):
                gameStatus.scoreDiff += 1
            else:
                gameStatus.scoreDiff -= 1 
        elif(batterPlay[0]=='K'):
            gameStatus.out += 1 
                
    if(batterPlay[0].isdigit() and batterPlay.find('E')!=1):
        if(batterPlay.find('(')!=-1):
            if(batterPlay.count('(')==2 and batterPlay.find('B')==-1):
                gameStatus.out-=1
            while(batterPlay.find('(')!=-1):
                parenPos = batterPlay.find('(')
                runnerOut = batterPlay[parenPos+1]
                if(runnerOut == '1'):
                    gameStatus.first=False
                elif(runnerOut=='2'):
                    gameStatus.second=False
                elif(runnerOut=='3'):
                    gameStatus.third=False 
                elif(runnerOut=='B'):
                    gameStatus.out-=1
                batterPlay=batterPlay[parenPos+3:]
                gameStatus.out+=1
        gameStatus.out+=1
        if(ignoreBatter or fieldPlay.find('FO')!= -1):
            gameStatus.out-=1
            gameStatus.first = True
    
def parseAtBat(play):
    inning = play[0] if int(play[0]) < 10 else '9+'
    inning = play[1] + inning
    isBottom = play[1] #top = 0, bottom = 1
    batter = play[2]
    pitchPlay = play[4]
    
    fieldPlay = play[5]
    # print("Play",play,"Pitchplay",pitchPlay,"fieldplay",fieldPlay)
    retPitches = []
    if(gameStatus.prevBatter == batter):
        try:
            
            while('.' in pitchPlay):
                pitchPlay = pitchPlay[pitchPlay.find('.')+1:]
        except Exception as e:
            print(play, e)
    else:
        gameStatus.newBatter()
           
    if(gameStatus.out >= 3):
        gameStatus.newInning()

    for p in pitchPlay:
        prevStatus = gameStatus.duplicateStatus()  
        if(p in strikePlays):
            gameStatus.strike +=1              

        elif(p in ballPlays):
            gameStatus.ball+=1
        elif(p in foulPlays):            
            if(gameStatus.strike<2):
                gameStatus.strike+=1
            
        elif(p not in activePlay): continue
        newPitch = pitch(prevStatus.ball, prevStatus.strike, prevStatus.out, prevStatus.scoreDiff, p, prevStatus.first, prevStatus.second, prevStatus.third, inning)
        
        retPitches.append(newPitch)

    parseFieldPlay(fieldPlay,isBottom)
    
    if(gameStatus.out > 3):
        print(",".join(play), "4 outs recorded")
        print(gameStatus)

    return retPitches

def createGame(gameId,game): 
    lastBat = game[-1]
    finalScore = lastBat.scoreDiff
    winner = finalScore >= 0
    for index,pitch in enumerate(game):
        pitch.winningTeam = winner
        pitch.id = gameId + str(index)
        pitches.append(pitch)

def readFile(f):
    with open(f) as fp:
        gameId = None
        game = []
        
        for line in fp:
            lineDetailed = line.strip().split(',')
            if(lineDetailed[0]=='id'):
                gameStatus.clear()
                if(gameId != None):
                    # games[gameId] = game
                    createGame(gameId,game)
                    game = []

                gameId = lineDetailed[1]
            if(lineDetailed[0]=='play' ):
                if(lineDetailed[6]=='NP' and lineDetailed[5] == ''): continue #ignore non-injury subs
                retPitches = parseAtBat(lineDetailed[1:])
                prevBatter = lineDetailed[3]
                game.extend(retPitches)
        #add final game to list
        createGame(gameId,game)

def getFilePath(file):
    filePath = os.path.join('.',"2017eve",file)
    return filePath

def writeResults():
    output = []
    count = 0
    for p in pitches:
        output.append(p.toDict())
    jsonOut = json.dumps(output)
    with(open('results.json','w')) as wf:
        wf.write(jsonOut)
    

if __name__ == "__main__":
    for file in os.listdir("./2017eve"):
        if file.endswith(".EVA") or file.endswith(".EVN"):
            readFile(getFilePath(file))
    print(len(pitches))
    writeResults()
    mango.loadData()