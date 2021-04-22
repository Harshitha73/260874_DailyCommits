#Write a Python program to find the repeated items of a tuple
tupple_x=(1,0,0,2,1,4,2,0,4,1,3,5,7,9)
tupple_y=sorted(tupple_x)
#print(tupple_y)
for i in tupple_x:
    if tupple_x.count(i) >1:
            print(i, " is repeated")
    else:
        print(i, " is unique")

