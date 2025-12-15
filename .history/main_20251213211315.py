def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_number_of_words(book_text):
    words = book_text.split()
    word_counter = len(words)
    return word_counter







def main():
    #book_contents = get_book_text("books/frankenstein.txt")
    #print(book_contents)
    words_number = get_number_of_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {words_number} total words")
    



main()