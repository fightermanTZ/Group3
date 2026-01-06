number=int(input("Guess a number between 1 to 9 only: "))

while number>9 or number<1:
    number = int(input("Guess a number between 1 to 9 only: "))
print("Well guessed")