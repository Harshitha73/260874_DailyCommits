#Write a Python program to change the position of every n-th value with the (n+1)th in a list

from itertools import zip_longest, chain, tee
def changePosition(my_list):
    return my_list[-1:] + my_list[:-1]
my_list = [0,1,2,3,4,5,6,7,8,9]
print(changePosition(my_list))