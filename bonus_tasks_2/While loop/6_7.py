n,sum, cnt = int(input()), 0, 0
while n:
    sum += n
    n = int(input())
    cnt+=1
print(float(sum/cnt))