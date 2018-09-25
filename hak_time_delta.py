from datetime import datetime

FMT = "%a %d %b %Y %H:%M:%S %z"

#%a weekday
#d day of the month
#b month name
# %Y year with century
# %H 24-hour clock
# %M minute
# %S second
# %z UTC

for i in range(int(input())):
    time_1 = datetime.strptime(input(), FMT)
    time_2 = datetime.strptime(input(), FMT)
    print(abs(int((t1-t2).total_seconds())))
