def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_book_number_words(book_text):
    word_counter = 0
    for word in book_text:
        book_text.split(word)
        word_counter = word_counter + 1

    return f"Found {word_counter} total words"







def main():
    # book_contents = get_book_text("books/frankenstein.txt")
    # print(book_contents)
    get_book_number_words("books/frankenstein.txt")
    



main()