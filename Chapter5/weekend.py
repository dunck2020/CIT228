import datetime
# weekdays tuple
weekDays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# retrieve current date
now = datetime.date.today()
# retrieve the day of the week which is an integer
dayOfWeek = now.weekday()
# subscript into weekDays using dayOfWeek
today = weekDays[dayOfWeek]
# calculate and print days until the weekend
daysToWeekend = 6 - dayOfWeek
print(f'There are {daysToWeekend - 1} days until the weekend')
# flag to only print 1 quote in the for loop
quotePrinted = 'false'
# print week days left until weekend with a quote
for left in weekDays[dayOfWeek:daysToWeekend]:
    if today == 'Sunday' and quotePrinted == 'false':
        print(left, 'Sundays are the best days to relax')
        quotePrinted = 'true'
    elif (today == 'Monday' or today == 'Tuesday' or today == 'Wednesday') and quotePrinted == 'false':
        print(left, 'These are the most productive days of the week')
        quotePrinted = 'true'
    elif today == 'Thursday' and quotePrinted == 'false':
        print(left, 'Thursdays are pretty much Fridays in disguise, we are almost there')
        quotePrinted = 'true'
    elif quotePrinted =='false':
        print(left, 'Finally the weekend is here!!')
        quotePrinted = 'true'
    else:
        print(left)

