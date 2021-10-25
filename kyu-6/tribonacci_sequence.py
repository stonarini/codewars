# https://www.codewars.com/kata/556deca17c58da83c00002db
# Tribonacci Sequence

# First Implementation 04/10/2021
def tribonacci(signature, n):
    if n == 0: return []
    if n < 3: return signature[0:n]
    
    for i in range(n-3): 
        signature.append(signature[i]+signature[i+1]+signature[i+2])
    return signature
