# https://www.codewars.com/kata/523a86aa4230ebb5420001e1
# Where My Anagrams At?

# First Implementation 15/10/2021
def anagrams(word, words):
    # create array for valid anagrams
    anagramArray = []
    # set that the current word is a valid anagram
    isAnagram = True
    # for every word (possible anagram) in the list of words
    for possibleAnagram in words:
        # if the length of the word and the possible anagram differ
        if len(word) != len(possibleAnagram): 
            # the possible anagram is not an anagram
            continue
        # for every letter in the word
        for letter in word:
            # if the count of letters in the word and in the possible anagram differ
            if word.count(letter) != possibleAnagram.count(letter):
                # the current possible anagram is not an anagram 
                isAnagram = False 
                # exit the loop because it cannot be an anagram
                break
        if isAnagram:
            # add the anagram to the anagrams array
            anagramArray.append(possibleAnagram)
        else: 
            # reset the isAnagram boolean
            isAnagram = True
    #return the array of anagrams
    return anagramArray

