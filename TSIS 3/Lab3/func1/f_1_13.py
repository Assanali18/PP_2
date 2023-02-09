def play():
    import random
    x, cnt = int(random.randint(1, 20)), 0
    print('Well,', input('Hello! What is your name? \n') + ', I am thinking of a number between 1 and 20.')
    a = int(input('Take a guess. \n' ))
    while a!=x:
        if a> x: 
            print('Your guess is too large.')
            a = int(input('Take a guess. \n' ))
            cnt+=1
        elif a < x:
            print('Your guess is too low.')
            a = int(input('Take a guess. \n' ))
            cnt+=1
        if a ==x: 
            print('Good job, KBTU! You guessed my number in {} guesses!'.format(cnt))
