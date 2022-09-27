
# Shared base g
g = 666

# Shared prime p
p = 6661

# Bob's public key PK = g^sk mod p
bobPK = 2227

# 1. You are Alice, send the message '2000' to Bob

r = 5125

def encryption(m, pk):
    c1 = (g**r) % p
    c2 = m * ((pk**r) % p)
    return (c1, c2)

def decryption(c, sk):
    c1, c2 = c
    m = c2 / ((c1 ** sk) % p)
    return m

c = encryption(2000, bobPK)

print("==== Assignment 1 ====\nAlice's message to Bob: ", c)

m = decryption(c, 66)

print("\n==== Assignment 2 ====\nBob's decrypted message, as seen as Eve: ", m)