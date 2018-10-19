games = {}
import os
from pitch import pitch
from atBat import atBat

strikePlays = ['C','K','M','O','Q','S','T']
ballPlays = ['B','I','P','V']
activePlay = ['H','X','Y']

def parseFieldPlay(fieldPlay,first,second,third,scoreDiff,outs,isBottom):
    slashPos = fieldPlay.find('/')
    periodPos = fieldPlay.find('.')
    batterPlay = fieldPlay
    runnerPlay = None
    batterOut = False

    if(slashPos > -1):
        batterPlay=batterPlay[:slashPos]

    if(periodPos != -1):
        runnerPlay = fieldPlay[periodPos+1:]
        runPlays = runnerPlay.split(';')

        starts = []
        ends = []
        for p in runPlays:
            if(p[1]=='X'):
                #players out
                if(p[0]==1):
                    first=False
                elif(p[0]==2):
                    second=False
                elif(p[0]==3):
                    third=False
                elif(p[0]=='B'):
                    batterOut = True
                outs+=1
            else:#if(p[1]=='-')
                start = p[0]
                end = p[2]
                starts.append(start)
                ends.append(end)

        for start in starts:
            if(start == 1):
                first=False
            elif(start==2):
                second=False
            elif(start==3):
                third=False 
        for end in ends:
            if(end == 1):
                first=True
            elif(end==2):
                second=True
            elif(end==3):
                third=True
            else:#HOME
                if(isBottom == '1'):
                    scoreDiff += 1
                else:
                    scoreDiff -= 1  

    return {'first':first,'second':second,'third':third,'scoreDiff':scoreDiff,'outs':outs}               

def parseAtBat(play,prevAtBat):
    inning = play[0]
    isBottom = play[1] #top = 0, bottom = 1
    pitchPlay = play[4]
    fieldPlay = play[5]
    pitches = []
    strikes = 0
    balls = 0
    
    outs = 0
    scoreDiff = 0
    first = False
    second = False 
    third = False

   
    if(prevAtBat != None):
        outs = prevAtBat.outs
        scoreDiff = prevAtBat.scoreDiff
        first = prevAtBat.first
        second = prevAtBat.second
        third = prevAtBat.third
        if('.' in pitchPlay):
            prevCount = prevAtBat.getCurrentState()
            strikes = prevCount.strikes
            balls = prevCount.balls
            pitches = prevCount.pitches
            while('.' in pitchPlay):
                pitchPlay = pitchPlay[pitchPlay.find('.')+1:]
    if(outs == 3):
        outs = 0
        first = False
        second = False
        third = False

    for p in pitchPlay:
        if(p in strikePlays):
            strikes +=1
            if (strikes == 3):
                outs += 1
        elif(p in ballPlays):
            balls+=1
        elif(p not in activePlay): continue
        newPitch = pitch(balls, strikes, outs, scoreDiff, p, first, second, third, None)
        pitches.append(newPitch)
    retVals = parseFieldPlay(fieldPlay,first,second,third,scoreDiff,outs,isBottom)
    first = retVals["first"]
    second = retVals["second"]
    third = retVals["third"]
    scoreDiff = retVals["scoreDiff"]
    outs = retVals["outs"]
    print('Strikes: {} Balls: {} Outs: {} ScoreDiff: {} Pitches: {}'.format(strikes,balls,outs,scoreDiff,pitchPlay))
    retBat = atBat()
    
def readFile(f):
    with open(f) as fp:
        gameId = None
        game = []
        for line in fp:
            lineDetailed = line.strip().split(',')
            if(lineDetailed[0]=='id'):
                if(gameId != None):
                    games[gameId] = game
            if(lineDetailed[0]=='play'):
                if(lineDetailed[6]=='NP' and lineDetailed[5] == ''): continue #ignore non-injury subs
                prevAtBat = None
                if (len(game)>0):
                    prevAtBat = game[-1]
                if(lineDetailed[5].find('.') != -1):
                    game.pop()
                atBat = parseAtBat(lineDetailed[1:], prevAtBat)
                game.append(atBat)

filePath = os.path.join('.',"2017eve","2017BOS.EVA")
readFile(filePath)

