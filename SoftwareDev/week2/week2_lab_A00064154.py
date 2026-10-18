#STUDENT ID - A00064154
#STUDENT NAME - Szymon Podraza-Ostrega

#Exercise 1
#Assignment didn't ask for user input
var1, var2, var3 = 5, 6, 7
avg = (var1 + var2 + var3) / 3
print(f"The average of 5, 6 and 7 is {avg}!")

print("The value of var1 is", var1, "the value of var2 is", var2, "and the value of var3 is", var3)
print("The value of var1 is " + str(var1) + " the value of var2 is " + str(var2) + " and the value of var3 is " + str(var3))
print("The value of var1 is {0} the value of var2 is {1} and the value of var3 is {2}".format(var1, var2, var3))
print("\n")

#Exercise 2
#Assignment didn't ask for user input
WEIGHT = 112
calories_needed = WEIGHT * 19

print("This person needs to eat", calories_needed, "calories as they are", WEIGHT, "lbs.")
print("This person needs to eat " + str(calories_needed) + " calories as they are " + str(WEIGHT) + " lbs.")
print("This person needs to eat {0} calories as they are {1} lbs.".format(calories_needed, WEIGHT))
print("\n")

#Exercise 3
#Assignment didn't ask for user input
age_earth = 18
age_mercury = (age_earth * 365) / 88
age_venus = (age_earth * 365) / 225
age_jupiter = (age_earth * 365) / 4380
age_saturn = (age_earth * 365) / 10767

print("A person who is 18 on Earth would be", age_mercury, "on Mercury.")
print("A person who is 18 on Earth would be " + str(age_venus) + " on Venus.")
print("A person who is 18 on Earth would be {0} on Jupiter.".format(age_jupiter))
print(f"A person who is 18 on Earth woould be {age_saturn} on Saturn.")