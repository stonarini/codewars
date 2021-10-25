# https://www.codewars.com/kata/5906436806d25f846400009b
# ASCII Fun #1: X Shape

# First Implementation 01/10/2021
def x(n):
    result=""
    for column in range(n):
        for row in range(n):
            if row == column:
                result += "■"
            elif row + column == n - 1:
                result += "■"
            else:
                result += "□"
        if column != n-1:
            result+="\n"

    return result
