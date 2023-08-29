import csv

books = []

def read():
    with open('./Goodreads/books-small.csv', newline='') as csvfile:
        book = csv.reader(csvfile, delimiter=' ', quotechar='|')
        keys = book[0]
        vals = book[1:]
        for row in vals:
            d = {}
            for i in range(row):
                d[keys[i]] = row[i]
            books.add(d)
                

def get_size_books():
    return len(books)