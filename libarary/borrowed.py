
import date_time as dt
Bname = []
Aname = []
Stocks = []
price = []

with open ("Book.txt", "r") as files:
    for i in files:
        i= i.split(",")
        Bname.append(i[0])
        Aname.append(i[1])
        Stocks.append(int(i[2]))
        price.append(float(i[3].strip("NRs\n")))
    
def Borrow():
    def showBooks():
        print("\n")
        for i in range(len(Bname)):
            print("-", i,". " , Bname[i], "\n")

    while True:
        name = input(" \n Enter your name: ")
        if name.isalpha() == True:
            break
        else:
            print("\n Please enter alphabets only!") 
            
    fname = name + "borrow.txt"
    fileBookBorrowed = name + "Borrowed.txt"
    with open(fname, "w+") as f:
        f.write("\n\n---- Library Management \n\n")
        f.write("-----Borrowed by: " + name +"\n\n")
        f.write("---- Borrowed Date: " + str(dt.currentDateTime()) + "\n\n\n")
        f.write("S.N\t\t\tBookName\t\t\tAuthorName \n\n")

    showBooks()
    count = 1
    taken_books = []
    number = []
    Borrowedbook = []
    while True:
        try:
            B_index = int(input('Enter the books index that you want to borrow :'))
            
        except ValueError:
            print('\n invalid literal.please try again.\n')
            showBooks()
            continue
        
        if B_index < 0 or B_index >= len(Bname):
            print(" \nBook Index out of range")
            showBooks()
            continue
        
        if Bname[B_index] in taken_books:
            print(' \n Borrowing the same book is invalid \n')
            continue
        else:
            pass

        taken_books.append(Bname[B_index])
        Borrowedbook.append(Bname[B_index])

        if Stocks[B_index] > 0:
            print(' \nThis book is available \n')
            with open (fname, "a") as f:
                f.write(str(count) + "\t\t\t" + Bname[B_index] + "\t\t\t" +  Aname[B_index] + "\n")
                count += 1

            Stocks[B_index] = Stocks[B_index] - 1

            with open('book.txt' , 'w+') as f:
                for x in range(len(Bname)):
                    f.write(Bname[x]+','+ Aname[x]+','+ str(Stocks[x])+','+'NRs'+ str(price[x]) + "\n")
        else:
            print('This book is unavailable!')
            print("Thankyou for coming to our library")
            break
        if set(taken_books) == set(Bname):
            print( '\n Work done.' )
            print(' \nBooks that are available to borrow.\n')
            break

            

        while True:
            print(" Do you still want to borrow Yes or No. Cannot borrow the borrowed book: ")
            choice = input(" \n Enter your choice: ")
            if choice.isalpha() == True:
                break
            else:
                print('\n Invalid')
                continue

        if choice.lower() == 'y' or choice.lower() == "yes":
            showBooks()
            continue 
        
        else:
            with open(fname,"r") as f:
                r=f.read()
                print(r)
            print("\nThankyou for coming to our library:")
            break
    with open(fileBookBorrowed, "w") as f:
        f.write(str(Borrowedbook))

        
        


