print("welcome to our calculator")
 
x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))
 
sign = input("Enter + or - : ")
 
if sign == "+":
    result = x + y
    print("Sum =", result)
elif sign == "-":
    result = x - y
    print("Sum =", result)