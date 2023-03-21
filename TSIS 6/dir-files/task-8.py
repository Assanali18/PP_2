import os
if os.path.exists("efef.txt"):
  os.remove("efef.txt")
else:
  print("The file does not exist")