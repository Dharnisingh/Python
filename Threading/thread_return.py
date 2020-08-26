import threading
import time

def task():
    ''' I am worker thread '''
    print("I am working..")
    return "Hello"

t = threading.Thread(target=task)
t.start()
ret = t.join()
print(t)
print(ret)
