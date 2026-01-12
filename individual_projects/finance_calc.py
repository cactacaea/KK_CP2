# KK 2nd, Finance Caclulator // Practice

import sys
import time

# "again?" function
def again():
    bold = '\033[1m'
    end = '\033[0m'
    while True:
        calc_again = input(f"\n{bold}Yes/No - Would you like to make another calculation?:{end}\n")
        if calc_again == "no":
            print("/nStopping...")
            time.sleep(2)
            sys.exit()
            break
        elif calc_again == "yes":
            print(" ")
            main()
        else:
            print("\nError. // Try Again.")
        
# main func
def main():
    bold = '\033[1m'
    end = '\033[0m'
    # while LOOP
    while True:
    # input getting user choice for what to calculate (starting menu) // save for a goal, compound interest, budget allocator, sales, tip
        choice = input("\n#1: Savings Time Calculator // Determine how much time it will take to save up to a goal based on monthly/weekly contributions.\n#2: Compound Interest // Determine the amount of money you would have based on an interest rate after an amount of years spent compounding.\n#3: Budget Allocator // \n#4: Sale Price Calculator // Determine a discounted price.\n#5: Tip Calculator // Find how much your total will be with an added tip.\n\nEnter the number to select your options:\n").lower().strip()
    # if input == an available option, call the necessary function
        if choice == "1": # save for a goal

        elif choice == "2": # compound interest
        elif choice == "3": # budget allocator
        elif choice == "4": # sales price discount
        elif choice == "5": # tip
        else:
            print("\nError. // Try Again.")

# save for a goal func
def savingsTime():
    # input what users goal is
    goal = input("\nWhat amount of money are you saving to?:\n")
    # input how often user is contributing (weekly/monthly)
    contribution_rate = input("\nWeekly/Monthly - How often are you contributing?:\n").lower().strip()
    # input how much user is contributing
    contribution_amount = input("\nHow much are you contributing each time?:\n")
    # if weekly contributions:
    if contribution_rate == "weekly":
        # goal divided by contribution #
            # print how many weeks
            # wait a few seconds and ask to calculate again
    # if monthly contributions
    if contribution_rate == "monthly":
        # goal divided by contribution #
            # print how many weeks
            # wait a few seconds and ask to calculate again

# compound interest calc function

# budget allocator function
def budgetAllocator():
    # empty categories list
    categories = []
    # user input how many budget categories they have
    # make budget categories into an integer
    # for loop in the range of the budget category integer
        # input what type of budget category it is

# sales function
def salesPrice():
    # original item cost input
    # discount percent input
    # calculated discount = original*discount percent/100
    # final price = original item - discount
    # print final price
    # wait a few seconds and ask to calculate again


# tip calc function
def tip():
    # user input for the inital bill
    # user input for tip percent
    # tip amount = orginal_price*tip/100
    # total = original_price + tip amount
    # display results
    # call again? function