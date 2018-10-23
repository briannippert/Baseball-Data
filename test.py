from parse import *

testlines = """play,4,1,ramih003,32,CFBBBX,6/P
play,4,1,younc004,22,CFBFBX,HR/78/L
play,4,1,bradj001,01,FX,5/P5F
play,4,1,leons001,12,CBFFX,S7/G
play,4,1,marrd001,12,FFFBX,8/L"""
testlines = testlines.split()
for line in testlines:
    detailedLine = line.split(',')
    ret = parseAtBat(detailedLine[1:],None)
    print(ret)

# print(parseAtBat(testlines[0][1:],None))