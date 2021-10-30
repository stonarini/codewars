# https://www.codewars.com/kata/51c8e37cee245da6b40000bd
# Strip Comments

# First Implementation 15/10/2021
def solution(string,markers):
    letterIndex=0
    string=string.replace('\n', '|')
    while letterIndex < len(string):
        if letterIndex == len(string): break
        if string[letterIndex] in markers:
            if string.find('|', letterIndex) == -1:
                string=(string[:letterIndex]).strip()
                break
            else:
                string=(string[:letterIndex]).strip() + string[string.find('|', letterIndex):]
                letterIndex=string.find('|', letterIndex-1)
        letterIndex+=1
    return string.replace('|', '\n')