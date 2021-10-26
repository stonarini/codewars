# https://www.codewars.com/kata/5282b48bb70058e4c4000fa7
# Convert A Hex String To RGB

# First Implementation 18/10/2021
def hex_string_to_RGB(hex_string): 
    return {
        'r': int(hex_string[1:3], 16), 
        'g': int(hex_string[3:5], 16), 
        'b': int(hex_string[5:], 16) 
    }
