import json
import pitch

class atBat:
    def __init__(self,pitches,inning):
            self.pitches = pitches
    def toJSON(self):
        data = {}
        data['pitches'] = self.pitches
        json_data = json.dumps(data)
        return json_data
    def getCurrentState(self):
        return pitches[-1]