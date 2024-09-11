class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def listBooks(self):
        print("Books present in this Library are : ")
        for book in self.books:
            print(f" * {book}")

    def requestBook(self, book):
        if(book in self.books):
            print(f"You have been issued the book {book}. Please keep it safe and return within 15 days.")
            self.books.remove(book)
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available.")

    def returnbook(self, book):
        if(book in self.books):
            print("You already returned this book or you have not issued this book yet.")
        else:
            print(f"Thanks for returning this book {book}. Hope you enjoyed reading it. Have a great day ahead!")
            self.books.append(book)

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow : ")
        return self.book
    
    def returnbook(self):
        self.book = input("Enter the name of the book you want to return : ")
        return self.book

lib = Library(["C", "C++", "HTML", "CSS", "JavaScript", "Java", "OOPs", "Python"])
stu = Student()

print("===== Welcome to the Central Library =====")
msg = """\nPlease choose an option : 
    1. List all the books
    2. Request a book
    3. Return a book
    4. Exit the Library\n"""

print(msg)
n = int(input("Enter a choice : "))

while True:
    if(n==1):
        lib.listBooks()
    elif(n==2):
        lib.requestBook(stu.requestBook())
    elif(n==3):
        lib.returnbook(stu.returnbook())
    elif(n==4):
        print("Thanks for choosing the Central Library. Have a great day ahead!")
        break
    else:
        print("Invalid choice!")

    print(msg)
    n = int(input("Enter your choice again : "))

input()