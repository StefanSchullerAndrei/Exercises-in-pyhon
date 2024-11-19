import random
from art import logo
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Ensure there's at least one character type selected
    if not characters:
        fail = print("You must select at least one character type!")
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
def get_user_input():
    password_length = int(input("Enter the desired password length: "))
    print("_" * 80)
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    print("_" * 80)
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    print("_" * 80)
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    print("_" * 80)
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    print("_" * 80)

    # Generate and display password
    generated_password = generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_symbols)
    print("Generated password:", generated_password)

    if generated_password == "You must select at least one character type":
        print (generate_password)

get_user_input()