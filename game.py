import json
import atBat

class game:
    def __init__(self,id,winningTeam,loosingTeam,homeTeam,atBats,JSON):
        if JSON != None:
            jData = json.load(JSON)
            self.id = jData['id']
            self.winningTeam= jData['winningTeam']
            self.loosingTeam = jData['loosingTeam']
            self.homeTeam = jData['homeTeam']
            self.atBats = jData['atBats']  
        else:
            self.id = id
            self.winningTeam= winningTeam
            self.loosingTeam = loosingTeam
            self.homeTeam = homeTeam
            self.atBats = atBats
    def toJSON(self):
        data = {}
        data['id'] = self.id
        data['winningTeam'] = self.winningTeam
        data['loosingTeam'] = self.loosingTeam
        data['homeTeam'] = self.homeTeam
        data['atBats'] = self.atBats
        json_data = json.dumps(data)
        return json_data