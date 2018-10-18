import json
import pitch

class atBat:
    def __init__(self,pitches,inning, first,second,third,outs,rundiff, outcome):
        self.pitches = pitches
        self.inning = inning
        self.first = first
        self.second = second
        self.third = third
        self.outs = outs
        self.rundiff = rundiff
    def toJSON(self):
        data = {}
        data['pitches'] = self.pitches
        json_data = json.dumps(data)
        return json_data
    def getCurrentState(self):
        return pitches[-1]