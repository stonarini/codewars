# https://www.codewars.com/kata/523f5d21c841566fde000009
# Array.diff

# First Implementation 01/10/2021
def array_diff(a, b):
    i = len(a) - 1
    for value_to_remove in b:
        while(i >= 0):
            if a[i] == value_to_remove:
                a.remove(value_to_remove)
            i=i-1
        i = len(a) - 1
    
    return a
