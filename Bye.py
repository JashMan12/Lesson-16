Valid=False
while not Valid:
    try:
        num=int(input("Give me any number."))
        while num%2==0:
            print("bye")
        Valid=True
    except:
        print("There is some error.")
