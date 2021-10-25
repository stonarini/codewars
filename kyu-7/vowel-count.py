# https://www.codewars.com/kata/54ff3102c1bad923760001f3
# Vowel Count

# First Implementation 01/10/2021
def get_count(sentence):
    vowelCount = 0
    for letter in sentence:
        if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
            vowelCount+= 1
    return vowelCount

# -------------------

# Second Implementation 25/10/2021
def get_count(sentence):
    return sum(sentence.count(letter) for letter in ["a", "e", "i", "o", "u"])
