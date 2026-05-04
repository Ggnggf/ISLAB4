import hashlib

# Hash
def hash_msg(m):
    return int(hashlib.sha256(m.encode()).hexdigest(), 16)

# Sign
def sign(m):
    h = hash_msg(m)
    return pow(h, d, n)

# Verify
def verify(m, sig):
    h = hash_msg(m)
    return pow(sig, e, n) == h % n

# Test
message = "Hello"
signature = sign(message)

print("Signature:", signature)
print("Valid:", verify(message, signature))

# Modify message
fake = "Hella"
print("After change:", verify(fake, signature))