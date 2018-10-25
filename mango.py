import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Baseball-Data"]
myCol = mydb["pitches"]

# myquery = {"atBats.inning":"116"}

# mydoc = myCol.find(myquery)

# for x in mydoc:
#   print(x)

x = myCol.find()
print(x[0])
