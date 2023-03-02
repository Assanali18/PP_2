import re
txt = input()
x = re.search("a(b){2,3}", txt)
print ('Match found') if x else print('Match not found')