import calendar


def set_first_week_day(new_day):
    first_day = calendar.firstweekday()

    calendar.setfirstweekday(new_day)

    new_default = calendar.firstweekday()

    print("First day of the week:", calendar.day_name[new_default])


d1 = int(input("Day of the week (0-6):"))

set_first_week_day(d1)