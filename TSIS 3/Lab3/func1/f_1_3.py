def solve(numheads, numlegs):
    y = numlegs/2 - numheads
    x = numheads - y
    print(int(x), int(y))

numheads = int(input('Enter the number of heads: '))
numlegs = int(input('Enter the even number of legs: '))
if numlegs%2!=0:
    print('Read the condition carefully!')
else:
    solve(numheads, numlegs)
