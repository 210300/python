from datetime import date
data = input().split()
day = int(data[0])
month = int(data[1])
givendate = date(2009,month,day)
weekday = givendate.strftime("%A")
print(weekday)