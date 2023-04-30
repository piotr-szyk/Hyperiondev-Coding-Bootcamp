'''
Data Science
TASK: Capstone Project I - Variables and Control Structures
Compulsory Task 1
Author: Piotr Szyk
Date: 02 Apr 2023
'''


import math

print()
print("Welcome to your investment and bond calculator!")


def which_calculator():
    """
    Function asks (continuously using while True loop) the user to select the
    calculator (investment or bond) with addition of lower() method in order
    to return user selection as a lowercase string (variable 'selection').
    """
    while True:
        selection = input('''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
investment  - to calculate the amount of the interest you'll earn on your investment
bond        - to calculate the amount you'll have to pay on a home loan
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Enter either 'investment' or 'bond' from the menu above to proceed: ''')
        if selection.lower() == "investment" or selection.lower() == "bond":
            return selection.lower()
        else:
            print("Invalid selection. Please enter either 'investment' or 'bond' to proceed: ")


def simple_interest(P, r, t):
    """
    Function calculates the simple interest using provided formula: A = P * (1 + r*t), where
    A - is the total amount once the interest has been applied
    r - is the interest entered divided by 100, e.g. 8% -> 0.08
    P - is the amount that the user deposits
    t - is the number of years that the money is being invested
    """
    # calculate simple interest using formula
    A = P * (1 + r*t)
    return A


def compound_interest(P, r, t):
    """
    Function calculates the compound interest using provided formula: A = P * math.pow((1 + r),t), where
    A - is the total amount once the interest has been applied
    r - is the interest entered divided by 100, e.g. 8% -> 0.08
    P - is the amount that the user deposits
    t - is the number of years that the money is being invested
    """
    # calculate compound interest using formula
    A = P * math.pow((1 + r), t)
    return A


def bond_repayment(P, i, n):
    """
    Function calculates the how much money the user will have to repay each month using provided formula:
    repayment = (i * P)/(1 - (1 + i)**(-n)), where
    P - is the present value of the house
    i - is the monthly interest rate, calculated by dividing the annual interest rate by 12
    n - in the number of months over which the bond will be repaid
    """
    # calculate bond repayment using formula
    repayment = (i * P) / (1 - (1 + i)**(-n))
    return repayment


# calling which_calculator function and assigning the result to calculator_type
calculator_type = which_calculator()
# informing user of the selection
print("You have selected:", calculator_type)
print()
# using if/elif statements to take user selection between investment and bond. If investment is selected,
# continous while true loop is run for the user to select between simple or compound interest. Based on the
# selection, a specific funcion is run and result of calculation displayed for the user.
if calculator_type == "investment":
    # ask user to input the amount they would like to deposit
    principal = float(input("Please enter the amount to deposit: "))
    # ask user to input the interest rate (as a percentage ommiting % sign)
    interest_rate = float(input("Please enter the interest rate: "))
    # converting from percentage to decimal notation
    interest_rate /= 100
    # ask user to input the number of years they plan on investing
    time_in_years = int(input("Enter the number of years you plan investing: "))
    # ask user to input if they want "simple" or "compount" interest and based on selection
    # run appropriate function (simple_interest or compound_interest)

    while True:
        interest = input("Please select your interest. Enter 'simple' or 'compound': ")
        if interest.lower() == "simple":
            print(
                "\n"
                "The total amount accrued has been calculated based on the information provided. Please see below for details:\n"
                "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                f"Deposit:              {principal}\n"
                f"Interest rate:        {interest_rate}\n"
                f"Years invested:       {time_in_years}\n"
                f"Total Amount Accrued: {round(simple_interest(principal,interest_rate,time_in_years),2)}\n"
                "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                )
            break
        elif interest.lower() == "compound":
            print(
                "\n"
                "The total amount accrued has been calculated based on the information provided. Please see below for details:\n"
                "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                f"Deposit:              {principal}\n"
                f"Interest rate:        {interest_rate}\n"
                f"Years invested:       {time_in_years}\n"
                f"Total Amount Accrued: {round(compound_interest(principal,interest_rate,time_in_years),2)}\n"
                "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                )
            break
        else:
            continue
elif calculator_type == "bond":
    # ask user to input present value of the house
    present_value = float(input("Enter the present value of the house: "))
    # ask user to input interest rate
    interest_rate = float(input("Enter the interest rate: "))
    # converting from percentage to decimal notation
    interest_rate /= 100
    # calculate monthly interest rate based on the provided annual rate
    monthly_interest_rate = round(interest_rate / 12, 4)
    # ask user to input number of months to repay the bond
    time_in_months = int(input("Enter the number of months to repay the bond: "))
    print(
        "\n"
        "Please see below for the information provided and the amount of money that you will have to repay each month:\n"
        "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
        f"Present value of the house:              {present_value}\n"
        f"Interest rate:                           {interest_rate}\n"
        f"Monthly interest rate:                   {monthly_interest_rate}\n"
        f"Number of months to repay the bond:      {time_in_months}\n"
        f"You will owe each month: {round(bond_repayment(present_value,monthly_interest_rate,time_in_months),2)}\n"
        "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
        )
