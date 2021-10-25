# https://www.codewars.com/kata/5390bac347d09b7da40006f6
# Jaden Casing Strings

# First Implementation 01/10/2021
def to_jaden_case(string):
    splitted_string = string.split(" ")
    jaden_case=[]
    for word in splitted_string:
        jaden_case.append(word.capitalize())
    return " ".join(jaden_case) 
