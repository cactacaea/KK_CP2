# KK 2nd, Personal Library Program

#import sys
import sys
import time

# main list for all books which will store dictionaries
all_books = []
# main menu options tuple
menu = ("View","Add","Remove","Search","Quit")

# main function
def main(menu, all_books):
# while loop for input validation
 while True:
    # input for user action (view,add,remove,search,exit), for loop to display options
    print("\n--- Valid Choices ---")
    for object in menu:
        print(object)
    action = input("\nPlease enter the word for your option:\n").lower()
    # if user chooses to view added books, call function
    if action == "view":
       viewBooks(all_books)
    # else if user chooses to add a book, call function
    elif action == "add":
        addBooks(all_books)
    # else if user chooses to remove a book, call function
    elif action == "remove":
        removeBooks(all_books)
    # else if user chooses to search a book, call function
    elif action == "search":
        searchBooks(all_books)
    # else if user chooses to quit
    elif action == "quit":
        # break loop/stop entire system
        sys.exit()
        break
    # else
    else:
        # ask for a valid answer 
        print("\nInvalid choice. Try again\n")
        time.sleep(2)

# view func; parameters - all books variable
def viewBooks(all_books):
    print("\nThese are your current made books!:\n")
    # for each item/book in all_books
    for book in all_books:
        # display "book" by "author"
        title, author = book["book"]
        print(f"{title} by {author}")
    time.sleep(2)

# add func; parameters - all books variable
def addBooks(all_books):
    # title/author inputs from user
    title = input("\nWhat is the book's title?:\n").strip()
    author = input("Who's the author of this book?:\n").strip()
    # make new book dictionary and add new item to all_books, store info as a tuple(?)
    book_info = (title,author)
    new_book = {
        "book": book_info
    }
    all_books.append(new_book)
    print(f"\nYou added: {title} by {author}\n")
    time.sleep(2)

# remove func; parameters - all books variable
def removeBooks(all_books):
    index = 1
    for book in all_books:
        # UNPACK TUPLE
        title, author = book["book"]
        print(f"{index}. {title} by {author}")
        index += 1
    # user input for book search
    choice = int(input("\nEnter the number // What book would you like to remove?:\n"))
    # for each item/book in the books list, print the book if the input text is in it
    # remove the index of the book +1 because the index subtracts
    removed_book = all_books.pop(choice - 1)
    title, author = removed_book["book"]
    print(f"\nYou removed: {title} by {author}\n")


# search func; parameters - all books variable
def searchBooks(all_books):
    search_method = input("\nHow would you like to search for your book? Enter the number.\n1. Title\n2. Author\n?: ")
    search = input("\nEnter your book search: ")
    found_book = False

    for book in all_books:
        title, author = book["book"]

        if search_method == "1" and search in title.lower():
            print(f"{title} by {author}")
            found_book = True

        elif search_method == "2" and search in author.lower():
            print(f"{title} by {author}")
            found_book = True

    if found_book == False:
        print("There are no books containing this text..")
    
print("Greetings!")
main(menu,all_books)