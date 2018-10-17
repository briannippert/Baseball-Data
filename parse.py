games = {}

with open('.\\2017eve\\2017BOS.EVA') as fp:
    gameId = None
    game = None
    for line in fp:
        # print(line.strip())
        lineDetailed = line.strip().split(',')
        # print(lineDetailed)
        if(lineDetailed[0]=='id'):
            # print(lineDetailed[1])
            
            if(gameId != None):
                games[gameId] = game
        if(lineDetailed[0]=='play'):
            if(lineDetailed[6]=='NP' and lineDetailed[5] == ''): pass #ignore non-injury subs
            print(lineDetailed[1:])