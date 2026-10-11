try:
    Number1=int(input("Enter any number"))
    print("The number you have entered is",Number1)
except ValueError as ex:
    print("You have not enter a number.")
    print("The error is ",ex)