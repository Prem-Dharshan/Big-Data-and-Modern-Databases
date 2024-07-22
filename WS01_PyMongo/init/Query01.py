from pymongo_get_database import get_database
dbname = get_database()
collection_book= dbname["book"]
collection_author= dbname["author"]


# Increment the rating of the book with Bookid 1 by 0.5

book = collection_book.find_one({"Bookid": 1})

if book:
    print("Book found:", book)
else:
    print("Book not found.")

collection_book.update_one(
    {"Bookid": 1},
    {"$inc": {"rating": 0.5}}
)

book = collection_book.find_one({"Bookid": 1})

if book:
    print("Book found:", book)
else:
    print("Book not found.")

print("Rating updated successfully!")

print(book)

# Push a new author into the Authors array of the book with Bookid 1
new_author = {
    "AuthorID": 111,
    "Author name": "Dr. New Author",
    "University name": "New University",
    "University_City": "New City",
    "country": "New Country",
    "Contact_no": "1231231234"
}

collection_author.update_one(
    {"Bookid": 1},
    {"$push": {"Authors": new_author}}
)
print("New author added successfully!")

# Delete an author with AuthorID 101 from the Authors array of the book with Bookid 1
collection_book.update_one(
    {"Bookid": 1},
    {"$pull": {"Authors": {"AuthorID": 101}}}
)
print("Author deleted successfully!")

collection_author.delete_one({"AuthorID": 111})

