'''
write a python function which accepts a sentence and finds the number of letters and digits in the sentence.
it should return a list in which the first value should be letter count and the second value should be digit count.
ignore the spaces or any other special character in the sentence.
sample input                 expected output
Infosys 123                    [7,3]
ABCEFG                         [6,0]
'''
#ANS

def function(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return [l_count, d_count]
print(function("Infosys 123"))
#print(function(input()))  
