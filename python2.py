'''
A traveller on a visit to India is in need of some Indian Rupees (INR) but he has money belonging to another currency.
Write a python program to implement a currency calculator which accepts the amount needed in INR and the name of the currency which the traveller has.
Currency                                    Equivalent of 1.00 INR
Euro                                          0.01417
British Pound                               0.0100
Australian                                   0.02140
Canadian Dollar                              0.02027
'''
#ans

def currencycal(AmountINR,curr):
    if curr=="Euro":
        print(AmountINR*0.01417)
    elif curr=="British Pound":
        print(AmountINR*0.0100)
    elif curr=="Australian":
        print(AmountINR*0.02140)
    elif curr=="Canadian Dollar":
        print(AmountINR*0.02027)
    else:
        print(-1)
currencycal(300,"Euro")
currencycal(300,"British Pound")
currencycal(300,"Australian")
currencycal(300,"Canadian Dollar")
