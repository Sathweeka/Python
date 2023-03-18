for loop version -->even elements square
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
#list comprehension version -->even elements square
print([i if i%2!=0 else i**2 for i in range(11)])
