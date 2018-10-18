import json
import atBat

class game:
    def __init__(self,id,winningTeam,atBats,JSON):
        if JSON != None:
            jData = json.load(JSON)
            self.id = jData['id']
            self.winningTeam= jData['winningTeam']
            self.atBats = jData['atBats']  
        else:
            self.id = id
            self.winningTeam= winningTeam
            self.atBats = atBats
    def toJSON(self):
        data = {}
        data['id'] = self.id
        data['winningTeam'] = self.winningTeam
        data['atBats'] = self.atBats
        json_data = json.dumps(data)
        return json_data


    