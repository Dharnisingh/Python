# Instance Variable remain unique to each instance of class

class Emp:
    def __init__(self):
        self.name = "Default Employee"
    def get_name(self):
        return "My Name : {}".format(self.name)
# Instance variable creted using objects
emp1 = Emp()
emp1.name = "Instance Employee"
print(emp1.get_name())
# This will call "Default Employee"
emp2 = Emp()
print(emp2.get_name())
