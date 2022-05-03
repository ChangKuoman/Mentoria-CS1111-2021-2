
# K(n, p) = (1 * p) + (2 ∗ p) + (3 ∗ p) + (4 ∗ p) + ... + (n ∗ p)

# Input n: 5
# Input p: 2
# Output : 30

# Input n: 6
# Input p: 3
# Output : 63

def K(n, p):
    if n == 1:
        return p
    else:
        return n*p + K(n-1, p)

print(K(5, 2))
print(K(6, 3))
