# https://www.codewars.com/kata/54e6533c92449cc251001667
# Unique in Order

# First Implementation 01/10/2021
def unique_in_order(iterable):
    unique_list=[]
    previous_item=""
    for item in iterable:
        if item != previous_item:
            unique_list.append(item)
        previous_item=item
    return unique_list
