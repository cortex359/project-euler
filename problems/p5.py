# Problem 5: Smallest Multiple
# ----------------------------
import math

# divisible by all numbers from 1 to 10
# testing for 10, includes 2, 5
# testing for  9, includes 3
# testing for  8, includes 4, 2
# testing for  7
# testing for  6, includes 3, 2
i = 10
while True:
    if len([divisor for divisor in [10, 9, 8, 7, 6] if i % divisor == 0]) == 5:
        print(i)
        break
    i += 1

print(math.lcm(*list(range(2, 21))))
