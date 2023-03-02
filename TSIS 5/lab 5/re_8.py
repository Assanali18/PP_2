import re
text = input()
res = re.findall(r'[a-z]+|[A-Z][a-z]*', text)
print(res)