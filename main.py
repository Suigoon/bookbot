from stats import get_num_words
from stats import get_num_chars
from stats import sort_list
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words")
        print("--------- Character Count -------")
        chars_sorted = sort_list(get_num_chars(get_book_text(sys.argv[1])))
        for char_dict in chars_sorted:
            char = char_dict["char"]
            num = char_dict["Num"]
            if char.isalpha():
                print(f"{char}: {num}")

        print("============== END ===============")
    

main()