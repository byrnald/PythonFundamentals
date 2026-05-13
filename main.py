# Personal Finance Calculator
try: 
    income = float(input("Enter Income: "))
    rent = float(input("Rent: "))
    food_budget = float(input("Budget: "))
    expenses = input("Expenses: ")

#was not sure onto how we needed to add all of the expenses based off of 
#one input, so i decided to create a list and add them into it
    exp_list = []
    for expense in expenses.split():
#took every string from exp input and split which by default 
#splits from whitespaces (spaces)
        exp_list.append(float(expense))
#then took those split string and added them to the list while
#type casting them into floats

    total_expense = 0
    for expense in exp_list:
        total_expense += expense
    total_expense += rent
    total_expense += food_budget
    print(f"Total Expenses: {total_expense}")
#then i just added all of it up and included rent 
#did not include food yet since it's just a budget not a 
#complete expense, actually i just added it

    remaining_money = income - total_expense
    saving_rate = (remaining_money / income) * 100

    if total_expense > income:
        print(f"Warning! Expenses > Income. \nRemaining: {remaining_money:.2f}")
        
    else:
        print(f"Remaining Money: {remaining_money:.2f}\nSaving Rate: {saving_rate:.2f}%")
        
        print("No Warning!")


except ValueError: 
    print("Invalid Input")