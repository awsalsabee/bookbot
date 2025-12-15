from stats import get_number_of_words

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    book_contents = get_book_text("books/frankenstein.txt")
    #print(book_contents)
    words_number = get_number_of_words(book_contents)
    print(f"Found {words_number} total words")
    



main()