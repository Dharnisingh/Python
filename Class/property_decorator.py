# @porperty decorator acts like
# 1: getter = @property
# 2: setter = @var_name.setter
# 3: deleter = @var_name.deleter
# allwos us to access methods as object
# Same functionality can be achived using property() method

class Emp:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        print("Getting Name:")
        return self._name
    @name.setter
    def name(self, my_name):
        print("Setting Name:")
        self._name = my_name
    @name.deleter
    def name(self):
        print("Deleting Name:")
        del self._name

print("Creating instance of Emp class:")
emp1 = Emp("Dr.John")
#Using getter
print(emp1.name)
#Using Setter
emp1.name = "Dr.Phill"
print(emp1.name)
#using Deleter
del emp1.name
