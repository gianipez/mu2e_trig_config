import pymongo, pprint
from bson.objectid import ObjectId


def read_table(args):
    c1 = pymongo.MongoClient("mongodb://admin:XXXX@localhost:27017/teststand_db?authSource=admin")
    print(c1.list_database_names())
    
    db = c1.test
    print(db.list_collection_names())
    
    col = db.trigger_table
    
    #cur = col.find({"_id" : ObjectId("656819f6682447520684b0cd")})
    cur = col.find({"version" : args.version})
    for doc in cur: pprint.pprint(doc)




if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-q", "--quiet",
                        action="store_false", dest="verbose", default=True,
                        help="don't print status messages to stdout")
    parser.add_argument("-v", "--version",
                        dest="version",
                        help="vesion of the table to be downloaded")

    args = parser.parse_args()

    read_table(args)
