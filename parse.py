games = {}
import os

strikePlays = ['C','K','M','O','Q','S','T']
ballPlays = ['B','I','P','V']

def advanceRunners(batter,firstBase,secondBase,thirdBase, count)
{
    runsScored = 0
    curCount = 0
    while count <= curCount:
        if thirdBase == true:
            thirdBase = false
            runsScored += 1
        if secondBase == true:
            secondBase = false
            thirdBase = true
        if firstBase == true:
            firstBase == false:
            secondBase = true
        if batter == true:
            batter = false
            firstBase = true
        curCount += 1
    return rundiff
}

def parsePlay(play,prevPlay):
    pitchPlay = play[4]
    fieldPlay = play[5]

    strikes = 0
    balls = 0
    outs = 0
    for p in pitchPlay:
        if(p in strikePlays):
            strikes +=1
            if (strikes == 3):
                outs += 1
        if(p in ballPlays):
            balls+=1
            if(balls == 4):
                pass#advance runners
    print('Strikes: {} Balls: {} Outs: {} Pitches: {}'.format(strikes,balls,outs,pitchPlay))
    
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
                prevPlay = None
                if (len(game)>0):
                    prevPlay = game[-1]
                parsePlay(lineDetailed[1:], prevPlay)
#os.path.join('app', 'subdir', 'dir', 'filename.foo')
filePath = os.path.join('.',"2017eve","2017BOS.EVA")
#filePath = './2017eve/2017BOS.EVA'
readFile(filePath)


