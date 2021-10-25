# https://www.codewars.com/kata/550498447451fbbd7600041c
# Are They the "Same"?

# First Implementation 01/10/2021
def comp(array1, array2):
    if array1 == None or array2 == None: return False
    square_list = array2

    for squared_num in array1:
        for num in array2:
            if num == squared_num**2:
                square_list.remove(num)
                break
    
    return True if square_list == [] else False

