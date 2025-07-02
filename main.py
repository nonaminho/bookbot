from stats import *

book = "books/frankenstein.txt"
text = get_book_text(book)
num_words = count_words(text)
char_list = count_each(text)

print(f"""============ BOOKBOT ============
Analizing book found at {book}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")

for i in range(len(char_list)):
    print(f"{char_list[i]['char']}: {char_list[i]['num']}")

print("============= END ===============")