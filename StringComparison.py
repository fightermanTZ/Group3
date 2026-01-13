first_string=input("Enter a word: ")
second_string=input("Enter a word: ")

if first_string==second_string:
    print("The strings are equal")
else:
    print("The strings are not equal")


if len(first_string)>len(second_string):
    print("The first string is longer")
elif len(first_string)==len(second_string):
    print("The strings have equal length")
else:
    print("The second is longer")