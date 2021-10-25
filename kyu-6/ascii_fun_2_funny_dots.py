# https://www.codewars.com/kata/59098c39d8d24d12b6000020
# ASCII Fun #2: Funny Dots

# First Implementation 02/10/2021
def dot(row,column):
    line="+---"
    dot="| o "
    output=""
    
    for i in range(column):
        output+=line*row+"+\n"
        output+=dot*row+"|\n"
    
    output+=line*row+"+"
    
    return output

