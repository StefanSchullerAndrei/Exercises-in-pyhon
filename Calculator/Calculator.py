# Calculator
# Concepts: Basic arithmetic, functions, user input
# Description: Build a basic calculator that can perform simple operations like addition, subtraction, multiplication, and division.

from art import logo

def addition(x,y):
    return x + y

def substraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

# ---------------------------------------

def menu():
    print("What operation do you want to use?")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

def calculator():
    print(logo)
    menu()
    choice = input("Enter choice (1, 2, 3, 4): ")

    if choice in ("1", "2", "3", "4"):
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))

        if choice == "1":
            print("Your result is ", addition(x, y))

        elif choice == "2":
            print("Your result is ", substraction(x, y))

        elif choice == "3":
            print("Your result is ", multiplication(x, y))

        elif choice == "4":
            print("Your result is ", division(x, y))

calculator()