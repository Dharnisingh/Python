class Emp:
    def __init__(self, name):
        self._name = name
    def __getitem__(self,key):
        return getter(self,key)
    def __repr__(self):
        return "Repr Name = {}".format(self._name)
    def __str__(self):
        return "String Name = {}".format(self._name)
emp = Emp("Dr.John")
print(emp)
print(emp.__dict__)
