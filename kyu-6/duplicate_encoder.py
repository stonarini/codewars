# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
# Duplicate Encoder

# First Implementation 15/10/2021
def duplicate_encode(word):
    return "".join([")" if word.lower().count(letter.lower()) > 1 else "(" for letter in word ])
