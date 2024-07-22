# 4. List the books titles written by author ‘Abraham silberschatz’

from init.pymongo_get_database import get_database
from pprint import pprint

# Get the database
db = get_database()
# Get the collection
collection = db["book"]

# book = {
#     "Bookid": 412,
#     "Title": "OS",
#     "Authors": ["Abraham Silberschatz"],
#     "Category": ["OS", "Education"],
#     "Publisher ID": 202,
#     "edition": "2nd",
#     "price": 49.99,
#     "rating": 4.8,
#     "year": 2020
# }

# # Insert the book into the collection
# result = collection.insert_one(book)


books = collection.find({
    "Authors": {
        "$in": ["Abraham Silberschatz"]
    }
})

for book in books:
    pprint(book)