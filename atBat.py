import json
import pitch

class atBat:
    def __init__(self,pitches,inning, first,second,third,outs,scoreDiff):
        self.pitches = pitches
        self.inning = inning
        self.first = first
        self.second = second
        self.third = third
        self.outs = outs
        self.scoreDiff = scoreDiff
    
    def toDict(self):
        data = {}
        Jpitches =[]
        for pitch in self.pitches:
            Jpitches.append(pitch.toDict())
        data["pitches"] = Jpitches
        data["inning"] = self.inning
        data["first"] = self.first
        data["second"] = self.second
        data["third"] = self.third
        data["outs"] = self.outs
        data["scoreDiff"] = self.scoreDiff
        #json_data = json.dumps(data)
        return data
   
    def getCurrentState(self):
        if (len(self.pitches)==0):
            return []
        else:
            return self.pitches[-1]

