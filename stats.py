def get_book_text(filepath):
    # Reads the contents of a text file using the filepath and returns it as a string
    with open(filepath, "r") as f:
        return f.read()

def count_words(book):
    # Counts the number of words in the given book text
    words = book.split()
    return len(words)

def count_characters(book):

    char_dict = {}

    words = book.split()

    for word in words:
        for char in word:
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    return char_dict

def sort_char_list(char_dict):
    
    list_of_dicts = []
    for char, count in char_dict.items():
        list_of_dicts.append({"char": char, "num": count})
    
    list_of_dicts.sort(key=lambda x: x["num"], reverse=True)
    return list_of_dicts