# Implementation od decorator

def smart_divide(func):
    def inner(a,b):
        print("Going to divide {} and {}".format(a,b))
        if(b==0):
            print("Cant Divide")
            return
        else:
            print("Calling divide method from decorator")
            print("It will return to inner function")
            return func(a,b)
    return inner

# Definig decorator
@smart_divide
def divide(a,b):
    print(a/b)

# Calling decorator
# Same as divide = smart_divide(divide)
divide(5,2)
