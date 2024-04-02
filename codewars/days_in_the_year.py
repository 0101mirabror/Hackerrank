def year_days(year):
    if year%400==0:
        return f'{year} has 366 days'
    elif year%100!=0 and year%4==0:
        return f'{year} has 366 days'
    return f'{year} has 365 days'
print(year_days(2000))
print(year_days(1900))
print(year_days(0))
print(year_days(-10))

# best practice
# def year_days(year):
#     days = 365
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         days += 1
#     return "%d has %d days" % (year, days)