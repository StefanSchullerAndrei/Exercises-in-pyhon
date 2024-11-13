#Palindrome Checker
#Description: Write a program to check if a given word or phrase is a palindrome, ignoring spaces and punctuation.
#Key concepts: String reversal, string cleaning (removing spaces and punctuation)

from art import logo


def palindrome_checker():
    print(logo)
    word_to_check = input("Please write the word that you wish to check for: ")

    word_to_check = word_to_check.lower().replace(' ', '')
    if word_to_check == word_to_check[::-1]:  #check if the string is equal to it's reverse
        print(f"The word {word_to_check} is a palindrome")

    else:
        print(f"The word {word_to_check} is not a palindrome")

palindrome_checker()