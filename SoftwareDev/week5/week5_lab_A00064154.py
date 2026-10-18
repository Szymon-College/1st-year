#STUDENT NAME: Szymon Podraza-Ostrega
#STUDENT ID: A00064154

#Exercise 1
message = "Welcome to the Payroll System"
print(f"{message:>40}")
id = int(input("Enter your ID:\n"))
name = input("Enter your name:\n")
address = input("Enter your address:\n")
marital = input("Enter your marital status - s for single, m for married:\n")
gross = int(input("Enter your gross pay:\n"))
allowance = 0
tax = 0
if gross < 50000:
    allowance = 25000
else:
    allowance = 20000
if marital == 's':
    tax = .2
elif marital == 'm':
    tax = .23
else:
    tax = 0

pre_net = gross - allowance
total_tax = tax * pre_net
net = pre_net - total_tax + allowance

message2 = "Payroll Details for employee"
print(f"{message2:>40}\t{id}")
print(f"{'Id:':<30}\t{id}")
print(f"{'Name:':<30}\t{name}")
print(f"{'Address:':<30}\t{address}")
print(f"{'Marital status:':<30}\t{marital}")
print(f"For a gross pay of €{gross:.2f}, your total tax is {total_tax:.2f} and your net pay is €{net:.2f}")

message3 = "Secuity Feature"
print(f"{message3:>40}")
passowrd = input("Enter your password:\n")
password_check = input("Re-enter your password:\n")
if passowrd == password_check:
    print("Proceed")
else:
    print("Wrong")

#Exercise 2
WAGE = 12.25
hours = int(input("Enter how many hours you worked today:\n"))
sales = int(input("Enter your sales:\n"))
num_commissions = 0
pay = 0

if hours <= 38:
    pay = WAGE * hours
else:
    pay = WAGE * 38
    extra_hours = hours - 38
    overtime = (WAGE * 1.5) * extra_hours
    pay = pay + overtime

if sales >= 50:
    commissions = sales * 0.05
    pay = pay + commissions
    num_commissions += 1

print(f"{'Total hours:':<20}\t{hours}")
print(f"{'Total sales:':<20}\t€{sales}")
print(f"{'Pay':<20}\t€{pay:.2f}")
print(f"{'Number of commissions:':<20}\t{num_commissions}")
