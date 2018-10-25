import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Baseball-Data"]
myCol = mydb["BaseBall-Data"]

# myquery = {"atBats.inning":"116"}

# mydoc = myCol.find(myquery)

# for x in mydoc:
#   print(x)

data = myCol.aggregate([
    {'$match': {'atBats.inning':'116'}},
    {'$unwind': {'path':'$atBats.pitches'}}
    
    # {'$match':}
])

# data = myCol.aggregate([
#     {'$match': {
#         '$and': 
#             [{'atBats.pitches.strike':2},
#             {'atBats.inning':'116'}]
#     }}
#     {'$project': {
#         'atBats': {'$filter': {
#             'input': '$atBats',
#             'as': 'atBat',
#             'cond': {'$eq':
#                 ['$$atBats.inning']
#             }
#         }}

#     }}
# ])
for x in data:
    print(x)