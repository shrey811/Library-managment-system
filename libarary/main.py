
import borrowed as B
import returned as R
print( "\n\n WELCOME TO MY LIBRARY \n\n" )
def main():

     print("--- press 1 to borrow a book")
     print("--- press 2 to return a book")
     print("--- press 3 to exit")

print(  "\n Please Follow accordingly with the guided instructions: \n" )
main()
while True:

    try:
        choice = int(input("\n\n Insert the  numbers accordingly to fulfill task:  "))
        if choice == 1:
            B.Borrow()
            main()
            continue
        
        elif choice == 2:
            R.Return()
            main()
            continue

        elif choice == 3:
             print(" Please visit the libary again, Thank you ")
             break
    except ValueError:    
        print("Please enter 1,2 or 3")



