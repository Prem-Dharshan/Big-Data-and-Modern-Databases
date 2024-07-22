# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["book"]

# Sample data
books = [
    {
        "Bookid": 1,
        "Title": "Advanced Physics",
        "Authors": [
            {"AuthorID": 101, "Author name": "Dr. John Doe", "University name": "MIT", "University_City": "Cambridge", "country": "USA", "Contact_no": "1234567890"},
            {"AuthorID": 102, "Author name": "Dr. Jane Smith", "University name": "Stanford", "University_City": "Stanford", "country": "USA", "Contact_no": "0987654321"}
        ],
        "Category": ["Science", "Physics"],
        "Publisher ID": 201,
        "edition": "3rd",
        "price": 59.99,
        "rating": 4.5,
        "year": 2021
    },
    {
        "Bookid": 2,
        "Title": "Modern Mathematics",
        "Authors": [
            {"AuthorID": 103, "Author name": "Dr. Alan Turing", "University name": "Cambridge", "University_City": "Cambridge", "country": "UK", "Contact_no": "1122334455"},
            {"AuthorID": 104, "Author name": "Dr. Ada Lovelace", "University name": "Oxford", "University_City": "Oxford", "country": "UK", "Contact_no": "5566778899"}
        ],
        "Category": ["Maths", "Computer Science"],
        "Publisher ID": 202,
        "edition": "2nd",
        "price": 49.99,
        "rating": 4.8,
        "year": 2020
    },
    {
        "Bookid": 3,
        "Title": "Fictional Worlds",
        "Authors": [
            {"AuthorID": 105, "Author name": "J.K. Rowling", "University name": "Exeter", "University_City": "Exeter", "country": "UK", "Contact_no": "6677889900"},
            {"AuthorID": 106, "Author name": "George R.R. Martin", "University name": "Northwestern", "University_City": "Evanston", "country": "USA", "Contact_no": "7788990011"}
        ],
        "Category": ["Fiction", "Fantasy"],
        "Publisher ID": 203,
        "edition": "1st",
        "price": 39.99,
        "rating": 4.7,
        "year": 2019
    },
    {
        "Bookid": 4,
        "Title": "Introduction to Chemistry",
        "Authors": [
            {"AuthorID": 107, "Author name": "Dr. Marie Curie", "University name": "Sorbonne", "University_City": "Paris", "country": "France", "Contact_no": "3344556677"},
            {"AuthorID": 108, "Author name": "Dr. Linus Pauling", "University name": "Caltech", "University_City": "Pasadena", "country": "USA", "Contact_no": "4455667788"}
        ],
        "Category": ["Science", "Chemistry"],
        "Publisher ID": 204,
        "edition": "4th",
        "price": 69.99,
        "rating": 4.9,
        "year": 2022
    },
    {
        "Bookid": 5,
        "Title": "Historical Perspectives",
        "Authors": [
            {"AuthorID": 109, "Author name": "Dr. Howard Zinn", "University name": "Boston University", "University_City": "Boston", "country": "USA", "Contact_no": "5566778899"},
            {"AuthorID": 110, "Author name": "Dr. Yuval Noah Harari", "University name": "Hebrew University", "University_City": "Jerusalem", "country": "Israel", "Contact_no": "6677889900"}
        ],
        "Category": ["History", "Social Science"],
        "Publisher ID": 205,
        "edition": "5th",
        "price": 79.99,
        "rating": 4.6,
        "year": 2018
    }
]

# Insert data into MongoDB
collection_name.insert_many(books)
print("Data inserted successfully!")
