# 30day 4 6 9 11
# 28/29day 2
# 31day 1 3 5 7 8 10 12

month_s = [4, 6, 9, 11]
month_m = [2]
month_b = [1, 3, 5, 7, 8, 10, 12]

year = int(input("please input year:"))
month = int(input("please input month:"))
day = int(input("please input day:"))
calculateDay = 0

if month < 2:
    print("Today is %sth day in this year" % day)
elif month <= 12:
    for m in range(1, month):
        if m in month_b:
            calculateDay += 31
        elif m in month_s:
            calculateDay += 30
        elif m in month_m:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                calculateDay += 29
            else:
                calculateDay += 28
    print("Today is %sth day in this year" % (calculateDay+day))
