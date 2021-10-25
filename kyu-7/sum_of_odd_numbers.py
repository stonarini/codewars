# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
# Sum of Odd Numbers

# First Implementation 01/10/2021
def row_sum_odd_numbers(n):
    first_column_number = (n * (n - 1)) + 1
    sum_of_odd_num = first_column_number
    i = 1
    while i < n:
        sum_of_odd_num += first_column_number + (2 * i)
        i += 1
    return sum_of_odd_num
