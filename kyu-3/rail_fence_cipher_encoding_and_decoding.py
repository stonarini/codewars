# https://www.codewars.com/kata/58c5577d61aefcf3ff000081
# Rail Fence Cipher: Encoding and Decoding

# First Implementation 04/11/2021
def encode_rail_fence_cipher(string, n):
    rail=[[] for _ in range(n)]
    stringIndex=0
    railIndex=0
    goingDown=True
    while stringIndex < len(string):
        while railIndex != n and goingDown and stringIndex < len(string):
            rail[railIndex].append(string[stringIndex])
            railIndex+=1
            stringIndex+=1
        goingDown=not goingDown
        railIndex-=1
        while railIndex > 0 and not goingDown and stringIndex < len(string):
            railIndex-=1
            rail[railIndex].append(string[stringIndex])
            stringIndex+=1
        railIndex+=1
        goingDown=not goingDown
            
    return "".join(["".join(list) for list in rail])
            
def decode_rail_fence_cipher(string, n):
    rail = [[]for _ in range(n)]
    stringIndex=0
    railIndex=0
    goingDown=True
    while stringIndex < len(string):
        while railIndex != n and goingDown and stringIndex < len(string):
            rail[railIndex].append(string[stringIndex])
            railIndex+=1
            stringIndex+=1
        goingDown=not goingDown
        railIndex-=1
        while railIndex > 0 and not goingDown and stringIndex < len(string):
            railIndex-=1
            rail[railIndex].append(string[stringIndex])
            stringIndex+=1
        railIndex+=1
        goingDown=not goingDown
            
    railMask = [len(list) for list in rail]
    previousMask = 0
    rail = []
    for mask in railMask:
        rail += [string[previousMask:mask+previousMask]]
        previousMask=mask+previousMask
        
    stringIndex=0
    railIndex=0
    goingDown=True
    decodedString=""
    while stringIndex < len(string):
        while railIndex != n and goingDown and stringIndex < len(string):
            decodedString+=rail[railIndex][0]
            rail[railIndex]=rail[railIndex][1:]
            railIndex+=1
            stringIndex+=1
        goingDown=not goingDown
        railIndex-=1
        while railIndex > 0 and not goingDown and stringIndex < len(string):
            railIndex-=1
            decodedString+=rail[railIndex][0]
            rail[railIndex]=rail[railIndex][1:]
            stringIndex+=1
        railIndex+=1
        goingDown=not goingDown
        
    return decodedString
