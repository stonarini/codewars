# https://www.codewars.com/kata/54b724efac3d5402db00065e
# Decode the Morse Code

# First Implementation 03/10/2021
def decodeMorse(morse_code):
    
    morseChars=morse_code.split(" ")
    decodedMorse=[]
    prevWasEmpty=False
    
    for i in range(len(morseChars)):
        if morseChars[i] == '':
            if prevWasEmpty:
                decodedMorse.append(" ")
            else:
                prevWasEmpty=True
        else:
            decodedMorse.append(MORSE_CODE[morseChars[i]])
            prevWasEmpty=False
        
    return ("".join(decodedMorse)).strip()

