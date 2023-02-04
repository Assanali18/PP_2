n, k, l = int(input()), 1, 0
while l <= n:
    l = k**2
    if l>n: break
    print(l)
    k+=1