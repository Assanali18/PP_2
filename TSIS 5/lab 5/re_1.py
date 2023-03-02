import re
txt = input()
x = re.search(".*ab+", txt)
print ('Match found') if x else print('Match not found')