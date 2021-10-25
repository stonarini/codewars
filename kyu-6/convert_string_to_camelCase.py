# https://www.codewars.com/kata/517abf86da9663f1d2000003
# Convert String to Camel Case

# First Implementation 02/10/2021
def toCamelCase(text):
    textList=list(text)
    newText=""
    i = 0
    while i < len(text):
        if textList[i] == "-" or textList[i] == "_":
            newText+=textList[i+1].upper()
            i+=2
        else:
            newText+=textList[i]
            i+=1
    return newText

