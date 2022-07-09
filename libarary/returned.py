import date_time as DT
book = []
author = []
Stock= []
bookprice = []
with open ("Book.txt", "r") as files:
    for l in files:
        l = l.split(",")
        book.append(l[0])
        author.append(l[1])
        Stock.append(int(l[2]))
        bookprice.append(float(l[3].strip("NRs\n")))
def Return():
    cost = 0
    payment = 0
    count = 0
    borrower= input("\n\nEnter the name of the borrower: ")
    filereturnName = borrower+ "Return.txt"
    

    with open(filereturnName, "w") as f:
        f.write("----Library Management\n\n")
        f.write("----Returned by: " + borrower+ "\n\n")
        f.write("----Borrowed Date: " + str(DT.currentDateTime()) + "\n\n\n")
        f.write("S.N \t\t\t BookName \t\t\tAuthorName \n\n")


    if borrower.isalpha() == True:
        try:
            fname = borrower+ "Borrowed.txt"
            with open(fname, "r") as f:
                for x in f:
                    x = x.replace("[","")
                    x = x.replace("]","")
                    x = x.replace("'","")
                    x = x.split(", ")     
                print(x) 
        except:
            print("Your file name is invalid!!")
            return
    else:
        print("Please enter alphabetes!")
        Return()
        

    while True:
        count += 1
        if len(x) != 0:
            for main, word in enumerate(x):
                print(main, ". " , word)
            print("\n Books you have borrowed. Which you can return back! \n")
            #asking number from user for returning book
            while True:
                try:
                    bookmain = int(input('Enter the number of the book that you want to return: '))
                    bookname = x[bookmain]
                    break
                except ValueError:
                    print("Please enter only numerical values!! ")
                    continue
                except IndexError:
                    print("Please enter the number acording to the index")
                    continue
            x.remove(bookname)
            with open(fname, "w") as f:
                f.write(str(x))


            main = book.index(bookname)
            Stock[main] =Stock[main] + 1

            with open(filereturnName, "a") as f:
                f.write(str(count) + "          " + book[main] + "         " + author[main])

            with open("book.txt", "w") as f:
                for i in range(len(book)):
                    f.write(book[i]+','+ author[i]+','+ str(Stock[i])+','+'NRs'+ str(bookprice[i]) + "\n")

            print("\n Is the return date expired \n")
            
            while True:
                choice = str(input( "Yes or No: "))
                if choice.isalpha() == True:
                    break
                else:
                    print("Please enter only alphabets ")
                    continue

            if choice.lower() == "y" or choice.lower() == "yes":
                while True:
                    try:
                        time = int(input("Time taken to return the book?"))
                        break
                    except ValueError:
                        print("Please enter numerical values only!! ")
                        continue

                payment += time * 1 
                cost += bookprice[main] + payment
               
                with open(filereturnName, "a") as f:
                    f.write("\n\n\n\n\n Total Cost : \n\n\n" +  str(cost))
            else:
                cost += bookprice[main] 
                with open(filereturnName, "a") as f:
                    f.write("\n\n\n\n\n Total Cost : " + str(cost))

            print('\n Returned.Your book is recived\n')
           

            print("\n Would you like to return more books?\n\n ")

            while True:
                choice = input(" Yes or No : ")
                if choice.isalpha() == True:
                    break
                else:
                    print("Please enter alphabets")
                    continue

            if choice.lower() == "y" or choice.lower() == "yes":
                continue
            else:
                with open(filereturnName,"r") as f:
                    r=f.read()
                    print(r)
                print("Thankyou for coming to our Library!! ")
                break
        else:
            print("No more books to return. You have returned all the books! ")
            print("\nThankyou for coming to our library: ")
            break
        

        


