import pymongo, pprint
import json
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb://admin:XXXX@localhost:27017/teststand_db?authSource=admin")
db     = client["test"]
col    = db["trigger_table"]#this specifies the MongoDb collection name, aka the name of the table

f      = open("data/trigDict.json")
data   = json.load(f)

v_to_check = data['version']
print("version to check: {}".format(v_to_check))
cur = col.find({"version" : v_to_check})
for document in cur:
    print(document)
#
print('Located {0:,} item(s)'.format(cur.retrieved))
if cur.retrieved !=0:
    print("VERSION {} ALREADY PRESENT IN THE DB, PLEASE RE-UPLOAD IT WITH A DIFFERENT ONE".format(v_to_check))
    exit()

x      = col.insert_one(data)
print("TABBLE V {} SUCCESFULLY UPLOADED :-)".format(v_to_check))
