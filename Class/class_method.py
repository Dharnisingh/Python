# class method is a decorator 
# class methods can be accessed using class name or obj name
# while declaring class method use "cls" as first argument.
# instead of "cls" we can take any name
# class method can be used as alternative to constructor
class Emp:
    # Class variable
    raise_val = 10
    def __init__(self, emp_name):
        self.name = emp_name
    def get_name(self):
        print("My Name: {}".format(self.name))
    def get_raise(self):
        print("Raise of emp: {}".format(self.raise_val))
    # Class method definition
    @classmethod
    def my_class_method(cls, raise_amt):
        cls.raise_val = raise_amt

emp1 = Emp("Dr.John")
emp1.get_name()
print("Class raiae_val {}".format(Emp.raise_val))

# Using class method
Emp.my_class_method(20)
# It will show 20
emp1.get_raise()
