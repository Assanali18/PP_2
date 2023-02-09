n, max = int(input()), 0
while n:
    if max < n: max = n
    n = int(input())
print(max)