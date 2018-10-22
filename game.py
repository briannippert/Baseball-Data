import json
from atBat import atBat
from pitch import pitch
class game:
    def __init__(self,id,winningTeam,atBats,JSON):
        if JSON != None:
            jData = json.load(JSON)
            self.id = jData["id"]
            self.winningTeam= jData["winningTeam"]
            self.atBats = jData["atBats"]  
        else:
            self.id = id
            self.winningTeam= winningTeam
            self.atBats = atBats
    def toJSON(self):
        data = {}
        data["id"] = self.id
        data["winningTeam"] = self.winningTeam
        atBatList = []
        for atBat in self.atBats:
            atBatList.append(atBat.toDict())
        data["atBats"] = atBatList
        json_data = json.dumps(data)
        return json_data
    def toDict(self):
        data = {}
        data["id"] = self.id
        data["winningTeam"] = self.winningTeam
        atBatList = []
        for atBat in self.atBats:
            atBatList.append(atBat.toDict())
        data["atBats"] = atBatList
        return data


# pitches = []
# p = pitch( 0,0,0,0,"S",False,False,False,None)
# pitches.append(p)
# p = pitch(0,1,0,0,"S",True,False,True,None)
# pitches.append(p)
# p = pitch(0,2,0,0,"K",True,False,True,None)
# pitches.append(p)

# atBats = []
# test = atBat(pitches,"T5",True,True,False,1,0,"K")
# atBats.append(test)
# test = atBat(pitches,"T5",True,False,False,2,0,"K")
# atBats.append(test)
# test = atBat(pitches,"T5",False,True,False,3,0,"K")
# atBats.append(test)
# test = atBat(pitches,"B5",True,True,False,1,0,"K")
# atBats.append(test)

# game = game(1,"BOS",atBats,None)
# testJson = game.toJSON()
# undoJson = json.loads(testJson)
# print(testJson)
