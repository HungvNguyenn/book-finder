from pymongo import MongoClient
import certifi

# Replace with your Atlas connection string
client = MongoClient("mongodb+srv://hungnguyen210703_db_user:GxByorfpV3juqBwx@book-db.ik3qbep.mongodb.net/?appName=book-db", tlsCAFile=certifi.where())

# Pick a database and collection
db = client["book-finder"]
collection = db["books"]

# --- Step 1: Clear the collection ---
collection.delete_many({})  # completely remove all documents

# --- Step 2: Define all books ---
all_books = [
    # Fantasy
    {"Title": "Harry Potter and the Sorcerers Stone", "Genre": "Fantasy"},
    {"Title": "The Hobbit", "Genre": "Fantasy"},
    {"Title": "Game of Thrones", "Genre": "Fantasy"},
    {"Title": "The Name of the Wind", "Genre": "Fantasy"},
    {"Title": "Mistborn The Final Empire", "Genre": "Fantasy"},
    {"Title": "The Lion the Witch and the Wardrobe", "Genre": "Fantasy"},
    {"Title": "Eragon", "Genre": "Fantasy"},

    # Science Fiction
    {"Title": "Dune", "Genre": "Science Fiction"},
    {"Title": "The Martian", "Genre": "Science Fiction"},
    {"Title": "Enders Game", "Genre": "Science Fiction"},
    {"Title": "Neuromancer", "Genre": "Science Fiction"},
    {"Title": "Snow Crash", "Genre": "Science Fiction"},
    {"Title": "The Time Machine", "Genre": "Science Fiction"},

    # Romance
    {"Title": "Pride and Prejudice", "Genre": "Romance"},
    {"Title": "Twilight", "Genre": "Romance"},
    {"Title": "The Fault in Our Stars", "Genre": "Romance"},
    {"Title": "Me Before You", "Genre": "Romance"},
    {"Title": "Anna Karenina", "Genre": "Romance"},
    {"Title": "The Notebook", "Genre": "Romance"},

    # Horror
    {"Title": "It", "Genre": "Horror"},
    {"Title": "Dracula", "Genre": "Horror"},
    {"Title": "Frankenstein", "Genre": "Horror"},
    {"Title": "The Shining", "Genre": "Horror"},
    {"Title": "Bird Box", "Genre": "Horror"},
    {"Title": "Pet Sematary", "Genre": "Horror"},
    {"Title": "The Exorcist", "Genre": "Horror"},

    # Mystery / Thriller
    {"Title": "Sherlock Holmes A Study in Scarlet", "Genre": "Mystery"},
    {"Title": "Gone Girl", "Genre": "Mystery"},
    {"Title": "The Girl with the Dragon Tattoo", "Genre": "Mystery"},
    {"Title": "Big Little Lies", "Genre": "Mystery"},
    {"Title": "And Then There Were None", "Genre": "Mystery"},
    {"Title": "The Da Vinci Code", "Genre": "Mystery"},

    # Classics / Literature
    {"Title": "The Hunger Games", "Genre": "Dystopia"},
    {"Title": "Of Mice and Men", "Genre": "Tragedy"},
    {"Title": "To Kill a Mockingbird", "Genre": "Fiction"},
    {"Title": "The Catcher in the Rye", "Genre": "Fiction"},
    {"Title": "1984", "Genre": "Dystopia"},
    {"Title": "Brave New World", "Genre": "Dystopia"},
    {"Title": "Little Women", "Genre": "Fiction"},
    {"Title": "Jane Eyre", "Genre": "Fiction"},

    # Adventure
    {"Title": "The Adventures of Huckleberry Finn", "Genre": "Adventure"},
    {"Title": "Treasure Island", "Genre": "Adventure"},
    {"Title": "Around the World in 80 Days", "Genre": "Adventure"},
    {"Title": "Journey to the Center of the Earth", "Genre": "Adventure"},
    {"Title": "King Solomons Mines", "Genre": "Adventure"},

    # Historical
    {"Title": "All the Light We Cannot See", "Genre": "Historical"},
    {"Title": "The Book Thief", "Genre": "Historical"},

    # Young Adult
    {"Title": "Percy Jackson and the Lightning Thief", "Genre": "Young Adult"},
    {"Title": "Divergent", "Genre": "Young Adult"},

    # Non Fiction
    {"Title": "Sapiens A Brief History of Humankind", "Genre": "Non Fiction"},
    {"Title": "Educated", "Genre": "Non Fiction"},
]

# --- Step 3: Insert all books ---
collection.insert_many(all_books)
# Verify the format
for book in collection.find():
    print(book)