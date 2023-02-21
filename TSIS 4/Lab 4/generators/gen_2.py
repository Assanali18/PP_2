def gensequence(N):
    for i in range(N+1):
        if i%2 == 0: yield i 

N= int(input())
for i in gensequence(N):
    print(i, end = ', ') if i<N and i != N-1 else print(i)