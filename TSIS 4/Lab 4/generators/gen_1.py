def gensequence(N):
    for i in range(N):
        yield i**2 

for i in gensequence(int(input())):
    print(i)