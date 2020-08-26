# Dunder methonds can be used to emulate behaviour of builtin type to user defined object
# these are special method and we should never invent our own dunder methods
# Thes methods gets called automatically depending on events line __init__() gets called when object is created
# Examples of Dunder methods
# 1: __init__() == object initialization
# 2: __str__(self) == To print object in human redable format called when we do print(obj)
# 3: __repr__(self) == called when we do >> obj
# 3: __getitem__(self, index) == used to access element at index obj[2] 
# 4: __setitem__
# 5: __item__

class Emp:
    def __init__(self,name):
        self.name = name
        self.role = "Manager"
    def __str__(self):
        print("Calling __str__ dunder")
        return "Name = {} Role = {}".format(self.name, self.role)

emp1 = Emp("Dr.john")
print(emp1)
