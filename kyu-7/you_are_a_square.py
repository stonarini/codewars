# https://www.codewars.com/kata/54c27a33fb7da0db0100040e
# You're a Square!

# First Implementation 16/10/2021
def is_square(n):    
    if n < 0: 
        return False
    res = n**0.5
    if res.is_integer():
        return True
    return False

# --------------------

# Second Implementation 16/10/2021
def is_square(n):    
    return (n**0.5).is_integer() if n > -1 else False
