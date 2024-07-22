from init.pymongo_get_database import get_database
from pprint import pprint

# Get the database
db = get_database()
# Get the collection
collection = db["book"]

# Find the document with the specified title
fav_book = collection.find_one({
    "Title": "Modern Mathematics"
})

# Display the favorite book
if fav_book:
    print("Displaying Favourite Book...\n")
    pprint(fav_book)
else:
    print("Book not found.")

# Closing message
print("\nClosing Program...")
