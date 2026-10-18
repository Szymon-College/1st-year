my_string = "Monty Python"

print(my_string[0])

print(len(my_string) - 1)

print(my_string[::2])

my_name = "joe Bloggs"
print(my_name)
my_name = my_name.replace("j","Fl")
print(f"My name is {my_name}")

print("" in my_name)
print("z" in my_name)

space_location = my_name.index(" ")
print(f"The space is in position: {space_location}")

full_name = input("Please enter your full name:\n")
space = full_name.index(" ")
f_name = full_name[:space]
l_name = full_name[space + 1:]
print(f_name.capitalize())
print(l_name.capitalize())

test = "Dragon"
if "Dragon" is test:
    print("True")
else:
    print("False")