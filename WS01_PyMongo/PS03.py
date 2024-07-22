# 3. Display the 3 highest rated books.

from pymongo import DESCENDING 
from init.pymongo_get_database import get_database
from pprint import pprint

# Get the database
db = get_database()
# Get the collection
collection = db["book"]

top_three_books = collection.find({}).sort('rating', DESCENDING).limit(3)

for book in top_three_books:
    print(book['Title'], book['rating'])
