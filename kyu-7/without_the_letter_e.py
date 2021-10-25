# https://www.codewars.com/kata/594b8e182fa0a0d7fc000875
# Without the Letter 'e'

# First Implementation 01/10/2021
def find_e(s):
    if s == '': return s
    try:
        letter_list=(char for char in s)
    except:
        return s
    
    e_count=0
    for letter in letter_list:
        if letter.lower() == "e":
            e_count += 1
    
    if e_count == 0:
        return "There is no \"e\"."
    else:
        return str(e_count)
