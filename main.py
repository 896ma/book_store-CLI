
def main():
    try:
        booklist = []  # Initializing the booklist

        infile = open("Booklists.txt", "r")
        line = infile.readline()

        while line:
            booklist.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()  # Closing the infile

    except FileNotFoundError:
        print("An unexpected error occurred and your <Booklists.txt> file is not found.")
        print("Starting a new bookslist")
        booklist = []

    choice = 0
    while  choice!=4:
        print("Greetings Developer")
        print(" ***Welcome to the Book Manager :)")
        print("1) Add a book")
        print("2) Look up a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book...")
            nbook = input("Enter the name of the book >>")
            nAuthor = input("Enter the Author of the Book >>")
            nPages = input("Enter the Number of pages in the book >>")

            booklist.append([nbook, nAuthor, nPages])

        elif choice == 2:
            print("Looking up for a book ...")
            keyword = input("Enter search Term to look for your book:")
            for book in booklist:
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("Displaying all your books ...")
            for i in range(len(booklist)):
                print(booklist[i])

        else:
            print("Leaving Bookstore...")
            quit()

    print("Program terminated..")

    # Saving the books listed to an external TXT File
    outfile = open("Booklists.txt", "w")
    for book in booklist:
        outfile.write(",".join(book) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()
