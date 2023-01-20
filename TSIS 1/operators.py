print(10 + 5)
print()

print(10 ** 2)
print()

print(10 // 5)
print()

x = 5
x &= 3
print(x)#if the corresponding bit of x AND of y is 1, otherwise it's 0.
print()

x = 5
x >>= 3
print(x) #//'ing x by 2**y.

x = 5
x <<= 3
print(x) #multiplying x by 2**y.
print()

x = 5
x |= 3
print(x) # Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
print()

x = 5
x ^= 3
# Each bit of the output is the same as the corresponding bit 
# in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1
print(x)
print()

