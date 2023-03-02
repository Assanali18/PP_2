import re
txt = input()
res = re.sub(r'(?:^|_)(.)', lambda x: x.group(1).upper(), txt)
print(res)