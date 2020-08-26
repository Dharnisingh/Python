# There is not any concept constant in python
# we assume a variable constant by adding undersocer to the variable
# Private variables can be accessed and modified as normal variable

class Emp:
    def __init__(self, name, priv_var):
        self.name = name
        self._priv_var = priv_var
    def get_name(self):
        print("{} has private variable {}".format(self.name,self._priv_var))

emp1 = Emp("Dr.John", "PRIV")
emp1.get_name()
# Access using instance
# will be mangled as self._priv_var
print(emp1._priv_var)

