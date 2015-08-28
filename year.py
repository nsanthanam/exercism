def is_leap_year(year):
    if year % 400 is 0:
        leap_value = True
    elif year % 100 is 0:
        leap_value = False
    elif year % 4 is 0:
        leap_value = True
    else:
        leap_value = False
    return leap_value