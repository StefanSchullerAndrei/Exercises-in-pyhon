#Time converter
#Description: Write a program that converts a time duration in seconds to hours, minutes, and seconds (e.g., 3661 seconds becomes 1 hour, 1 minute, and 1 second).
#Key concepts: Modular arithmetic, division, user input.

import math



# MINUTE = 60
# HOURS = 3600
# DAYS = 86400
# print(DAYS * 3.5)
# print(302400 - (DAYS*3))
# x = 302400
# print(x % DAYS)
# y = 43200
# print(y / HOURS)

# Version 1 of the time converter. The user can convert from seconds to days, hours, minutes, seconds
def convert_seconds(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return days, hours, minutes, seconds

# Get user input
total_seconds = int(input("Enter the time duration in seconds: "))

# Convert and display the result
days, hours, minutes, seconds = convert_seconds(total_seconds)
print(f"{total_seconds} seconds is equal to {days} day(s), {hours} hour(s), {minutes} minute(s), and {seconds} second(s).")

#Version 2 of the time converter. The user can choose from which unit he wants to convert to what unit he desires
#Conversion factors to seconds
# def convert_time(seconds):
#     days = seconds // 86400
#     hours = (seconds % 86400) // 3600
#     minutes = (seconds % 3600) // 60
#     seconds = seconds % 60
#     return days, hours, minutes, seconds
#
#
# def time_converter():
#     time = int(input("Please type the number of units that need to be converted: "))
#     from_unit = input("Please type the unit you want to convert from (seconds, minutes, hours, days): ").lower()
#     to_unit = input("Into (seconds, minutes, hours, days): ").lower()
#
#     # Conversion factors to seconds
#
#
#     # Check if the input units are valid
#     if from_unit in convert_time and to_unit in convert_time:
#         # Convert the input time to seconds
#         time_in_seconds = time * convert_time[from_unit]
#
#         # Convert the time in seconds to the target unit
#         days, hours, minutes, seconds = convert_time(time_in_seconds)
#
#         print(
#             f"{time} {from_unit} is equal to {days} day(s), {hours} hour(s), {minutes} minute(s), and {seconds} second(s).")
#     else:
#         print("Invalid unit entered. Please use 'seconds', 'minutes', 'hours', or 'days'.")
#
#
# # Run the time converter
# time_converter()