class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material
s1=Shoe(1000, "Canvas")
print(s1)
print(s1.price,s1.material)
#-----------------------------------------------------

class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material
s1=Shoe(1000, "Canvas")
print(s1)
print("the unique id of the object",id(s1))
#-------------------------------------------------------

class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material
    def __str__(self):
        return "Shoe with price: " + str(self.price) + " and material: " + self.material
s1=Shoe(1000, "Canvas")
print(s1)
