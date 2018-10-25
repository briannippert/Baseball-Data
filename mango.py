import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Baseball-Data"]
myCol = mydb["BaseBall-Data"]

# myquery = {"atBats.inning":"116"}

# mydoc = myCol.find(myquery)

# for x in mydoc:
#   print(x)

data = myCol.aggregate([
    {'$match': {'$and': 
                    [{'atBats.pitches.strike':2},
                    {'atBats.inning':'116'}]
                }}
])

for x in data:
    print(x)