#Exercise 1
string1 = "Python"
print(string1[1:])
print(string1[0:3])
print(string1[:4])
print(string1[:-1])
print(string1[-4:-2])

#Exercise 2
user_word = input("Enter a word:\n")
print(user_word[:3]) #First three letters
print(user_word[-3:]) #Last three letters
print(user_word[::-1]) #Reverses string
print(user_word[::2]) #String in steps of two

#Exercise 3
user_word2 = input("Enter a sentence:\n")
start_pos = int(input("Enter the start position:\n"))
end_pos = int(input("Enter the end position:\n"))
step_value = int(input("Enter the step count:\n"))

print(f"The sliced string is {user_word2[start_pos:end_pos:step_value]}")
print(user_word2[::-1])
print(f"The length of your inputted text is {len(user_word2)}")
print(user_word2.upper())

#Exercise 4
user_sentence = input("Enter a sentence:\n")
selected_word = input("Enter a word to look for in the sentence:\n")
status = selected_word in user_sentence
print("Does the word exist?", status)
word_pos = user_sentence.index(selected_word)
print("The word appears at index:",word_pos)
user_sentence = user_sentence.replace(selected_word,"***")

#Exercise 5
print(f"€{456.8787:.2f}") #Rounding to two figures
print(f"€{456654777:,}") #Comma evrey three numbers
print(f"{0.768:.1%}") #Adds percentage with one figure
age = 23
print(f"Your current age is {age}, next year you will be {age + 1}!")