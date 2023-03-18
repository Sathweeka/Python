#Decision making statements


#read a number ---> multiple 3---> multiple of 5 ---> if both then print multiple of 3&5 else print invalid
a=int(input())
if (a&3==0 and a%5==0):
    print("multiple of both 3 and 5")
elif (a%5==0):
    print("multiple of 5")
elif (a%3==0):
    print("multiple of 3")
else:
    print(invalid)
