print ("Welcome To ISoft Book Store\n")
print ("1. View Books")
print ("2. Add Book")
print ("3. Delete Book")
print ("0. Exit\n")

action = -1
while action != 0:
    try:
        action = int(input("Enter a number to perform an action: "))
    except NameError:
        pass

    if action == 1:
        print ("You chose to view books!\n")  # method to view books goes here
    elif action == 2:
        print ("You chose to add a book!\n")  # method to add books goes here
    elif action == 3:
        print ("You chose to delete a book!\n")  # method to delete books goes here
    elif action == 0:
        print ("Buzz off!\n")
    else:
        print ("You entered a wrong input!\n")


