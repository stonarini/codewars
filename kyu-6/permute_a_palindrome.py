# https://www.codewars.com/kata/58ae6ae22c3aaafc58000079
# Permute a Palindrome

# First Implementation 15/10/2021
def permute_a_palindrome(input): 
    letters_count = {}
    for letter in input:
        try:
            letters_count[letter] += 1
        except:
            letters_count[letter] = 1
    
    filtered_letters={}
    for letter in letters_count:
        if letters_count[letter] % 2 != 0:
            filtered_letters[letter] = letters_count[letter]
            
    if len(filtered_letters) < 2:
        return True
    return False

