n, cnt, max, pos = int(input()), 0, 0, 0
while n:
    if max < n: 
        max = n
        pos = cnt
    cnt +=1
    n = int(input())
print(pos)