def transaction():
    total=1
    try:
        prompt = int(input("Enter the transaction amount "))
        if prompt != 0:
            print("The amount is ", prompt)
            total+=1
            transaction()
        elif prompt == 0:
            total+=1
            print("The total transactions are ",total)
            print("Process terminated")
    except ValueError:
        print("Sorry the input is invalid")
        transaction()


transaction()