categories = {"Car": [], "House": [], "Groceries": [], "Pets": [], "Bills": []}
def calculate_budget(income, expenses):
    total_income = sum(income)
    total_expenses = sum(expenses)
    budget = total_income - total_expenses
    return budget

def main():
    income = []
    expenses = []

    # Get user input for income
    income_count = int(input("Enter the number of income sources: "))
    for i in range(income_count):
        income_amount = float(input("Enter income amount: "))
        income.append(income_amount)

    # Get user input for expenses
    expenses_count = int(input("Enter the number of expenses: "))
    for i in range(expenses_count):
        expense_amount = float(input("Enter expense amount: "))
        expenses.append(expense_amount)

    # Calculate the budget
    budget = calculate_budget(income, expenses)

    # Display the budget
    if budget > 0:
        print("Your budget is positive. You have a surplus of $", budget)
    elif budget < 0:
        print("Your budget is negative. You have a deficit of $", abs(budget))
    else:
        print("Your budget is balanced.")

# Run the budget program
if __name__ == "__main__":
    main()
