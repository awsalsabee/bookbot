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

def get_list_of_char(count_of_char):
    char_list = []
    for char_key in count_of_char:
        num_value = count_of_char[char_key]
        new_dict = {
            'char': char_key,  
            'num': num_value
        }
        char_list.append(new_dict)
    return char_list

def get_key(items):
   return items['num']

def get_char_list_sorted(char_list):
   sorted_list = char_list.sort(reverse=True, key=get_key)
   return sorted_list