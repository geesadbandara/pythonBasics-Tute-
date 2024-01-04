books = {
    "The Lord of the Rings": "Fantasy",
    "Pride and Prejudice": "Romance",
    "The Hitchhiker's Guide to the Galaxy": "Sci-Fi",
    "To Kill a Mockingbird": "Fiction",
    "The Great Gatsby": "Fiction",
}

fantasyBook = []
romanceBook = []
sciFiBook = []
fictionBook = []
for key,value in books.items():
    if(value == "Fantasy" ):
        fantasyBook.append(key)
    elif(value == "Romance"):
        romanceBook.append(key)
    elif(value == "Sci-Fi"):
        sciFiBook.append(key)
    elif(value == "Fiction"):
        fictionBook.append(key)
        
print(fantasyBook)
print(romanceBook)
print(sciFiBook)
print(fictionBook)
