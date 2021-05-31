import math
import base64
import random


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
p = get_prime(10)
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

print()

# Confirming crypto key
c_key = int

if g_ba == g_ab:
    c_key = g_ab
    print('collective cryptographic key: ', c_key)
else:
    print('Diffie-Hellman process failed \t No key')

# Performing stream cryptography on ciphers and messages
print('\n\n')
print('Cryptography process: \n')


class KeyStream:
    def __init__(self, key=c_key):
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345)  % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256


def encrypt(key, message):
    return bytes(message[i] ^ key.get_key_byte() for i in range(len(message)))


key = KeyStream(8)
message = input("Enter your message: ")
message = message.encode()
cipher = encrypt(key, message)
cipher = base64.b64encode(cipher)
cipher = str(cipher)
cipher = cipher.lstrip("b'")
cipher = cipher.rstrip("'")
print()
print("Cipher: ", cipher)

print()

key = KeyStream(8)
cipher = input("Enter your cipher: ")
cipher = cipher.encode()
cipher = base64.b64decode(cipher)
message = encrypt(key, cipher)
message = str(message)
message = message.lstrip("b'")
message = message.rstrip("'")
print()
print("Message: ", message)

print()
print()
print("This service has now been ended")
print("AKC Productions")
