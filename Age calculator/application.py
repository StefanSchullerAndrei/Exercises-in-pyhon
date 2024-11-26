# Age calculator
# description: write a program that calculates a persons age based on their birthdate and todau's date. optionally, calculate their age in days, months and years.
# key concepts: date manipulation, date libraries

from datetime import datetime
from art import logo


class AgeCalculator:
    def __init__(self):
        self.birthdate = self.get_birthdate_from_user()

    def get_birthdate_from_user(self):
        birthdate_input = input("Please enter your date of birth (DD-MM-YYYY): ")
        return datetime.strptime(birthdate_input, "%d-%m-%Y")

    def calculate_age(self):
        today = datetime.today()
        birthdate = self.birthdate

        # Calculate age in years
        age_years = today.year - birthdate.year
        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            age_years -= 1

        # Calculate age in months
        age_months = (today.year - birthdate.year) * 12 + today.month - birthdate.month
        if today.day < birthdate.day:
            age_months -= 1

        # Calculate age in days
        age_days = (today - birthdate).days

        return age_years, age_months, age_days

    def display_age(self):
        age_years, age_months, age_days = self.calculate_age()
        print(f"Age in years: {age_years}")
        print(f"Age in months: {age_months}")
        print(f"Age in days: {age_days}")


# Create an instance of AgeCalculator and display the age
print(logo)
age_calculator = AgeCalculator()
age_calculator.display_age()