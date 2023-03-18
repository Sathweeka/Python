'''
write a python function, find_pairs_of_numbers() which accepts a list of positive integers ith no repetitions and returns count of pairs of numbers in the list that adds up to n.
the function should return 0, if no such pairs are found in the list.
sample input                         expected output
[1,2,7,4,5,6,0,3],6                           3 (1,5)(2,4)(6,0)
[3,4,1,8,5,9,0,6],9                           4 (3,6)(4,5)(1,8)(9,0)
'''
#ans

def find_pairs_of_numbers(num_list,n):
    count=0
    for x in num_list:
        index=num_list.index(x)+1 #index=1
        for y in range(index,len(num_list)):
            if x+num_list[y]==n: #1+2==6
                count+=1  #count=0
    return count
num_list=[1,2,7,4,5,6,0,3]
n=6#int(input())
print(find_pairs_of_numbers(num_list,n))
