#range function

#1 to 100
for i in range(1,101):# range(start,end,step)
    print (i,end=' ')
#print(*no of objects, step=' ',end='\n')
#odd numbers between 1 to 100

for i in range(1,101,2):
    print(i,end=' ')
print()
#even numbers between 1 to 100

for i in range(2,101,2):
    print(i,end=' ')
    
# numbers in reverse order
for i in range(100,0,-1):# range(start,end,step)
    print (i,end=' ')
print()
#odd numbers between 100 to 1

for i in range(99,0,-2):
    print(i,end=' ')
print()
#even numbers between 100 to 1

for i in range(100,1,-2):
    print(i,end=' ')
