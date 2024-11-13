# 8. Even or Odd Number Checker
# Concepts: Conditionals, user input
# Description: Ask the user to input a number and determine if it is even or odd. You can also extend it by adding features like checking if it's positive, negative, or zero.

# from art import logo
# print(logo)
# number_introduced = int(input("Type the number you wish to check: "))
#
# if number_introduced % 2 == 0:
#     print("The number provided is Even")
#
# else:
#     print("The number is Odd")

#Adding more features

from art import logo
print(logo)
number_introduced = int(input("Type the number you wish to check: "))

if number_introduced % 2 == 0:
    x = "and Even"
    if number_introduced > 0:
        print(f"The number is positive {x}")

    elif number_introduced < 0:
        print(f"The number is negative {x}")

    # elif number_introduced == 0:
    #     print(f"The number is null {x}" )

elif number_introduced % 2 != 0:
    y = "and Odd"
    if number_introduced > 0:
        print(f"The number is positive {y}")
    elif number_introduced < 0:
        print(f"The number is negative {y}")