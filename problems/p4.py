# Largest Palindrome Product
import itertools


def is_palindrome(n: int) -> bool:
    n_str: str = str(n)
    for c in range(len(n_str) // 2):
        if n_str[c] != n_str[-c - 1]:
            return False
    return True


palindroms = []
for i, j in itertools.combinations(list(range(1000, 100, -1)), r=2):
    product = i * j
    if is_palindrome(product):
        palindroms.append((i, j, product))

print(sorted(palindroms, key=lambda x: x[2])[-1])
