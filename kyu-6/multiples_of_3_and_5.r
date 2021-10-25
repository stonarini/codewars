# https://www.codewars.com/kata/514b92a657cdc65150000006
# Multiples of 3 and 5

# First Implementation 17/10/2021
solution <- function(number) {
  if (number < 0) {
    return <- 0
  }
  index <- 1:number - 1
  return <- sum(index[index %% 3 == 0 | index %% 5 == 0])
}

# --------------------

# Second Implementation 17/10/2021
solution <- function(number) {
  index <- 1:number - 1
  return <- sum(index[index %% 3 == 0 | index %% 5 == 0])
}