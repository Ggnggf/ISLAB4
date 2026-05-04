# Small primes
p, q = 11, 13
n = p * q
phi = (p-1)*(q-1)

e = 7  # public key

# Find d (private key)
def inv(e, phi):
    for i in range(1, phi):
        if (e*i) % phi == 1:
            return i

d = inv(e, phi)

# Encrypt / Decrypt
def enc(m): return pow(m, e, n)
def dec(c): return pow(c, d, n)

# Test
msg = [ord(c) for c in "Ali"]
cipher = [enc(x) for x in msg]
plain = ''.join(chr(dec(x)) for x in cipher)

print("Encrypted:", cipher)
print("Decrypted:", plain)