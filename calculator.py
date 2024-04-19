print("Welcome to our Calculator")

X = float(input("Enter the first number: "))
Y = float(input("Enter the second number: "))
Sign = input("Select - or +: ")

if Sign == "+":
    Sum = X + Y
else:
    Sum = X - Y

print("Result:", Sum)