n, max, cnt = int(input()), 0, 1
while n:
    if max < n: 
        max, cnt = n, 1
    elif max == n:
        cnt+=1
    n = int(input())
print(cnt)