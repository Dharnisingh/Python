# Static methods are bound to the class not object
# Can not access or modify state of class
# static method can access Class variable
class Emp:
    # Class variable
    raise_amt = 10
    def __init__(self, emp_name):
        self.name = emp_name
    def get_name(self):
        print("My name {}".format(self.name))
    # stati method
    @staticmethod
    def get_raise(var1):
        print("Raise amt of {} is {}".format(var1,Emp.raise_amt))
        

emp1 = Emp("Dr.John")
emp1.get_name()
# Calling static method
Emp.get_raise("My_Name")
