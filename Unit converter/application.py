# Unit Converter
# •	Description: Build a unit converter that converts values between units (e.g., kilometers to miles, Celsius to Fahrenheit, kilograms to pounds, etc.). Allow the user to select the units and provide the input value.
# •	Key Concepts: User input, arithmetic operations, dictionaries for conversion factors.

from art import logo

# Conversion functions
def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(mi):
    return mi / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lb):
    return lb / 2.20462

# Dictionary of conversion functions
conversion_functions = {
    'km_to_mi': kilometers_to_miles,
    'mi_to_km': miles_to_kilometers,
    'c_to_f': celsius_to_fahrenheit,
    'f_to_c': fahrenheit_to_celsius,
    'kg_to_lb': kilograms_to_pounds,
    'lb_to_kg': pounds_to_kilograms
}

def main():
    print("Unit Converter")
    print("Select the conversion:")
    print("1: Kilometers to Miles")
    print("2: Miles to Kilometers")
    print("3: Celsius to Fahrenheit")
    print("4: Fahrenheit to Celsius")
    print("5: Kilograms to Pounds")
    print("6: Pounds to Kilograms")

    choice = input("Enter the number of your choice: ")
    value = float(input("Enter the value to convert: "))

    if choice == '1':
        converted_value = conversion_functions['km_to_mi'](value)
        print(f"{value} kilometers is equal to {converted_value} miles.")
    elif choice == '2':
        converted_value = conversion_functions['mi_to_km'](value)
        print(f"{value} miles is equal to {converted_value} kilometers.")
    elif choice == '3':
        converted_value = conversion_functions['c_to_f'](value)
        print(f"{value} Celsius is equal to {converted_value} Fahrenheit.")
    elif choice == '4':
        converted_value = conversion_functions['f_to_c'](value)
        print(f"{value} Fahrenheit is equal to {converted_value} Celsius.")
    elif choice == '5':
        converted_value = conversion_functions['kg_to_lb'](value)
        print(f"{value} kilograms is equal to {converted_value} pounds.")
    elif choice == '6':
        converted_value = conversion_functions['lb_to_kg'](value)
        print(f"{value} pounds is equal to {converted_value} kilograms.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    print(logo)
    main()
