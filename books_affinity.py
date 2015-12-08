__author__ = 'danil.gizdatullin'
import itertools
# import numpy as np
# import config
# import datetime
import json
# import matplotlib.pyplot as plt


# path = config.path_to_users_library
# path = "/Users/danil.gizdatullin/Projects/Recommendations/user_book.csv"
path = "/Users/danil.gizdatullin/Projects/Recommendations/user_book1.csv"

# Step 1 - create users_library - dictionary of lists and set of all books
books = set([])
users_library = {}
data_file = open(path, 'r')
next(data_file)
for line in data_file:
    data_line = line[0:-1].split(',')
    user = str(data_line[0])
    book = int(data_line[1])
    books.add(book)
    if user in users_library:
        users_library[user].append(book)
    else:
        users_library[user] = [book]

books = list(books)

p_books = {}
for book in books:
    p_books[book] = 0

n_users = len(users_library)
n_books = len(books)
# 2,158,370
# 217,721

# distribution = []
# for user in users_library.iterkeys():
#     l = len(users_library[user])
#     distribution.append(l)
#
# plt.hist(distribution, bins=150)
# plt.title("Similarities median")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

# Step 2 - create a dictionary of affinity between all books
# affinity(x, y) = p(x, y) / (p(x)p(y))
#
books_affinity = {}

num_pair = 1
pairs = n_users
for user in users_library.iterkeys():
    #
    # print ("%i from %i") % (num_pair, pairs)
    # if num_pair == 1:
    #     print(datetime.datetime.now().time())
    # if num_pair == 1000000:
    #     print(datetime.datetime.now().time())
    # num_pair += 1
    books_of_current_user = users_library[user]
    if len(books_of_current_user) < 800:
        for book in books_of_current_user:
            p_books[book] += 1
        for pair in itertools.combinations(books_of_current_user, r=2):
            if pair[0] < pair[1]:
                book1 = pair[0]
                book2 = pair[1]
            else:
                book1 = pair[1]
                book2 = pair[0]
            key = str(book1) + "_" + str(book2)
            if key in books_affinity:
                books_affinity[key] += 1
            else:
                books_affinity[key] = 1
print("Second part")
num_pair = 1
pairs = len(books_affinity)
for book1_book2 in books_affinity.iterkeys():
    # print ("%i from %i") % (num_pair, pairs)
    num_pair += 1
    book_book = book1_book2.split('_')
    book1 = int(book_book[0])
    book2 = int(book_book[1])
    books_affinity[book1_book2] *= (float(n_users) / (p_books[book1] * p_books[book2]))

path_to_save_affinity = "/Users/danil.gizdatullin/Projects/Recommendations/books_graph/books_affinity.json"
with open(path_to_save_affinity, 'w') as fp:
    json.dump(books_affinity, fp)

