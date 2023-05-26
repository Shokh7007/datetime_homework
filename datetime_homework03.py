#Task 3:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and calculates the number of days between the current date and the entered date.
import datetime
date=datetime.date(day=12,month=6,year=2022)
today=datetime.date.today()

print(today-date)