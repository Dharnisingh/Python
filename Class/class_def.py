# Basic functionality of class

class my_class():
    # Constructor
    def __init__(self,emp_name):
        self.name = emp_name
        print("Constructor of class")
    # Destructor will be called when we delete object
    # Or it goes out of scope 
    def __del__(self):
        print("Destructor of class")
    # Class method
    def get_name(self):
        return "My name is: {}".format(self.name)
# Creating class object    
obj = my_class("Dr. John")
#Calling class method
print(obj.get_name())
