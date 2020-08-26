import threading
import time

def worker():
    ''' Worker thread '''
    for i in range(1000):
        print("I am worker thread..")
        time.sleep(0.1)
    return

def work2():
    ''' Worker second '''
    for i in range(1000):
        print("I am worker2 thread")
        time.sleep(0.3)

t = threading.Thread(target=worker)
t1 = threading.Thread(target=work2)
t.start()
t1.start()
