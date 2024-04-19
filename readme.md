## draw.py
## This Python script draws a simple face using the Turtle module.
It creates a turtle object and draws a circle for the face.
Then, it positions and draws dots for the eyes.
Lastly, it draws a curved line to represent a smiling mouth.
To keep the window open and display the drawing, it uses turtle.done().


## grade.py 
## This Python script compares two variables, a and b, and prints a message if a is larger than b.
It then prompts the user to input their grade.
Based on the grade input, it determines and prints the corresponding letter grade.
If the grade is greater than 80, it prints "A".
If the grade is between 70 and 80 (inclusive), it prints "B".
The script lacks a message for grades below 70.
It uses an f-string to format the output message for the comparison of a and b.
It uses int(input()) to convert the input grade to an integer.
The if statement is followed by an elif statement to check for the condition grade >= 70.
A more comprehensive README would clarify what happens if the grade is less than 70 and include information on how to run the script.

## text.y
## This Python script demonstrates string concatenation using the + operator.
It prompts the user to input their name and concatenates it with the string "Good afternoon, ".
It utilizes f-strings for string interpolation, like in the line print(f"welcome to {website}").
The script showcases the usage of the join() method to concatenate strings from a list.
It shows string manipulation methods such as upper() and lower() to change the case of the string.
The script utilizes string formatting using the format() method and f-strings.
It calculates the total price of items in the basket and formats the output accordingly.


## variable.py
## This Python script demonstrates basic variable usage and data types.
It prints a prompt asking for the user's name.
It then prints the string "tanu".
The script declares integer variables first_num and second_num, and a string variable last__name.
It prints the values of first_num and second_num, along with their data types.
It declares a floating-point variable distance, prints its value, and its data type.
The script reassigns first_num as a complex number and prints its value and type.
It demonstrates a boolean variable True, printing its type.
Lastly, it assigns values to variables a and b, and prints them.

## calculator.py
## This Python script implements a simple calculator that performs addition or subtraction based on user input.
It greets the user with a welcome message.
It prompts the user to input the first number (X) and the second number (Y), converting them to floating-point numbers.
It prompts the user to select either addition or subtraction by entering "+" or "-".
Based on the user's choice, the script either adds or subtracts the numbers.
It calculates the result and stores it in the variable Sum.
It prints the result using the print() function.
The script handles both addition and subtraction using an if-else conditional statement.
It utilizes the input() function to receive user input and the float() function to convert input to floating-point numbers.
It follows best practices by providing clear prompts and messages to the user.
The README could include information on how to run the script and what operations are supported.
It demonstrates basic arithmetic operations and conditional statements in Python.