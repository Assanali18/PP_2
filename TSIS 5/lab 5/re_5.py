import re
txt = input()
x = re.search("a.*b$", txt)
print ('Match found') if x else print('Match not found')