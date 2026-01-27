def check():
    print("Your account balance is 1000$")
    prompt = input("Do you want to check account balance again ").lower()
    if prompt == 'y':
        check()
    elif prompt=='n':
        print("Process Terminated")
    else:
        print("Sorry the input is invalid")
        prompt = input("Do you want to check account balance again ").lower()
        check()

prompt=input("Do you want to check account balance ").lower()

check()
