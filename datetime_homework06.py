#Task 6:
#Write a Python program that accepts a date in the format "dd-mm-yyyy" and checks if it is a leap year. Display an appropriate message indicating whether it is a leap year or not.
import datetime
date=datetime.date(day=13,month=6,year=2020)
if date.year%4==0:
    print("leap year")
else:
    print("not leap year")