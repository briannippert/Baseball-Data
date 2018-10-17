import json
class atBat:
    def __init__(self,pitches,inning):
            self.pitches = pitches
    def toJSON(self):
        data = {}
        data['pitches'] = self.pitches
        json_data = json.dumps(data)
        return json_data