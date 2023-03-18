'''class Customer:
    def __init__(self):
        cust_id=100                 #attribute error
c1=Customer()
print(c1.cust_id)

#------------------------------------------------------------------

class Customer:
    def __init__(self,id):
        id=100                 #attribute error
c1=Customer(200)
print(c1.id)'''
#-----------------------------------------------------------------
class Customer:
    def __init__(self,id):
        self.id=100                 
c1=Customer(200)
print(c1.id)

#---------------------------------------------------------------

class Customer:
    def __init__(self,id):
        self.id=id                 
c1=Customer(200)
print(c1.id)
