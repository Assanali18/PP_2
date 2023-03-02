import re
txt = input()
res =  re.sub(r'([A-Z])', r' \1', txt)
print(res)