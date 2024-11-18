#Counting Vowels in a String
# Concepts: Strings, loops, conditionals
# Description: Create a program that takes a string input and counts how many vowels are in the string.

from art import logo

# I start by creating two lists: one that contains all the vowels in the English language vocabulary
# and one that contains all the consonants.

print(logo)
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

#I define two variables that will hold the number of vowels, respectively of consonants
number_of_vowels = 0
number_of_consonants = 0

#Put the program to ask the user to input a word
string_provided = input("Please type a word to count -> ")

#Now the program will split the string into individual characters.
string_characters = list(string_provided)

#I create a loop that checks how many vowels the word given by the user has
for x in string_provided:
    if x in vowels:
        number_of_vowels = number_of_vowels + 1

    if x in consonants:
        number_of_consonants = number_of_consonants + 1

#Print an output message with the number of vowels and consonants
print(f"The word provided has {number_of_vowels} vowel(s) and {number_of_consonants} consonant(s).")