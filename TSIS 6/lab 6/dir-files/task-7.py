with open('test.txt','r') as firstfile, open('test(copy).txt','a') as secondfile:
    for line in firstfile:
        secondfile.write(line)