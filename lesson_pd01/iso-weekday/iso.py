import datetime


def iso_weekday(date):
    date_object = datetime.datetime.strptime(date, "%d/%m/%Y")

    iso_weekday = date_object.isoweekday()
    iso_week = date_object.strftime("%V")

    print("weekday =", int(iso_weekday), end="")
    print(", ", end="")
    print("week =", int(iso_week), end="")


d1 = input("Date:")

iso_weekday(d1)