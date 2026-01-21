# KK 2nd, Finance Calculator

import sys
import time

# "again?" function
def again():
    bold = '\033[1m'
    end = '\033[0m'
    while True:
        calc_again = input(f"\n{bold}Yes/No - Would you like to make another calculation?:{end}\n")
        if calc_again == "no":
            print("\nStopping...")
            time.sleep(2)
            sys.exit()
            break
        elif calc_again == "yes":
            main()
        else:
            print("\nError. Try Again.")
        
# main func
def main():
    bold = '\033[1m'
    end = '\033[0m'
    # while LOOP
    while True:
    # input getting user choice for what to calculate (starting menu) // save for a goal, compound interest, budget allocator, sales, tip
        choice = input("\n#1: Savings Time Calculator // Determine how much time it will take to save up to a goal based on monthly/weekly contributions.\n#2: Compound Interest // Determine the amount of money you would have based on an interest rate after an amount of years spent compounding.\n#3: Budget Allocator // Determine how much money your budget categories take up based on percentages\n#4: Sale Price Calculator // Determine a discounted price.\n#5: Tip Calculator // Find how much your total will be with an added tip.\n\nEnter the number to select your option:\n").lower().strip()
    # if input == an available option, call the necessary function
        if choice == "1": # save for a goal
            savingsTime()
        elif choice == "2": # compound interest
            compoundInterest()
        elif choice == "3": # budget allocator
            budgetAllocator()
        elif choice == "4": # sales price discount
            salesPrice()
        elif choice == "5": # tip
            tip()
        else:
            print("\nError. Try Again.")

# save for a goal func
def savingsTime():
    # input what users goal is
    goal = float(input("\nWhat amount of money are you saving to?:\n"))
    # input how often user is contributing (weekly/monthly)
    contribution_rate = input("\nWeekly/Monthly - How often are you contributing?:\n").lower().strip()
    # input how much user is contributing
    contribution_amount = float(input("\nHow much are you contributing each time?:\n"))
    # if weekly contributions:
    if contribution_rate == "weekly":
        # goal divided by contribution #
        weeks = goal/contribution_amount
        # print how many weeks
        print(f"\nIt will take {weeks:.0f} weeks to save ${goal:.2f}")
        # wait a few seconds and ask to calculate again
        time.sleep(4)
        again()
    # if monthly contributions
    elif contribution_rate == "monthly":
        # goal divided by contribution #
        months = goal/contribution_amount
        # print how many weeks
        print(f"\nIt will take {months:.0f} weeks to save ${goal:.2f}")
        # wait a few seconds and ask to calculate again
        time.sleep(4)
        again()

# compound interest calc function
def compoundInterest():
    goal = float(input("\nWhat is your starting amount?:\n")) # GOAL = STARTING /CHANGING AMOUNT AFTER EACH COMPOUND
    interest_rate = float(input("\nWhat is the interest rate percentage?:\n"))/100
    years = int(input("\nHow many years will you spend compounding?:\n"))

    # divide YEARLY INTEREST RATE by 12
    monthly_rate = interest_rate/12
    all_months = years*12
    def oneMonthCompound():
        nonlocal goal
        goal = goal + (goal*monthly_rate)
        return goal
    
    for month in range(all_months):
        oneMonthCompound()
    print(f"\nAfter {years} years compounding, you will have ${goal:.2f}")

    time.sleep(4)
    again()

# budget allocator function
def budgetAllocator():
    # empty categories list
    categories = []
    # user input how many budget categories they have
    # make budget categories into an integer
    category_amount = int(input("\nHow many budget categories do you have?:\n"))
    # for loop in the range of the budget category integer
    for i in range(1, category_amount+1):
        # user inputs what type of budget category it is, each input is appended to categories list
        category = input(f"\nCategory {i} is:\n")
        categories.append(category)

    income = float(input("\nWhat is your monthly income?:\n"))
    percentages = []
    while True:
        for category in categories:
            percent = float(input(f"\nWhat percent does your {category} take up?:\n"))
            percentages.append(percent)
        if sum(percentages) > 100 or sum(percentages) < 100:
            print("\nYour percentages don't add up to a perfect 100! Redo your math")
            percentages.clear()
        else:
            break

    print("\n")

    for i in range(len(categories)):
        amount = income * (percentages[i] / 100)
        print(f"{categories[i]}: ${amount:.2f}")

    time.sleep(4)
    again()

# sales function
def salesPrice():
    # original item cost input
    original_item = float(input("\nHow much does the item originally cost?:\n"))
    # discount percent input
    discount = float(input("\nWhat is the discount percentage?:\n"))
    # calculated discount = original*discount percent/100
    caclulated_discount = original_item*discount/100
    # final price = original item - discount
    final_price = original_item-caclulated_discount
    # print final price
    print(f"\nThe item would cost ${final_price:.2f} after a {discount:.0f}% discount.")
    # wait a few seconds and ask to calculate again
    time.sleep(4)
    again()


# tip calc function
def tip():
    # user input for the inital bill
    bill = float(input("\nHow much is the initial bill?:\n"))
    # user input for tip percent
    tip_percent = float(input("\nWhat percent of a tip would you like to give?:\n"))
    # tip amount = orginal_price*tip/100
    tip_amount = bill*tip_percent/100
    # total = original_price + tip amount
    final_bill = bill + tip_amount
    # display results
    print(f"\nThe tip amount is {tip_amount:.2f}, so your total is {final_bill}")
    # call again? function
    time.sleep(4)
    again()

print("Welcome to your local finance calculator.")
main()