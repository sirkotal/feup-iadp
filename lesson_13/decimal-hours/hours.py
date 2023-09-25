def dechours_to_hms(time):
    hours = int(time)
    mins = (time * 60) % 60
    secs = (time * 3600) % 60
    return ("%d hours, %02d minutes, %02d seconds" % (hours, mins, secs))