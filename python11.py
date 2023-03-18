#matrix 2D data
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop version --> odd then square if it is even cube it
result=[]
for row in mat:
    row_element=[]
    for element in row:
        if element%2!=0:
            row_element.append(element**2)
        else:
            row_element.append(element**3)
    result.append(row_element)
print(result)
#list comprehension-->odd then square if it is even then cube

print([element**2 if element%2!=0 else element**3 for row in mat
       for element in row])             #syntax-condition outer_loop inner_loop
print([[element**2 if element%2!=0 else element**3 for element in row]
       for row in mat])
