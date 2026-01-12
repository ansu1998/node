# Date and time in python
# 1970 jan 12AM - Unix epoch time
import time, datetime, calendar 

print(time.time())
# This code imports the time module, retrieves the current time in seconds since the epoch (January 1, 1970)

print(time.localtime(time.time()))
# local_time structure (year, month, day, hour, minute, etc.)


print(time.asctime(time.localtime(time.time())))  

# # # sleep time
for i in range(0, 10):
    print(i)
    time.sleep(2)

print(datetime.datetime.now())


# # calendar
# cal = calendar.month(2025, 10)
# print(cal)

calendar.prcal(2025)