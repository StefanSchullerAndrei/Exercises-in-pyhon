# The Challenge:
# Description: Create a program that calculates the tip amount and total bill based on the bill amount and
# the percentage tip the user wants to give.
from art import logo

def tip_calculator():
    print(logo)
    money_spent = float(input("How much is your bill? -> "))
    tip_percentage = float(input("What percentage of your bill do you want to leave as a tip? -> "))

    while tip_percentage not in [10, 15, 20]:
        money_spent = int(input("How much is your bill> -> "))
        tip_percentage = int(input("What percentage of your bill do you want to leave as a tip? -> "))

    else:
        if tip_percentage == 10:
            tip_amount = money_spent * 0.10
        elif tip_percentage == 15:
            tip_amount = money_spent * 0.15
        elif tip_percentage == 20:
            tip_amount = money_spent * 0.20

    total_amount = tip_amount + money_spent

    print(f"The tip you want to leave is {tip_amount}.")
    print(f"The total amount that you need to pay is {total_amount}.")

tip_calculator()

