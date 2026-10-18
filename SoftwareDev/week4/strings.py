# string1 = "hello"
# print(string1 * 3)

# string2 = (string1 + " ") * 2 + string1
# print(string2)

# print(len(string2))

# print(string1.upper())
# print(string1.lower())
# print(string1.capitalize())

# price = 23.53913
# print(f"The price is {price:.2f}") #Rounding within f-string

# big_number = 623467924658236
# print(f"The number is {big_number:,}") #Adds commas to every three digits

# progress = 0.635
# print(f"The progress is {progress:.1%}") #Converts to percentage

# name = "John"
# print(f"{name:>10}") #Right align
# print(f"{name:^10}") #Centre align
# print(f"{name:<10}") #Left align

# product = "Laptop"
# price = 1799.872
# print(f"{product:>15} | €{price:.2f}")

name = input("Enter your name:\n")
age = int(input("Enter your age:\n"))
height = float(input("Enter your height in meters:\n"))
weight = float(input("Enter your weight in kilograms:\n"))

bmi = weight / (height ** 2)
name = name.capitalize()
length = len(name)

print(f"Hi {name}, your name has {length} characters. \nYour bmi index is:{bmi:.2f}")