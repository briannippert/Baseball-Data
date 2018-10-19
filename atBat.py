import json
import pitch

class atBat:
    def __init__(self,pitches,inning, first,second,third,outs,scoreDiff, outcome):
        self.pitches = pitches
        self.inning = inning
        self.first = first
        self.second = second
        self.third = third
        self.outs = outs
        self.scoreDiff = scoreDiff
    
    def toJSON(self):
        data = {}
        Jpitches =" "
        for pitch in self.pitches:
            Jpitches += pitch.toJSON()
        data['pitches'] = Jpitches
        data['inning'] = self.inning
        data['fisrt'] = self.first
        data['second'] = self.second
        data['third'] = self.third
        data['outs'] = self.outs
        data['scoreDiff'] = self.scoreDiff
        json_data = json.dumps(data)
        return json_data
   
    def getCurrentState(self):
        return pitches[-1]

pitches = []
p = pitch.pitch(0,0,0,0,"S",False,False,False,None)
pitches.append(p)
p = pitch.pitch(0,1,0,0,"S",True,False,True,None)
pitches.append(p)
p = pitch.pitch(0,2,0,0,"K",True,False,True,None)
pitches.append(p)


test = atBat(pitches,"T5",True,True,False,1,0,"K")
print(test.toJSON())