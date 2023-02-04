n, cnt, k = int(input()), 1, 2
if n == 1: print(0, 1)
else:
    while k*2 <= n:
        k *= 2
        cnt += 1
    print(cnt, k)
