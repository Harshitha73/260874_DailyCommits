"""
Write Python code that asks a user how many pizza slices they want.
The pizzeria charges Rs 123.00 a slice
if user order even number of slices, price per slice is Rs 120.00
Print the total price depending on how many slices user orders.
"""

n=int(input("Enter number of slices: "))
if n%2==0:
    price=120.00*n
else:
    price=123.00*n
print(price)