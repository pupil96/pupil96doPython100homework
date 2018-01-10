# 输入某年某月某日，判断这一天是这一年的第几天？
# 30day 4 6 9 11
# 28/29day 2
# 31day 1 3 5 7 8 10 12

month_s = [4, 6, 9, 11]
month_m = [2]
month_b = [1, 3, 5, 7, 8, 10, 12]
# 防止用户输入错误的值进行计算  比如 2/30 3/32 4/31
year = 0
month = 0
day = 0
calculateDay = 0


def my_get_year():
    global year
    year = int(input("please input year:"))  # 不考虑年限的合法性


def my_get_month():
    global month
    while True:
        # noinspection PyBroadException
        try:
            month = int(input("please input month:"))
            if 1 <= month <= 12:  # 合法月份
                break
            else:
                print("illegal input")
        except Exception:
            print("illegal input")


def my_get_day():
    global year, month, day
    while True:
        # noinspection PyBroadException
        try:
            day = int(input("please input day:"))
            if month in month_s:
                if 1 <= day <= 30:
                    break
            elif month in month_b:
                if 1 <= day <= 31:
                    break
            elif month in month_m:
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    if 1 <= day <= 29:
                        break
                else:
                    if 1 <= day <= 28:
                        break
            else:
                print("illegal input")
        except Exception:
            print("illegal input")


if __name__ == "__main__":
    my_get_year()
    my_get_month()
    my_get_day()
    if 1 <= month < 2:
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
