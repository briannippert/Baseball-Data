games = {}

strikePlays = ['C','K','M','O','Q','S','T']
ballPlays = ['B','I','P','V']

def parsePlay(play,prevPlay):
    pass

with open('./2017eve/2017BOS.EVA') as fp:
    gameId = None
    game = None
    for line in fp:
        lineDetailed = line.strip().split(',')
        if(lineDetailed[0]=='id'):
            
            if(gameId != None):
                games[gameId] = game
        if(lineDetailed[0]=='play'):
            if(lineDetailed[6]=='NP' and lineDetailed[5] == ''): continue #ignore non-injury subs
            parsePlay(lineDetailed[1:])

