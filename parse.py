games = []
import os
from pitch import pitch
from atBat import atBat
from game import game
import json

strikePlays = ['C','K','M','O','Q','S','T']
ballPlays = ['B','I','P','V']
activePlay = ['H','X','Y']
foulPlays = ['F','L','R']

def parseFieldPlay(fieldPlay,first,second,third,scoreDiff,outs,isBottom):
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
            if(p[1]=='X'):
                #players out
                if(p[0]=='1'):
                    first=False
                elif(p[0]=='2'):
                    second=False
                elif(p[0]=='3'):
                    third=False
                elif(p[0]=='B'):
                    ignoreBatter = True
                outs+=1
            else:#if(p[1]=='-')
                start = p[0]
                end = p[2]
                starts.append(start)
                ends.append(end)

        for start in starts:
            if(start == '1'):
                first=False
            elif(start=='2'):
                second=False
            elif(start=='3'):
                third=False 
            elif(start=='B'):
                ignoreBatter=True

        for end in ends:
            if(end == '1'):
                first=True
            elif(end=='2'):
                second=True
            elif(end=='3'):
                third=True
            else:#HOME
                if(isBottom == '1'):
                    scoreDiff += 1
                else:
                    scoreDiff -= 1  
    
    csPos = batterPlay.find('CS')
    if(csPos != -1 and batterPlay[csPos + 5] != 'E'):
        outs+=1
        runner = batterPlay[csPos+2]
        if(runner == '2'):
            first = False
        elif(runner == '3'):
            second = False
        elif(runner == 'H'):
            third = False

    poPos = batterPlay.find('PO')
    if(poPos != -1 and batterPlay[poPos + 4] != 'E'):
        outs+=1
        runner = batterPlay[poPos+2]
        if(runner == '1'):
            first = False
        elif(runner == '2'):
            second = False
        elif(runner == '3'):
            third = False
        elif(runner == 'C'):
            #runner was caught stealing
            #an out was already accounted for, so we need to subtract one
            outs-=1
            



    if(ignoreBatter == False):
        if(batterPlay[0]=='S' 
            or batterPlay[:2]=='HP' 
            or batterPlay[0]=='C' 
            or batterPlay[0]=='E'
            or batterPlay[0]=='W'):
            first = True
        elif(batterPlay[0]=='D'):
            second = True
        elif(batterPlay[0]=='T'):
            third = True
        elif(batterPlay[0]=='H'):
            if(isBottom == '1'):
                scoreDiff += 1
            else:
                scoreDiff -= 1  
    
    
                
    if(batterPlay[0].isdigit()):
        if(batterPlay.find('(')!=-1):
            while(batterPlay.find('(')!=-1):
                parenPos = batterPlay.find('(')
                runnerOut = batterPlay[parenPos+1]
                if(runnerOut == '1'):
                    first=False
                elif(runnerOut=='2'):
                    second=False
                elif(runnerOut=='3'):
                    third=False 
                elif(runnerOut=='B'):
                    outs-=1
                batterPlay=batterPlay[parenPos+3:]
                outs+=1
        outs+=1
        if(ignoreBatter):
            outs-=1
        if(fieldPlay.find('FO') != -1):
            outs -=1
    return {'first':first,'second':second,'third':third,'scoreDiff':scoreDiff,'outs':outs}               

def parseAtBat(play,prevAtBat):
    inning = play[0]
    isBottom = play[1] #top = 0, bottom = 1
    pitchPlay = play[4]
    fieldPlay = play[5]
    # print("Play",play,"Pitchplay",pitchPlay,"fieldplay",fieldPlay)
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
            try:
                prevCount = prevAtBat.getCurrentState()
                strikes = prevCount.strike
                balls = prevCount.ball
                pitches = prevAtBat.pitches
                while('.' in pitchPlay):
                    pitchPlay = pitchPlay[pitchPlay.find('.')+1:]
            except:
                print(play)
           
    if(outs >= 3):
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
        elif(p in foulPlays):
            if(strikes<3):
                strikes+=1
        elif(p not in activePlay): continue
        newPitch = pitch(balls, strikes, outs, scoreDiff, p, first, second, third, None)
        pitches.append(newPitch)
    retVals = parseFieldPlay(fieldPlay,first,second,third,scoreDiff,outs,isBottom)
    first = retVals["first"]
    second = retVals["second"]
    third = retVals["third"]
    scoreDiff = retVals["scoreDiff"]
    outs = retVals["outs"]
    # print('Strikes: {} Balls: {} Outs: {} ScoreDiff: {} Pitches: {}'.format(strikes,balls,outs,scoreDiff,pitchPlay))
    inning = isBottom + inning
    retBat = atBat(pitches,inning,first,second,third,outs,scoreDiff)
    return retBat

def createGame(gameId,atBats): 
    lastBat = atBats[-1]
    finalScore = lastBat.scoreDiff
    winner = finalScore >= 0
    newGame = game(gameId,winner,atBats,None)  
    games.append(newGame)

def readFile(f):
    with open(f) as fp:
        gameId = None
        game = []
        prevBatter = None
        
        for line in fp:
            lineDetailed = line.strip().split(',')
            if(lineDetailed[0]=='id'):
                if(gameId != None):
                    # games[gameId] = game
                    createGame(gameId,game)
                    game = []
                    prevBatter = None

                gameId = lineDetailed[1]
            if(lineDetailed[0]=='play' ):
                if(lineDetailed[6]=='NP' and lineDetailed[5] == ''): continue #ignore non-injury subs
                prevAtBat = None
                if (len(game)>0):
                    prevAtBat = game[-1]
                if(lineDetailed[5].find('.') != -1 and prevBatter == lineDetailed[3]):
                    game.pop()
                atBat = parseAtBat(lineDetailed[1:], prevAtBat)
                prevBatter = lineDetailed[3]
                game.append(atBat)
        #add final game to list
        createGame(gameId,game)

def getFilePath(file):
    filePath = os.path.join('.',"2017eve",file)
    return filePath

def testGame(f):
    with open(f) as fp:
        gameId = None
        game = []
        prevBatter = None
        for line in fp:
            lineDetailed = line.strip().split(',')
            if(lineDetailed[0]=='id'):
                gameId = lineDetailed[1]
            if(lineDetailed[0]=='play' ):
                if(lineDetailed[6]=='NP' and lineDetailed[5] == ''): continue #ignore non-injury subs
                prevAtBat = None
                if (len(game)>0):
                    prevAtBat = game[-1]
                if(lineDetailed[5].find('.') != -1 and prevBatter == lineDetailed[3]):
                    game.pop()
                atBat = parseAtBat(lineDetailed[1:], prevAtBat)
                prevBatter = lineDetailed[3]
                game.append(atBat)
        #add final game to list
        
        with(open('test.txt','w')) as testFile:
            testFile.write('Game ID: ' + gameId + '\n')
            for ab in game:
                testFile.write(str(ab) + '\n')

def writeResults(gameId):
    output = {}
    for g in games:
        gameDict = g.toDict()
        if(gameId is None or gameDict["id"]==gameId):
            output[g.id] = gameDict
    jsonOut = json.dumps(output)
    with(open('results.txt','w')) as wf:
        wf.write(jsonOut)
    



if __name__ == "__main__":
    testFile = getFilePath('TESTBOS201707180.EVA')
    readFile(getFilePath('2017BOS.EVA'))
    print(len(games))
    testGameId = None
    # testGameId = 'BOS201707180'
    writeResults(testGameId)
    testGame(testFile)
    