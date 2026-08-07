# Library Management(OR Library Menu)

books = {"Maths","Physics","Chemistry","CS"}
print(f"\nLibrary Books: {books}\n")

print("\n--Library Management(Menu)--\n1 Add Book\n2 Remove Book\n3 Show Books\n4 Remove Random Book\n5 Clear Library\n6 Exit")

def library():
    select = int(input("Choose any one no. : "))
    match select:
      case 1:
        n = input("Enter the book you want to add: ")
        books.add(n)
        print(f"Books after adding: {books}\n")
      case 2:
        m = input("Enter the book you want to remove: ")
        books.remove(m)
        print(f"Books after removing: {books}\n")
      case 3:
        print(f"Showing books: {books}\n")
      case 4:
        item = books.pop()
        print(f"Books after Removing Random Books: {books}")
        print(f"Removed book: {item}\n")
      case 5:
        books.clear()
        print(f"Clearing all books from library(books set): {books}\n")
      case 6:
        print("Thank-You\n")
    library()

library()
    

