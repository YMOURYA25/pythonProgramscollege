p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest ): "))
t = float(input("Enter the time : "))

i = (p * t * r) / 100
print(f"The simple interest is: {i}")
print(f"The total amount is: {p + i}")
