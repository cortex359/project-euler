# Problem 10: Summation of Primes
# -------------------------------
import math


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
    return prime_list


print(sum(gen_prime_list(2_000_000)))