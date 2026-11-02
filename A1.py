library = {
    "Hariti": ["Python", "DBMS", "AI"],
    "Vaishnavi": ["Java", "Python"],
    "Shivam": [],
    "Sneha": ["DBMS", "Python", "AI", "Java"]
          }
def avgbooks():
    tb=[]
    for books in library.values():
        tb=tb.append(books)
    tm=len(library)
    avg=tb/tm
    print("Average books:",avg)

def max_min_bb():
    l = [len(books) for books in library.values()]

    high = max(l)
    low = min(l)

    return high, low

def nobooksborrowed():
    count = 0

    for books in library.values():
        if len(books) == 0:
            count += 1

    return count

def most_frequent_book(library):
    freq = {}

    for books in library.values():
        for book in books:
            if book in freq:
                freq[book] += 1
            else:
                freq[book] = 1

    most_book = None
    hf = 0

    for book, count in freq.items():
        if count > hf:
            hf = count
            most_book = book

    return most_book, hf