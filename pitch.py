import json

class pitch:
    def __init__(self, ball, strike, out, scoreDiff, outcome, first, second, third, JSON):
        if JSON != None:
            jData = json.load(JSON)
            self.ball = jData['ball']
            self.strike = jData['strike']
            self.out = jData['out']
            self.scoreDiff = jData['scoreDiff']
            self.outcome = jData['outcome']
            self.first = jData['first']
            self.second = jData['second']
            self.third = jData['third']
        else:
            self.ball = ball
            self.strike = strike
            self.out = out
            self.scoreDiff = scoreDiff
            self.outcome = outcome
            self.first = first
            self.second = second
            self.third = third

    def toJSON(self):
        data = {}
        data['ball'] = self.ball
        data['strike'] = self.strike
        data['out'] = self.out
        data['scoreDiff'] = self.scoreDiff
        data['outcome'] = self.outcome
        data['first'] = self.first
        data['second'] = self.second
        data['third'] = self.third
        json_data = json.dumps(data)
        return json_data
