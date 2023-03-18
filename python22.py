class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
#--------------------------------------------------------------

class Example:
    def __init__(self,num):#num is local variable
        self.num=num#self.num is instance variable
    def set_num(self,num):
        num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
#----------------------------------------------------------------------
class Example:
    def __init__(self,num1):
        self.num=num1
    def set_num(self,num2):
        self.num=num2
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
