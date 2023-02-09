n, k, cnt, max = int(input()), 0, 1, 1
while n:
    k = n
    n = int(input())
    if k == n:
        cnt +=1
        if max  < cnt:
            max =cnt
    else: cnt = 1
print(max)