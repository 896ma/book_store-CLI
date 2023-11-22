
# Building a  command Line Application in python (bbok store application)

def  main():
    
    booklist =[]  #initalizing thebooklist
    choice =0
    while choice!=4:
        print("Greetings Developer")
        print(" ***Welcome to the Book  Manager :)")
        print("1)Add a book")
        print("2)Look up a book")
        print("3)Display  books")
        print("4) Quit")
        choice =int(input())
        
        if choice == 1:
            print("Adding a book...")
            nbook = input("Enter the name of the book >>")
            nAuthor= input("Enter the Author of the Book>>")
            nPages = input("Enter the Number of pages in the book >>")
            
            booklist.append([nbook,nAuthor,nPages])
        
        elif choice ==2:
            print("Looking up for a book ...")
            keyword=input("Enter search Term to look for your book :")
            
            for book in booklist:
                if keyword in book:
                    print(book)
        elif choice==3:
            print("Displaying all  your books ...")
            for i in range(len(booklist)):
            
              print(booklist[i])
              
        else:
            
            print("Leaving Bookstore...")
            quit()
            
print("Program terminated..")
            
            
            
    


if   __name__ == "__main__":
    main() 
    
