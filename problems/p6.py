# Problem 6: Sum Square Difference
# --------------------------------
n = 100

sum_of_squares: int = n * (n + 1) * (2*n + 1) // 6
square_of_sums: int = (n * (n + 1)) ** 2 // 4
print(sum_of_squares, square_of_sums, (square_of_sums - sum_of_squares))
