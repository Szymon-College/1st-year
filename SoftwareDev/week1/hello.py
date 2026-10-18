print("Hello World", end = " and ")

x = "Hello variable"
print(x)
print(type(x))

if type(x) == str:
    print("This is a string")
else:
    print("This is not a string")

print("This is an example of using escape characters\nPretty\tcool")

print("My favourite movie is \"Die Hard 3\"")

print(5)

a,b = 4,2

print(type(a))

print(a + b) #Add
print(a - b) #Subtract
print(a * b) #Multiply
print(a / b) #Divide
print(a ** b) #Exponential
print(a % b) #Modulus (Shows remainder)
print(a // b) #Floor divide (Shows how many times number can get divided with no remainder)


TAX_RATE = 0.42
gross = int(input("Enter how much money you make:\n"))

profit = gross * TAX_RATE
print(profit)