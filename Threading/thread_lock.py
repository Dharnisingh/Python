import threading
import time

var = 0;
lock = threading.Lock()
def worker():
    ''' I am worker thread '''
    print("I am worker thread...")
    print("Lock acquired..")
    global var
    lock.acquire()
    var = var +1
    lock.release()
    print("Lock released..")


t = threading.Thread(target= worker)
t1 = threading.Thread(target= worker)
t2 = threading.Thread(target= worker)

t.start()
t1.start()
t2.start()

t.join()
t1.join()
t2.join()

print("Final Value = {}".format(var))

