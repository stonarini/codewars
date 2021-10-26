# https://www.codewars.com/kata/52e1476c8147a7547a000811
# Regex Password Validation

# First Implementation 03/10/2021
regex="^(?!.*[\W_])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{6}"

# ^ checks from the beginning of the line
# (?!.*[\W_]) checks if there aren't any non-alphanumerical characters
# (?=.*[a-z]) checks for at least 1 lowercase character in all the string
# (?=.*[A-Z]) checks for at least 1 uppercase character in all the string
# (?=.*[0-9]) checks for at least 1 number in all the string
# .{6} checks for at least 6 characters
