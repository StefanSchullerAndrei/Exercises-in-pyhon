#Given a number n, for each integer i in the range from 1 to n inclusive, print one value per line
#as follows:

# if i is a multiple of both 3 and 5, print FizzBuzz.
# if i is a multiple of 3 (but not 5), print Fizz.
# if i is a multiple of 5 (but not 3), print Buzz.
# if i is not a multiple of 3 and 5, print the value of i


from art import logo

print(logo)

def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzBuzz(n=101)  #Call fizzBuzz game and write the number untill you want the game to count