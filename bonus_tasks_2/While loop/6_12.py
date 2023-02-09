n, max, premax = int(input()), -1, -1
while n:
    if max < n:
        premax, max = max, n
    elif n > premax:
        premax = n
    n = int(input())
print(premax)