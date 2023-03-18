class Table:
    def __init__(self):
        print(id(self))
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
dining_table=Table()
print("dining_table id is:",id(dining_table))
back_table=Table()
print("back_table id is:",id(back_table))
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)
print(id(dining_table),id(back_table),id(front_table))
print("dining_table:",id(dining_table))
print("back_table:",id(back_table))
print(id(front_table))
