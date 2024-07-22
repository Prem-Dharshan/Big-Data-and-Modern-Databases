# Return all the publishers

from init.pymongo_get_database import get_database

dbname = get_database()
collection = dbname["publisher"]

for i in collection.find({}, {"Name": 1, "_id": 0}):
    print(i)