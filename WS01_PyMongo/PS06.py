from init.pymongo_get_database import get_database
from pprint import pprint

# Get the database
db = get_database()
# Get the correct collection for publishers
collection = db["publisher"]


# publisher = {
#     "PublisherID": 206,
#     "Name": "Prentice Hall",
#     "Address": {
#         "street": "1 Main St",
#         "city": "Upper Saddle River",
#         "pincode": "07458"
#     },
#     "Annual revenue": 5000000
# }

# # Insert the publisher into the collection
# result = collection.insert_one(publisher)

# # Check if the insertion was successful
# if result.acknowledged:
#     print(f"Publisher inserted with id: {result.inserted_id}")
# else:
#     print("Insertion failed")

existing_doc = collection.find_one({"Name": "Prentice Hall"})
pprint(existing_doc)

new_address = {
    "street": "2 New St",
    "city": "Upper Saddle River",
    "pincode": "07458"
}

updated_publisher = collection.update_one(
    {"Name": "Prentice Hall"},
    {"$set": {"Address": new_address}}
)

# Check if the update was successful
if updated_publisher.modified_count > 0:
    print("Publisher's address updated successfully.")
    updated_doc = collection.find_one({"Name": "Prentice Hall"})
    pprint(updated_doc)
else:
    print("Address update failed or no changes were made.")
