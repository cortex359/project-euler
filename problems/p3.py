# Problem 3: Largest Prime Factor
# -------------------------------
import math
import sys
from collections import deque
import sympy


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gen_prime_list(n: int) -> list[int]:
    prime_list = [2]
    for i in range(3, n + 1, 2):
        if is_prime(i):
            prime_list.append(i)
        if i % 10_000 == 1:
            print(i)

    return prime_list


def prime_factors(n: int) -> list[int]:
    prime_factor_list = []
    pl = deque(prime_list)
    i = pl.popleft()
    while i <= (n // 2):
        if n % i == 0:
            prime_factor_list.append(i)
        i = pl.popleft()
    return prime_factor_list


def v1(test_number):
    if is_prime(test_number):
        print(f"Number {test_number} is prime, so itself is it's single largest prime")
    else:
        prime_list = gen_prime_list(test_number)
        print(f"Created a list of {len(prime_list)} primes lower than {test_number}")
        pf_list = prime_factors(test_number)
        print(pf_list)
        print(f"Largest prime factor: {pf_list[-1]}")


def v2(test_number):
    i: int = test_number // 2
    while i >= 2:
        if is_prime(i) and test_number % i == 0:
            return i
        if i % 5000:
            print(i)
        i -= 1
    return 1


def v3(test_number):
    n = test_number
    for i in range(2, n):
        if n % i == 0:
            n = n // i
            if n > 1 and is_prime(n):
                return n


test_number: int = int(sys.argv[1]) if len(sys.argv) > 1 else 600_851_475_143

### my approach
print(v3(test_number))

### SymPy
print(sympy.primefactors(test_number))
