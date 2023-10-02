import time


def calculate_time(date1, date2):
    alt_date1 = time.strptime(date1, "%Y-%m-%d")
    alt_date2 = time.strptime(date2, "%Y-%m-%d")

    time_difference = time.mktime(alt_date2) - time.mktime(alt_date1)

    days_difference = int(time_difference / 86400)

    print("Number of days between dates=" + "{:.1f}".format(days_difference))


d1 = input("Date1:")
d2 = input("Date2:")

calculate_time(d1, d2)