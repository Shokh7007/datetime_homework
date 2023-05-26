#Task 4:
#Write a Python program that calculates the age of a person based on their birth year. Prompt the user to enter their birth year, and display their current age.
import datetime
date=datetime.date(day=12,month=6,year=2022)
today=datetime.date.today()
age=today.year-date.year
print(age)