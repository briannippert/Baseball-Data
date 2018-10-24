from parse import *



def testCase(play, eOuts, eFirst, eSecond, eThird, eScoreDiff):
    #takes in a play and tests the result 
    detailedLine = play.split(',')
    result = parseAtBat(detailedLine[1:],None)
    print(play)
    print(result)
    if (result.outs != eOuts):
        raise AssertionError("Outs do not match")
    elif (result.first != eFirst):
        raise AssertionError("First does not match")
    elif (result.second != eSecond):
        raise AssertionError("second does not match")
    elif (result.third != eThird):
        raise AssertionError("third does not match")
    elif (result.scoreDiff != eScoreDiff):
        raise AssertionError("scoreDiff does not match")
    else:
        print("Test passed")

print('tests double play')
ex = 'play,7,0,backw001,11,FBX,64(1)3/GDP/G6'
testCase(ex,eOuts=2,eFirst=False,eSecond=False,eThird=False,eScoreDiff=0)

print('tests double play where batter is specified')
ex = 'play,7,0,leonj001,01,CX,8(B)84(2)/LDP/L8'
testCase(ex,eOuts=2,eFirst=False,eSecond=False,eThird=False,eScoreDiff=0)

print('tests batter out where a runner progresses')
ex = 'play,7,1,tempg001,00,X,54(B)/BG25/SH.1-2'
testCase(ex,eOuts=1,eFirst=False,eSecond=True,eThird=False,eScoreDiff=0)

print('tests triple play')
ex = 'play,7,1,randw001,00,.>X,1(B)16(2)63(1)/LTP/L1'
testCase(ex,eOuts=3,eFirst=False,eSecond=False,eThird=False,eScoreDiff=0)

print('tests caught stealing where a runner progresses')
ex = 'play,1,0,bayld001,??,,CS2(24).2-3'
testCase(ex,eOuts=1,eFirst=False,eSecond=False,eThird=True,eScoreDiff=0)

print('tests caught stealing where error allow runner to reach safely')
ex = 'play,6,0,beneb001,??,,CS2(2E4).1-3'
testCase(ex,eOuts=0,eFirst=False,eSecond=False,eThird=True,eScoreDiff=0)

print('tests defensive indifference')
ex = 'play,9,0,bencj101,??,,DI.1-2'
testCase(ex,eOuts=0,eFirst=False,eSecond=True,eThird=False,eScoreDiff=0)

print('tests runner picked off')
ex = 'play,4,0,guerp001,00,22,PO2(14)'
testCase(ex,eOuts=1,eFirst=False,eSecond=False,eThird=False,eScoreDiff=0)

print('tests runner picked off caught stealing')
ex = 'play,6,1,javis001,10,B1,POCS2(1361)'
testCase(ex,eOuts=1,eFirst=False,eSecond=False,eThird=False,eScoreDiff=0)