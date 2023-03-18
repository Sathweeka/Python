'''write a python program to display all the common characters between two strings.
return -1 if there are no matching characters.
note: ignore blank spaces if there are any.
perform the case sensitive string comparison wherever necessary.
sample input                             expected output
"I like Python"
"Java is a very popular language"         lieyon
'''
#ans

def common_char(str1,str2):
    str=""
    for i in str1:
        if i in str2:
            if i not in str:
                str=str+i
    if(str):
        return str.replace(" "," ")
    else:
        return -1
str1=str(input())
str2=str(input())
print(common_char(str1,str2))
