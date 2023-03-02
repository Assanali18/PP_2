import datetime

x = datetime.datetime.now()

print(x)
#2023-02-21 13:42:03.090441

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
#2023
#Tuesday

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
#2020-05-17 00:00:00

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
#June
