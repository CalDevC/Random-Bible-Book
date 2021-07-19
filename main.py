import random
import os
import book_dict as books

chosen_book = random.randrange(1, 66)
book_info = books.dict[chosen_book]

# This check avoids an error that is created when a book with only 1 chapter is selected.
# The error is thrown if we try to generate a random number between 1 and 1
if book_info[-1] != 1:
    chosen_chapter = random.randrange(1, book_info[-1])
else:
    chosen_chapter = 1

os.system("clear")
print("\n\n\n")
print("Today's scripture: " + book_info[0] + " " + str(chosen_chapter))
print("\n\n\n")
