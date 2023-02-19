def gensequence(N):
    global cnt 
    cnt =0
    for i in range(N+1):
        if i%3 == 0 and i%4==0: 
            cnt+=1
            yield i
                  

N= int(input())
for i in gensequence(N):

    if cnt != 0:
        cnt-=1
        print(i, end = ' ')
    else:
        exit()
        
        
        
