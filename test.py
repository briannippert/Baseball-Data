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
        print("Test passed\n")

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

print('tests batter tagged out at base not normally covered by fielder')
ex = 'play,7,1,tempg001,00,X,54(B)/BG25/SH.1-2'
testCase(ex,eOuts=1,eFirst=False,eSecond=True,eThird=False,eScoreDiff=0)

print('tests Force out where batter is also out')
ex = 'play,2,0,espid001,00,X,36(1)/FO/G.3-H'
testCase(ex,eOuts=2,eFirst=False,eSecond=False,eThird=False,eScoreDiff=-1)

print('tests 1b runner being forced out. Allows batter to first and runner scores')
ex = 'play,5,0,gileb001,10,BX,54(1)/FO/G5.3-H;B-1'
testCase(ex,eOuts=1,eFirst=True,eSecond=False,eThird=False,eScoreDiff=-1)

print('tests single')
ex = 'play,8,0,pacit001,??,,S7'
testCase(ex,eOuts=0,eFirst=True,eSecond=False,eThird=False,eScoreDiff=0)

print('tests bases loaded clearing double')
ex = 'play,2,1,santn001,12,CFBX,D7/G5.3-H;2-H;1-H'
testCase(ex,eOuts=0,eFirst=False,eSecond=True,eThird=False,eScoreDiff=3)

print('tests triple with runner on second')
ex = 'play,3,0,raint001,11,CBX,T9/F9LD.2-H'
testCase(ex,eOuts=0,eFirst=False,eSecond=False,eThird=True,eScoreDiff=-1)

print('tests ground rule double with runner scoring')
ex = 'play,3,0,surhb001,10,.BX,DGR/L9LS.2-H'
testCase(ex,eOuts=0,eFirst=False,eSecond=True,eThird=False,eScoreDiff=-1)

print('tests solo home run')
ex = 'play,8,0,bellg001,21,CBBX,H/L7D'
testCase(ex,eOuts=0,eFirst=False,eSecond=False,eThird=False,eScoreDiff=-1)

print('tests 3 run homerun')
ex = 'play,12,1,bichd001,02,FFFX,HR/F78XD.2-H;1-H'
testCase(ex,eOuts=0,eFirst=False,eSecond=False,eThird=False,eScoreDiff=3)

print('tests inside the park hr')
ex = 'play,4,0,younr001,32,FBFFFBBX,HR9/F9LS.3-H;1-H'
testCase(ex,eOuts=0,eFirst=False,eSecond=False,eThird=False,eScoreDiff=-3)

print('tests error on foul. no changes')
ex = 'play,5,0,murre001,00,F,FLE5/P5F'
testCase(ex,eOuts=0,eFirst=False,eSecond=False,eThird=False,eScoreDiff=0)

print('tests hit by pitch')
ex = 'play,1,1,lansc001,00,H,HP.1-2'
testCase(ex,eOuts=0,eFirst=True,eSecond=True,eThird=False,eScoreDiff=0)

print('tests intentional walk')
ex = 'play,8,0,sciom001,30,B+22.III,IW'
testCase(ex,eOuts=0,eFirst=True,eSecond=False,eThird=False,eScoreDiff=0)

print('tests catchers interference')
ex = 'play,9,1,cruzj002,??,,C/E2.1-2'
testCase(ex,eOuts=0,eFirst=True,eSecond=True,eThird=False,eScoreDiff=0)
