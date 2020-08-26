# Python support allmost all kind of inheritance
# callin base calls constructor -> Base_cls.__init__(self)
# also super.__init__(self)
# syntax of inheritance --> child_ls(Base_cls1,Base_cls2...)
# all base class members are available in derived class
class Emp_base:
    def __init__(self,name):
        self.emp_name = name
        self.emp_type = "Default"

    def get_name(self):
        print("Employee Name: {}".format(self.emp_name))
    def get_type(self):
        print("Employee type: {}".format(self.emp_type))

# Derived class
class Manager(Emp_base):
    def __init__(self,mgr_name):
        # calling base class constructor
        Emp_base.__init__(self,mgr_name)
        self.emp_type = "Manager"
    def get_name(self):
        print("Manager Name: {}".format(self.emp_name))
    def get_type(self):
        print("Type of Emp: {}".format(self.emp_type))

emp_base = Emp_base("Teem Hock")
emp_base.get_name()
emp_base.get_type()

emp_mgr = Manager("Dr John")
emp_mgr.get_name()
emp_mgr.get_type()

