# https://www.codewars.com/kata/530e15517bc88ac656000716
# Rot13

# First Implementation 01/10/2021
def rot13(message):
    # set an empty output
    output=""
    # instantiate the alphabet
    alphabet=[chr(i) for i in range(97, 123)]
    
    # for every letter in the input message
    for letter in message:
        i = 0
        # set the letter as lowercase by default
        isUpper=False
        # we search for the index of the letter in the
        # alphabet and if it's uppercase
        while i < 26:
            if alphabet[i] == letter: 
                break
            if alphabet[i].upper() == letter:
                isUpper=True
                break
            i+=1
            
        # if the letter is in the alphabet (not a special character)
        if i != 26:
            # shift it by 13 positions in the alphabet
            newLetter=i+13
            # if we go over the amount of letters in the alphabet
            if newLetter > 25:
                # go back 26 positions
                # ie: 
                #   25 == z
                #   if the position > 25 (ie: 26)
                #   26 - 26 = 0 = a
                newLetter-=26
            # add to the output the new letter, keeping the original case
            output+=alphabet[newLetter].upper() if isUpper else alphabet[newLetter]
        else:
            # if the letter is a special character don't change it
            output+=letter
        
    return output

