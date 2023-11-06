# Ask user for gross income (per year). Remember to convert the value to float.
# If the income is below 10000, the user is exempt from tax hence the program should print the same value as it recieved
# The country has tax brackets as follows:
# a. income between 10000 and 30000 is taxed at 20%
# b. income at 30000 to 50000 is taxed at 35%
# c. income over 50000 is taxed at 45%
# Calculate the user's after-tax income using if/elif/else statements.

def after_tax_calc():
    gross_income = float(input("How much do you make per year? "))
    if gross_income <= 10000:
        print("Your gross income is less than $10,000, therefore you are exempt from paying taxes.")
    elif 10000 < gross_income <= 30000:
        print("You are eligible for Bracket 1 (20% tax rate)")
        after_tax_income = gross_income*.20
        print(f"Your income after taxes is: ${after_tax_income}")
    elif 30000 < gross_income <= 50000:
        print("You are eligible for Bracket 2 (35% tax rate)")
        after_tax_income = gross_income*.35
        print(f"Your income after taxes is: ${after_tax_income}")
    elif gross_income > 50000:
        print("You are eligible for Bracket 3 (45% tax rate)")
        after_tax_income = gross_income*.45
        print(f"Your income after taxes is: ${after_tax_income}")
    else:
        print("Please enter a positive number")

after_tax_calc()