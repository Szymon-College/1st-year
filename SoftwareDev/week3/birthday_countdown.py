# print("\t\tBIRTHDAY COUNTDOWN")

# name = input("Enter your name:\n")
# age = int(input("Enter your current age:\n"))
# years = int(input("How many years ahead?\n"))

# print("Hello", name)
# print(f"In {years}, you would be {age + years}!")
# print(f"{years} years is {years * 12} months!")

print("\t\tTRIP COST CALCLATOR")

destination = input("Enter your destination:\n")
distance = float(input("Enter the distance to your destination:\n"))
fuel_per_cons = float(input("Enter the cars fuel consumption:\n"))
fuel_per_litre = float(input("Enter the price of fuel:\n"))
fuel_used = distance * fuel_per_cons / 100

print(f"Trip to {destination}")
print(f"Estimated litres used: {fuel_used}")
