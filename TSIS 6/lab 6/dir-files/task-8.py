import os
if os.path.exists("test(delete).txt"):
  os.remove("test(delete).txt")
else:
  print("The file does not exist")