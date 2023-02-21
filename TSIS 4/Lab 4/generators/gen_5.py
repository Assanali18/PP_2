def gensequence(N):
    for i in range(N,0, -1):
        yield i

for i in gensequence(int(input())):
    print(i)