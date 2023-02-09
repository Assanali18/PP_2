n0, n1,cnt, n = 1, 1, 2, int(input())
while n1 < n:
    n1, n0, cnt = n1+n0, n1, cnt +1
print (cnt) if n1 == n else print (-1)