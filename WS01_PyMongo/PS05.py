# 5. List all the book titles written by Indian universities , sort by book title.


from init.pymongo_get_database import get_database
from pprint import pprint

# Get the database
db = get_database()
# Get the collection
collection = db["book"]

# book = {
#     "Bookid": 754,
#     "Title": "Advanced Data Structures",
#     "Authors": [
#         {
#             "AuthorID": 109,
#             "Author name": "Dr. Ravi Kumar",
#             "University name": "Indian Institute of Technology",
#             "University_City": "Delhi",
#             "country": "India",
#             "Contact_no": "1122334455"
#         },
#         {
#             "AuthorID": 110,
#             "Author name": "Dr. Priya Sharma",
#             "University name": "Indian Institute of Science",
#             "University_City": "Bangalore",
#             "country": "India",
#             "Contact_no": "5566778899"
#         }
#     ],
#     "Category": ["Computer Science", "Data Structures"],
#     "Publisher ID": 206,
#     "edition": "1st",
#     "price": 59.99,
#     "rating": 4.5,
#     "year": 2023
# }

# # Insert the book into the collection
# result = collection.insert_one(book)


# if result.acknowledged:
#     print(f"Book inserted with id: {result.inserted_id}")
# else:
#     print("Insertion failed")


books = collection.find({
    "Authors.country" : "India"
}).sort("Title", 1)

# Print the titles of the books
print("Books written by authors from Indian universities:")
for book in books:
    pprint(book["Title"])
    