 for loop version --> odd elements

result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)
#list comprehension version --> odd elements
print([i for i in range(11)if i%2!=0]) #syntax-output inner_loop_with_range condition
print([i for i in range(11)if i%2==0])
