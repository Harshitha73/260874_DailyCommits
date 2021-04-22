"""
Write a python program to check if the input number is
- real number
- float numner
- string
- complex number
- Zero (0)
"""

n=input("Enter input: ")

try:
    val=int(n)
    if val==0:
        print("Zero")
    else:
        print("Input is a real number")
except ValueError:
    try:
        val=float(n)
        print("Input is a float number")
    except ValueError:
        print("Input is a string")

#print(type(n))