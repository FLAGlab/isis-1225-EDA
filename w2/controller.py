import model as M

def load_books():
    M.read()
    return M.gest_size_books()


def get_avg_score(title):
    books = M.get_book()
    score = -1
    for book in books:
        if book.title == title:
            score = book.score
    return score