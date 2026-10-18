#1.
a, b, c = 11, 55, 2

a = a + b - c
print(a)
c = c % 3
print(c)

a = 11
c = (a + 22) % 2

print(c)

#2.
print(4 + 6 * 3)
print(16 % 2)
print(6 / 3 * 7)
print(17 % 2)
print(18 / 2 + 14 / 2)
print(28 % 5)
print(16 / 2)
print(28 % 5 * 3 + 1)
print(17/2)
print((2 + 3) * 4)
print(28 // 5)
print(20 / (4 + 1))

#3.
d, e, f = 23, 3, 1

d += e
print(d)
f *= f
print(f)
e %= 3
print(e)

#4.
age = int(input("Enter your age in years:\n"))
seconds = age * 365 * 24 * 3600
print(f"Your age in seconds is: {seconds}")

#5.
BOOK_PRICE = 24.95
DISCOUNT = 0.6
SHIPPING = 2

copies = int(input("Enter the amount copies needed:\n"))

print("\tBook Shop System")
print(f"\tCost of books: €{(BOOK_PRICE * copies) * DISCOUNT}")
print(f"\tCost of shipping: €{SHIPPING * copies}")
print(f"\tOverall cost: €{((BOOK_PRICE * copies) * DISCOUNT) + (SHIPPING * copies)}")