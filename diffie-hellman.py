import random
import math


def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p%i == 0:
            return False
    return True


def get_prime(size):
    while True:
        p = random.randrange(size, size*2)
        if is_prime(p):
            break
    return p


def is_generator(g, p):
    for i in range(1, p-1):
        if (g**i) % p == 1:
            return False
    return True


def get_generator(g):
    for g in range(2, p):
        if is_generator(g, p):
            return g


# p = get_prime(1000)
# g = get_generator(p)
# print(g, p)


# Public Area
p = get_prime(10000)
g = get_generator(p)
print("Public generator: ",g, "\nPublic Prime Number: ", p)

# Alice (private)
a = random.randrange(0, p)
g_a = (g**a) % p
# Alice (public)
print("Alice sends this to an unsecure domain: ", g_a)

# Bob (private)
b = random.randrange(0, p)
g_b = (g**b) % p
# Bob (public)
print("Bob sends this to an unsecure domain: ", g_b)

print("\n")

# Alice (private)(received Bob's generator)
g_ab = (g_b**a) % p
print("Key created by Alice: ", g_ab)

# Bob (private)(received Alice's generator)
g_ba = (g_a**b) % p
print("Key created by Bob: ", g_ba)
