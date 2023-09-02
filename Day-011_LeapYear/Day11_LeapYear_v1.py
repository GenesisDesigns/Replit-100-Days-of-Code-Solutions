#Title: Replit Day  - Day11 - Leap Year - How many seconds in 1 year - v1


def isLeapYr(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        result = True
    else:
        result = False
    return result


print("How many years are in a given year ")
year = input("Enter the year: ")
year = int(year)
if isLeapYr(year) == True:
    days = 366
    print(f"{year} IS a leap year and has {days} days in a year.")
else:
    days = 365
    print(f"{year} is NOT a leap year and has {days} days in a year.")

hoursInDay = 24
minInHour = 60
secInMinutes = 60
secondsInYr = days * hoursInDay * minInHour * secInMinutes

print(f"There are {secondsInYr} seconds in {year}.")
