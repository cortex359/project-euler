
fibonacci_numbers: list[int] = [1, 2]
number = 2
while number < 4_000_000:
    number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(number)

print(sum([f for f in fibonacci_numbers if f % 2 == 0]))
