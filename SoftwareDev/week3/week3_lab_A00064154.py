#STUDENT ID - A00064154
#STUDENT NAME - SZYMON PODRAZA-OSTREGA

#Exercise 1
a = "1"
b = 2
print((int(a) + b))

#Exercise 2
pirates = int(input("Enter the amount of pirates:\n"))
gold = int(input("Enter the amount of gold:\n"))

coins_per_pirate = gold // pirates
leftover_coins = gold % pirates

print(f"Total coins: {gold}")
print(f"Number of pirates: {pirates}")

print(f"Each pirate gets {coins_per_pirate} gold coins.")
print(f"Coins leftover: {leftover_coins}.")

#Exercise 3
hours = int(input("Enter the number of hours:\n"))
minutes = int(input("Enter the number of minutes:\n"))
seconds = int(input("Enter the number of seconds:\n"))

hours_to_seconds = hours * 3600
minutes_to_seconds = minutes * 60
total_sec = hours_to_seconds + minutes_to_seconds + seconds

print(f"The total seconds is: {total_sec}")

#Exercise 4
PI = 3.14159
radius = float(input("Enter the radius:\n"))
area = PI * radius ** 2
print(round(area,2))

#Exercise 5
input_seconds = int(input("Enter the number of seconds:\n"))
seconds_to_hours = input_seconds // 3600
remainder_seconds_from_hours = input_seconds % 3600
seconds_to_minutes = remainder_seconds_from_hours // 60
leftover_seconds = input_seconds % 60

print(f"Hours: {seconds_to_hours} Minutes: {seconds_to_minutes} Seconds: {leftover_seconds}")