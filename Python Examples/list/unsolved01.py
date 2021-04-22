#Write a Python program to find the second smallest number in a list
my_list=[10,20,30,50,12,34,40]
my_list.sort()
print("Sorted list: ",my_list)
sec_min=my_list[len(my_list)-2]
print(sec_min)