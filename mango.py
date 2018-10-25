import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Baseball-Data"]
myCol = mydb["pitches"]

myquery = {'$and': 
            [{"inning":"116"},
            {'scoreDiff':0}]
}  

mydoc = myCol.find(myquery)
for x in mydoc:
  print(x)
print(mydoc.count())

