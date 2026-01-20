x=23
def change_number():
    x=100
    return x
print(x) # before calling the list the x value remained the same
x=change_number()
print(x) # after calling our function x value changed to 100

lst=[2,3,5,6,8]
def change_lst():
    lst[0]=999
    return lst
print(lst) # Before calling our function our list remain the same
change_lst()
print(lst) # After calling our function the first value in the list changed to 999