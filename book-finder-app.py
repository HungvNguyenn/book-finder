from flask import Flask, render_template
from pymongo import MongoClient
import certifi

# Replace with your Atlas connection string
client = MongoClient("mongodb+srv://hungnguyen210703_db_user:GxByorfpV3juqBwx@book-db.ik3qbep.mongodb.net/?appName=book-db", tlsCAFile=certifi.where())

# Pick a database and collection
db = client["book-finder"]
collection = db["books"]

app = Flask(__name__)

# data = [
#     {
#         "Title" : "The Hobbit",
#         "Genre" : "Fantasy",
#     },
#     {
#         "Title": "The Hunger Game",
#         "Genre": "Dystopia",
#     },
#     {
#         "Title": "Harry Potter",
#         "Genre": "Fantasy",
#     },
#     {
#         "Title": "Of Mice and Men",
#         "Genre": "Tragedy",
#     },
# ]

@app.route("/")
def start_index():
    return render_template("index.html")

@app.route("/search/<genre>")
def find_book(genre):
    result = []
    for book in collection.find():
        if book["Genre"].lower() == genre.lower():
            book["_id"] = str(book["_id"])
            result.append(book)
    return result

app.run(host = "0.0.0.0", port = 5050)