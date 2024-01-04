# Problem 9: Special Pythagorean Triplet
# --------------------------------------

def find_pythagorean_tripplet():
    for a in range(1, 1000):
        for b in range(1, 1000 - a):
            c = 1000 - a - b
            if c < 1:
                continue
            if a * a + b * b == c * c:
                return (a, b, c)


a, b, c = find_pythagorean_tripplet()
print(f"{a}² + {b}² = {c}²")
print(a * a, "+", b * b, "=", c * c)
print(f"product: {a * b * c}")
