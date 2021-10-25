# https://www.codewars.com/kata/554b4ac871d6813a03000035
# Highest and Lowest

# First Implementation 01/10/2021
def high_and_low(numbers):
    num_list = numbers.split(" ")
    high_num = int(num_list[0])
    low_num = int(num_list[0])
    
    for num in num_list:
        num = int(num)
        if num > high_num:
            high_num = num
        if num < low_num:
            low_num = num
            
    return str(high_num) + " " + str(low_num)
