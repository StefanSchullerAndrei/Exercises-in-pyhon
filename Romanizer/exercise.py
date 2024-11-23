# Romanizer
# Given an integer, convert it to it's Roman numeral equivalent

import numbers
from art import logo


def romanizer(numbers):
    # Write your code here
    print(logo)
    roman_map = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",

    }

    roman_numerals = []
    for number in numbers:
        roman_num = ""
        for value, symbol in sorted(roman_map.items(), reverse=True):
            while number >= value:
                roman_num += symbol
                number -= value
        roman_numerals.append(roman_num)
    return roman_numerals

numbers = [3, 4, 9, 58, 1994]
print(romanizer(numbers))