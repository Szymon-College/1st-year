#Exercise 1
surname = "Podraza-Ostrega"
check = input("Enter my surname:\n")

if check == surname:
    print("You got my name correct")
else:
    print("Fail")

#Exercise 2
grade = int(input("Enter your grade:\n"))
if grade <= 34:
    print("F")
elif grade >= 35 and grade <= 39:
    print("D")
elif grade >= 40 and grade <= 44:
    print("C3")
elif grade >= 45 and grade <= 49:
    print("C2")
elif grade >= 50 and grade <= 54:
    print("C1")
elif grade >= 55 and grade <= 59:
    print("B3")
elif grade >= 60 and grade <= 64:
    print("B2")
elif grade >= 65 and grade <= 69:
    print("B1")
elif grade >= 70 and grade <= 74:
    print("A3")
elif grade >= 75 and grade <= 79:
    print("A2")
elif grade >= 80 and grade <= 100:
    print("A1")

#Exercise 3
oak = 225
pine = 100
mahogany = 310

wood_choice = int(input("Enter (1) for oak, (2) for pine and (3) for mahogany\n"))
if wood_choice == 1:
    quantity = int(input("How many do you wish to buy?\n"))
    print(f"Your order is {quantity} oak tables for a total of €{oak * quantity:.2f}")
elif wood_choice == 2:
    quantity = int(input("How many do you wish to buy?\n"))
    print(f"Your order is {quantity} pine tables for a total of €{pine * quantity:.2f}")
elif wood_choice == 3:
    quantity = int(input("How many do you wish to buy?\n"))
    print(f"Your order is {quantity} mahogany tables for a total of €{mahogany * quantity:.2f}")
else:
    print("ERROR! INVALID INPUT!")
