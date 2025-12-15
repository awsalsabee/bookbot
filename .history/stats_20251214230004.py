def get_number_of_words(book_text):
    words = book_text.split()
    word_counter = len(words)
    return word_counter

def get_char_count(book_text):
  count_of_char = {}
  for char in book_text:
    char = char.lower()
    if char in count_of_char:
      count_of_char[char] += 1
    else:
      count_of_char[char] = 1
  
  return count_of_char

def get_sorted(count_of_char):
  count_of_char[0]
  sorted_char_list = count_of_char.sort(reverse=True, key=get_sorted)
  return sorted_char_list
