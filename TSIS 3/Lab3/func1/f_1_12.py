def hystogram(args):
    for i in range(len(args)): print(args[i]*'*') 
hystogram([int(i) for i in input().split()])