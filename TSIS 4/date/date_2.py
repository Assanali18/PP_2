import datetime
print('Yesterday: ', datetime.datetime.now() - datetime.timedelta(days = 1))
print('Today: ',datetime.datetime.now())
print('Tomorrow: ',datetime.datetime.now() + datetime.timedelta(days = 1))