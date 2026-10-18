TAX = 25
TAX_BRACKET = 100

hours = int(input("Enter how many hours you worked:\n"))
rate = float(input("Enter the rate at which you work at:\n"))
gross = hours * rate

if gross >= TAX_BRACKET:
    net = gross - TAX
    print(f"Your gross pay is €{gross:.2f} and your net pay is €{net:.2f}")
else:
    print(f"Your gross pay is the same as net pay, which is €{gross:.2f}")

gpa=float(input("Enter your Grade Point Average, i.e. gpa:\n"))
num_fails = 0
num_passes = 0
num_merits = 0
if gpa < 2.0:
 print("You have failed - try again")
 num_fails += 1
elif gpa < 2.5:
 print("You received a Pass")
 num_passes += 1
else:
 print("Well done - you received a Merit")
 num_merits += 1
print(f"{'Fails:':<10}{num_fails}")
print(f"{'Passes:':<10}{num_passes}")
print(f"{'Merits:':<10}{num_merits}")

num = int(input("Enter a number:\n"))
if num % 2 == 0:
  print("The number is even!")
else:
  print("The number is odd!")

email = input("Enter your email:\n")
if "@" in email:
  print("'@' character is present")
else:
  print("'@' character is not present")