#!/usr/bin/env python3

class MyString:
    def __init__(self, value=None):
      self.value = None
      if value is not None:
          if isinstance(value, str):
              self.value = value
          else:
              print("The value must be a string.")
      else:
          print("The value must be a string.")
    def is_sentence(self):
        return self.value.endswith('.')
    def is_question(self):
        return self.value.endswith('?')
    def is_exclamation(self):
        return self.value.endswith('!')
    def count_sentences(self):
        return self.value.count('.') + self.value.count('?') + self.value.count('!')


my_string = MyString("Hello world! One! Two. Three?")
print(my_string.is_sentence())  # Output: False, ends with "?"
print(my_string.is_question())  # Output: True, last sentence
print(my_string.is_exclamation())  # Output: False, ends with "?"
print(my_string.count_sentences())  # Output: 4