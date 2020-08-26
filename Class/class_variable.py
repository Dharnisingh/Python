# Class variables are shared among instances of class
# Can be assecced using className.variable or objectname.variable

class Emp():
    #class variable
    raise_amt = 5
    def __init__(self,emp_name):
        self.name = emp_name
    def get_name(self):
        return "My Name: {}".format(self.name)
    def raise_sal(self):
        print("My raise is {}".format(self.raise_amt))

emp1 = Emp("John")
print(emp1.get_name())
emp1.raise_sal()
# Accessing class variable using Class name
print(Emp.raise_amt)
