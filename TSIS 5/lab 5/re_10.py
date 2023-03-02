import re
txt = input()
res =  re.sub(r'([a-z])([A-Z])', r'\1_\2', txt).lower()
print(res)