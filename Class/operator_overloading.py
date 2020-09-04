# Operator overloading in python
# __add__(self, obj) ==> called when obj1 + obj2
# __sub__(self, other)
# __mul__(self, other)
# __truediv__(self, other) ==> called when obj1/obj2
# __floordiv__(self, other) ==> obj1//obj2
# __mod__(self, other) ==> obj1 % obj2
# __pow__(self, other) ==> obj ** obj2
# __lt__(self, other) ==> obj1 < obj2
# __gt__(self, other)
# __le__(self, other)
# __ge__(self, other)
# __eq__(self, other)
# __ne__(self, other)

class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    # will be called when we perform obj1 + obj2
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Dharni")
ob4 = A("Singh")

print(ob1 + ob2)
print(ob3 + ob4)
