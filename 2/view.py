import controller as C

def load_books():
    print(C.load_books())

def get_avg_score():
    title = getLine()
    score = C.get_avg_score(title)
    print(score)