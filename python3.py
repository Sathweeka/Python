'''
The flight ticket rates for a round-trip (mumbai->dubai) were as follows:
Rate per Adult: Rs. 37550.00
Rate per child: 1/3rd of the rate per adult
Service Tax: 7% of the ticket amount (including all passengers)
As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
Find and display the total ticket cost for a group which had adults and children.

sample input                                  expected output
Number of adults     Number of children        Ticket cost
  5                       3                     204910.35
  3                       1                     120535.5
'''

#ans

n_adults=int(input("Enter the number of adults: "))
n_childs=int(input("Enter the number of childs: "))
total=((n_adults*37550.0)+(n_childs*37550.0/3))
print(total)
total1=total*0.07
total2=total+total1
print("with ur service tax",total2)
total_amount=total*0.90
print(total_amount)


#-------------------------------------------------------------------

n_adults=int(input("Enter the number of adults: "))
n_childs=int(input("Enter the number of childs: "))
print((((n_adults*37550.0)+(n_childs*37550.0/3)*1.07)*0.90))
