#Task 5:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and determines the day of the week on which that date falls.
import datetime
date=datetime.date(day=13,month=6,year=2022)
print(date.strftime('%A'))