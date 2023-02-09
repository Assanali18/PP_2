def reverse(string):
    string.reverse()
    return str(string).replace('[','').replace(']','').replace("'", '').replace(',','')
string =  list(input( 'Enter your sentence: ').split(' '))
print('Reverse of your sentence:')
print(reverse(string))
