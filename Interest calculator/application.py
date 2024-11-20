# Simple Interest Calculator
# •	Description: Write a program to calculate the simple interest on a principal amount over a specified time at a given rate.
# •	Key Concepts: Arithmetic operations, user input, basic financial formulas.

from art import logo


def simple_interest_calculator():
    print(logo)
    print("-" * 80)
    print("Welcome to the Simple Interest Calculator!")

    # User input for principal, rate, and time
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (in %): "))
        time = float(input("Enter the time (in years): "))

        #Simple Inrerest formula
        simple_interest = (principal * rate * time) / 100

        print(f"\n Principal Amount: {principal}")
        print(f"Annual interest Rate: {rate}%")
        print(f"Time: {time} years")
        print(f"Simple Interest; {simple_interest:.2f}")
        print(f"Total Amount (Principal + Interest): {principal + simple_interest:.2f}")
    except ValueError:
        print("\nInvalid input. PLease enter numeric values.")

simple_interest_calculator()