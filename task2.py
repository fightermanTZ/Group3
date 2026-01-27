ussd=input("Enter the ussd code ")


def send_money():
    print('''Send Money
    1. Enter phone number
    2. International transfers
    3. To Bank
    4. To other networks
    5. Send with withdraw fee
    6. Standing order
    7. My List''')
def withdraw():
    print('''Withdraw cash
     Enter till number
    '''

if ussd!="*150*00#":
    print("Ussd is invalid")
else:
    print('''M-PESA
    1.Send money
    2. Withdraw cash
    3. Buy Bundle/Airtime
    4. Pay by M-pesa
    5. Loans and savings
    6. Financial services
    7. TUZO
    8. Self services
    9. Mwendokasi''')
    option=int(input(''))
    if option==1:
        send_money()
    elif option==2:
        withdraw()
