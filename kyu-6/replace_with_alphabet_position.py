# https://www.codewars.com/kata/546f922b54af40e1e90001da
# Replace with Alphabet Position

# First Implementation 15/10/2021
def alphabet_position(text):
    alphabet=[chr(i) for i in range(97, 123)]
    return ("".join([(str(alphabet.index(letter)+1)+' ') if letter in alphabet else "" for letter in text.lower()])).strip()
