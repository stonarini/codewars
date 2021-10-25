# https://www.codewars.com/kata/59f11118a5e129e591000134
# Sum of Array Singles

# First Implementation 15/10/2021
def repeats(arr):
    number_count={}
    for number in arr:
        try:
            number_count[str(number)] += 1
        except:
            number_count[str(number)] = 1
            
    total=0
    for number in number_count:
        if number_count[number] == 1:
            total+=int(number)
    return(total)
