# https://www.codewars.com/kata/55a2d7ebe362935a210000b2
# Find the Smallest Integer in the Array

# First Implementation 17/10/2021
find_smallest_int <- function(arr) {
  smallest_int <- arr[1]
  for (i in arr) {
    if (i < smallest_int) {
      smallest_int <- i
    }
  }
  return(smallest_int)
}

# Second Implementation 25/10/2021
find_smallest_int <- min