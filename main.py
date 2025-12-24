from stats import get_book_text, count_words, count_characters, sort_char_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    booktext = get_book_text(filepath)

    print("="*12 + " BOOKBOT " + "="*12)
    print(f"Analizing book found at {filepath}")
    print("-"*10 + " Word Count " + "-"*10)    

    num_words = count_words(booktext)

    print(f"Found {num_words} total words")
    print("-"*8 + " Character Count " + "-"*8)

    char_counts = count_characters(booktext)
    sorted_char_list = sort_char_list(char_counts)
    for char_pair in sorted_char_list:
        if char_pair["char"].isalpha():
            print(f"{char_pair["char"]}: {char_pair["num"]}")

    print("="*13 + " END " + "="*13)


main()