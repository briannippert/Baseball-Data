import pymongo, json, os

def loadData():
  client = pymongo.MongoClient("mongodb://localhost:27017/")

  db = client["Baseball-Data"]
  db.drop_collection("pitches")
  pitchCol = db["pitches"]

  with open("results.json") as f:
    data = json.load(f)
  pitchCol.insert(data)
  client.close()
  os.remove("results.json")

if __name__ == '__main__':
  loadData()