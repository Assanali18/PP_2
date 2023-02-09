n, pre, cnt = int(input()), 0, -1
while n:
    if n> pre: cnt+=1
    pre = n
    n = int(input())
print(cnt)