'''
Data Science
TASK: Towards Defensive Programming II - Exception Handling
Compulsory Task 1
Author: Piotr Szyk
Date: 20 Apr 2023
'''

'''
V1.0: This program will ask a user to enter two numbers and the operation (e.g. +, -, x, etc.) 
that they would like to perform on the numbers and display the answer to the equation. Every
equation entered by the user is written to a txt file.
V1.1: Extending the capability of the program to give a user an option to either enter two 
numbers and the operation or to read all of the equations from a new txt file (user adds the name
of the txt file as an input). All of the equations are printed out
'''


def addition():
    """Calculate the sum of num1 and num2"""
    return num1 + num2


def subtraction():
    """Calculate the difference of num1 and num2"""
    return num1 - num2


def multiplication():
    """Calculate the product of num1 and num2"""
    return num1 * num2


def division():
    """Calculate the quotient of num1 and num2"""
    return num1 / num2


def save_equation():
    """Saving all the equations to file equations.txt
    Using append mode to create a file if does not 
    exists yet or append the data to the existing file
    """
    with open("equations.txt", "a") as file:
        file.write(f"{num1} {operator} {num2} = {result} \n") 


def read_equations():
    """This function will keep asking a user to provide a file name
    until the correct file name of equations.txt is obtained. If 
    wrong name is provided an error is thrown. If correct filename
    is provided, the function will print all the file contents."""
    while True:
        filename = input("Please enter the name of the file to read: ")
        try:
            with open(filename, "r") as file:
                contents = file.read()
                print("Here are your equations so far:")
                print()
                print(contents)
            break   # will exit the loop once the file successfully read
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please try again. Hint: filename is equations.txt")


# Putting the functions into dictionary
functions = {'+': addition,
             '-': subtraction,
             '*': multiplication,
             '/': division}

# The while true loop keeps asking user for input until valid inputs are provided.
# Added try/except to catch an invalid inputs. I have included additional raise 
# statements in case of incorrect operator or division by 0.

# Extending the program to give a user three options:
# 1. Perform calculation based on two numbers and the operator
# 2. Read equations from the file
# 3. Quit the program

# print welcome message
print("""
    Welcome to the calculator! 
    
    What would you like to do?""")

while True:
    option = input("""

    Please enter:
    '1' to perform calculation, 
    '2' to read from a file,
    'q' to quit: """)
    if option == "1":
        print("You have selected option 1.")
        while True:
            try:
                num1 = float(input("Please enter first number: "))
                num2 = float(input("Please enter second number: "))
                operator = input("""Please enter an operator:
                    + for addition, 
                    - for subtraction, 
                    * for multiplication, 
                    / for division
                    : """)
                if operator not in ["+", "-", "*", "/"]:
                    raise ValueError("Invalid operator!")
                elif operator == "/" and num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero!")
                break
            except ValueError as error:
                print(f"Invalid input: {error}")
            except ZeroDivisionError as error:
                print(f"Invalid input: {error}")
        # Using get() method for function selection to execute from the dictionary
        selection = functions.get(operator)
        result = selection()
        print(f"{num1} {operator} {num2} = {result}")
        # save equation to file
        save_equation()
    elif option == "2":
        print("You have selected option 2.")
        read_equations()
    elif option == "q":
        print("Thank you for using the calculator. Bye!")
        break
    else:
        print("wrong input! Please select 1, 2, or q")
    
