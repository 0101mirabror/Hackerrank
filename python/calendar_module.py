import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(5000))
data = list(map(int, input().split()))
weekday_number = calendar.weekday(data[2], data[0], data[1])
# print(weekday_number)
print(calendar.day_name[weekday_number].upper())