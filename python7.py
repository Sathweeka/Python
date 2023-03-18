'''
write a python function which accepts a string and returns a string made of the first 2 and the last 2 characters of the given string. if the string length is less than 2, return -1.
note: if the string length is equal to 2, consider the 2 characters to be the first as well as the last two characters.
sample input             expected output
w3resource                  w3ce
A                            -1
'''
#ans

def word(str1):
    if len(str1)<2:
        return -1
    else:
        return str1[0:2]+str1[-2:]
print(word("water"))
print(word(input()))
