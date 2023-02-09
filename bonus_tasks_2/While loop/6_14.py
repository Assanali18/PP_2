n, n0, n1, k, cnt = int(input()), 0, 1, 0, 1
if n == 0:
    print(0)
elif n ==1:
    print(1)
else:
    while cnt != n:
        if cnt > n: break
        k, n0, cnt = n0 + n1, n1, cnt +1
        n1 = k
    print(k)