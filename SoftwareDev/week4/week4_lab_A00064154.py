#STUDENT NAME: Szymon Podraza-Ostrega
#STUDENT ID: A00064154

#Exercise 1
word1 = input("Enter the first word:\n")
word2 = input("Enter the second word:\n")
word3 = input("Enter the third word:\n")
acronym = word1[0] + word2[0] + word3[0]
print(acronym)

#Exercise 2
password = input("Enter a password:\n")
print(f"The length of the password is {len(password)}")
status = "!" in password
print(f"The status of ! in your password is: {status}")

#Exercise 3
user_word = input("Enter a word:\n")
print(user_word)
print(f"{user_word[:2] + user_word[-2:]}")

#Exercise 4
user_sentence = input("Enter a sentence:\n")
chosen_let = input("Enter a letter to look for:\n")
status2 = chosen_let in user_sentence
print("Does the word exist?", status2)
word_pos = user_sentence.index(chosen_let)
print("The word appears at index:",word_pos)
user_sentence = user_sentence.replace(chosen_let,"#")
print(user_sentence)

#Exercise 5
user_sentence2 = input("Enter a sentence:\n")
start_pos = int(input("Enter the start position:\n"))
end_pos = int(input("Enter the end position:\n"))
step_value = int(input("Enter the step count:\n"))

print(f"The sliced string is {user_sentence2[start_pos:end_pos:step_value]}")
print(user_sentence2[::-1])
print(f"The length of your inputted text is {len(user_sentence2)}")
print(user_sentence2.upper())

#Exercise 6
num = int(input("Enter a number:\n"))
print(f"The squared number of your number {num**2} and the cubed is {num**3}")

#Exercise 7
temp = int(input("Enter the temperature in celcius:\n"))
f_temp = temp * 1.8 + 32
print(f"The temperature in celcius is {temp} and the temperature in fahrenheit is {f_temp:.1f}")