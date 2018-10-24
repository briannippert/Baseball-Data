from parse import *

testlines = """
play,7,0,leonj001,01,CX,8(B)84(2)/LDP/L8
play,7,1,tempg001,00,X,54(B)/BG25/SH.1-2
play,7,1,randw001,00,.>X,1(B)16(2)63(1)/LTP/L1
play,1,0,bayld001,??,,CS2(24).2-3
play,6,0,beneb001,??,,CS2(2E4).1-3
play,9,0,bencj101,??,,DI.1-2
play,4,0,guerp001,00,22,PO2(14)
play,6,1,javis001,10,B1,POCS2(1361)"""
testlines = testlines.split()
# for line in testlines:
#     detailedLine = line.split(',')
#     ret = parseAtBat(detailedLine[1:],None)
#     print(line, '\n',ret,'\n')

def testCase(play, eOuts, eFirst, eSecond, eThird, eScoreDiff):
    #takes in a play and tests the result 
    detailedLine = play.split(',')
    result = parseAtBat(detailedLine[1:],None)
    if (result.outs != eOuts):
        raise AssertionError("Outs do not match")
    else:
        print("Test passed")

print('tests double play')
ex = 'play,7,0,backw001,11,FBX,64(1)3/GDP/G6'
testCase(ex,eOuts=2,eFirst=False,eSecond=False,eThird=False,eScoreDiff=0)