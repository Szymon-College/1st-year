#Exercise 1
age1 = int(input("Enter the age of person 1:\n"))
age2 = int(input("Enter the age of person 2:\n"))

print(f"The age of person 1 is {age1}.")
print(f"The age of person 2 is {age2}.")
print(f"The average age of the two people are {(age1 + age2) / 2}")

#Exercise 2
feet = int(input(f"Enter how tall you are in feet:\n"))
inches = int(input(f"Enter how tall you are in inches:\n"))

while inches >= 12:
    inches -= 12
    feet += 1

print(f"You are {feet} feet and {inches} inches tall.")
print(f"In inches, you are {inches + (feet * 12)}.")

#Exercise 3
print("Waterfall approach is a structured approach in programming where a team works on one aspect of a product without variation, they typically have a set idea on how the product will look.\nAgile approach is where the team works on the entire product and have weekly meetings to adapt the product with the end users.")

#Exercise 4
print("Python is a low-level programming language which is incredibly beginner friendly with almost human like speech for syntax whilst being incredibly versatile and powerful.")

#Exercise 5
my_list = ["Youtube", "Amazon", "Microsoft"]
print(f"Three companies that use Python are {my_list[0]}, {my_list[1]} and {my_list[2]}.")

#Exercise 6
print("The syntax of a language is how the language is structured so that it is coherent. It is essentially the rules of the languages.")

#Exercise 7
print("Pseudocode allows programmers to visualize and break down their thought process before writing algorithms to reduce errors and save time from correcting errors and forgetting to add features.")