'''
you have x no. of 5 rupee coins and y no. of 1 rupee coins.
you want to purchase an item for amount z. the shopkeeper wants you to provide the exact change.
you want to pay using minimum number of coins. how many 5 rupee coins and 1 rupee coins will you use?
if exact change is not possible then display -1.
sample input                                                                                      expected output   
available Rs. 1 coins         available Rs.5 coins notes         Amount to be made        Rs.1 coins needed        Rs.5 notes needed       
    2                                  4                                21                      1                           4
    11                                 2                                11                      1                           2
    3                                  3                                19                               -1           
'''

#ans


def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    five = int(rupees_to_make/5)
    one_needed = rupees_to_make%5
    five_needed = five if five <= no_of_five else no_of_five
    if (five > no_of_five):
        one_needed = rupees_to_make - 5 * no_of_five     
    
    (print("No. of Five needed : {}\nNo. of One needed  : {}".format(five_needed,one_needed))) if one_needed <= no_of_one else (print(-1))

make_amount(int(input()),int(input()),int(input()))
