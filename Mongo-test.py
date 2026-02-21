from pymongo import MongoClient
import certifi

# Replace with your Atlas connection string
client = MongoClient("mongodb+srv://hungnguyen210703_db_user:GxByorfpV3juqBwx@book-db.ik3qbep.mongodb.net/?appName=book-db", tlsCAFile=certifi.where())

# Pick a database and collection
db = client["book-finder"]
collection = db["books"]

# WRITE
#collection.insert_one({"name" : "The Hunger Game", "Genre" : "Dystopia"})
#collection.insert_one({"name" : "Of Mice and Men", "Genre" : "Tragedy"})
#collection.insert_one({"name" : "Game of Thrones", "Genre" : "Fantasy"})
#collection.insert_one({"name" : "Dune", "Genre" : "Science Fiction"})
#collection.insert_one({"name" : "The Martian", "Genre" : "Science Fiction"})
#collection.insert_one({"name" : "To Kill a Mockingbird", "Genre" : "Fiction"})
#collection.insert_one({"name" : "The catcher in the Rye", "Genre" : "Fiction"})

# READ
doc = collection.find({"message": "Hello, MongoDB!"})
for f in collection.find():
    print(f)
