from pymongo_get_database import get_database
db = get_database()

collection = db["publisher"]

# Sample data
publishers = [
    {
        "Publisher ID": 201,
        "Name": "Pearson Education",
        "Address": {"street": "221B Baker Street", "city": "London", "pincode": "NW1 6XE"},
        "Annual revenue": 5000000
    },
    {
        "Publisher ID": 202,
        "Name": "Springer Nature",
        "Address": {"street": "Tiergartenstraße 17", "city": "Berlin", "pincode": "10785"},
        "Annual revenue": 7500000
    },
    {
        "Publisher ID": 203,
        "Name": "HarperCollins",
        "Address": {"street": "195 Broadway", "city": "New York", "pincode": "10007"},
        "Annual revenue": 6000000
    },
    {
        "Publisher ID": 204,
        "Name": "Oxford University Press",
        "Address": {"street": "Great Clarendon Street", "city": "Oxford", "pincode": "OX2 6DP"},
        "Annual revenue": 8000000
    },
    {
        "Publisher ID": 205,
        "Name": "Penguin Random House",
        "Address": {"street": "1745 Broadway", "city": "New York", "pincode": "10019"},
        "Annual revenue": 9000000
    }
]

# Insert data into MongoDB
collection.insert_many(publishers)
print("Data inserted successfully!")
