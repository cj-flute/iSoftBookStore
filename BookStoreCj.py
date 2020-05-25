import time

# Default author list
authors = [["Mike Pence", "Male"], ["Sandra Slim", "Female"], ["CJ Cool", "Male"]]


class Author():
    """arg: name and gender
     for the author"""

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        print("Name: {0}".format(self.name))
        print("Gender: {0}".format(self.gender))
        pass

    pass


authorList = [Author("Mike Pence", "Male"), Author("Sandra Slim", "Female"), Author("CJ Cool", "Male")]


# view authors function
def viewAuthors():
    print("AUTHORS\n")
    for i in authors:
        print(i[0])
    pass


def view_all_author():
    print("==== All Authors ====")
    print(f"{'|| SN':7}{'|| Name':15}{'|| Gender':15}")
    count = 1
    for author in authorList:
        print(f"{'|| '+str(count):7}{'|| '+author.name:15}{'|| '+author.gender}")
        count += 1
    pass


# function to add authors
def addAuthors():
    authorName = str(input("Input Author name: "))
    authorGender = str(input("Input gender: "))
    # Author(authorName, authorGender)
    # nameGender = [authorName, authorGender]
    # authors.append(nameGender)
    authorList.append(Author(authorName, authorGender))

    # just to check
    for i in authors:
        print(i)
    pass


# function to delete a book
def deleteBook():
    pass


# function to view book
def viewBook():
    pass


# function to add a book
def addBook():
    pass


# function to edit a book
def editBook():
    pass


# function to exit
def exit():
    quit()
    pass


# function for loading
def loading():
    for i in range(3):
        print(".",end=''),
        time.sleep(1)
    pass


while (True):
    loading()
    print("\n\n==== Welcome to ISoft Book Store ====")
    print("1.   View Authors")
    print("2.   Add Authors")
    print("3.   Delete Books")
    print("4.   View Books")
    print("5.   Add Books")
    print("6.   Exit")

    x = int(input("\nInput one option: "))
    if x == 1:
        view_all_author()  # viewAuthors()
    elif x == 2:
        addAuthors()
