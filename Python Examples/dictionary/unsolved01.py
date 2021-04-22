#Write a Python script to merge two Python dictionaries

my_dict1={ 1: "One", 2: "Two", 3: "Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven"}
my_dict2={ 1: "Sun", 102: "Mon",103:"Tue", 104:"Wed", 105:"Thu", 106:"Fri",107:"Sat"}
my_dict1.update(my_dict2)
print(my_dict1)