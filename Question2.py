subTotal=float(input("Enter the subtotal value: "))
gratuity=float(input("Enter the gratuity rate: "))

gratuity_rate=(gratuity/100 *subTotal)

total=gratuity_rate+subTotal

print(f'The gratuity is {gratuity_rate} and Total is {total}')