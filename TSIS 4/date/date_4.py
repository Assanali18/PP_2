import datetime
year =  datetime.datetime.now()
another_year =  datetime.timedelta(weeks=23, days=84, hours=23, minutes=51, seconds=821)
dif = year-another_year
print(dif.second)
