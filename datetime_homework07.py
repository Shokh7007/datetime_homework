#Task 7:
#Write a Python program that adds 5 days to the current date and displays the resulting date.
import datetime
today=datetime.date.today()
date=datetime.date(year=today.year,month=today.month,day=today.day+5)
print(date)