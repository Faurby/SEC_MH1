
# Shared base g
g = 666

# Shared prime p
p = 6661

# Bob's public key PK = g^sk mod p
bobPK = 2227

# Select random r as Alice's SK 
r = 5125

def encryption(m, pk):
    c1 = pow(g, r, p)
    c2 = (m * pk**r) % p
    return (c1, c2)

def decryption(c, sk):
    c1, c2 = c
    s = pow(c1, sk, p)
    m = (c2 * pow(s, -1, p)) % p
    return m

# Alice encrypting the message to Bob
c = encryption(2000, bobPK)

print("==== Assignment 1 ====\nAlice's encrypted message to Bob: ", c)

# brute force find Bob's SK
bobSK = 0
for i in range(6661):
    r = (g ** i) % p
    if (r == 2227):
        bobSK = i

# Decrypting the message using Bob's SK
m = decryption(c, bobSK)

print("\n==== Assignment 2 ====\nBob's secret key found using brute force: ", bobSK, "\nBob's decrypted message, as seen as Eve: ", m)

# Mallory intercepting Alice's message, and modifying it to decrypt to 6000
c1, c2 = c
c2 *= 3
c = (c1, c2)

# Bob decrypting the message
m = decryption(c, bobSK)
print("\n==== Assignment 3 ====\nBob decrypting the modified message from Mallory and receiving: ", m)