from threading import Thread

def task(lst_name, lst_roll):
    t = zip(lst_name, lst_roll)
    for name, roll in t:
        print("Name: {} Roll: {}".format(name,roll))

lstn = ['a', 'b', 'c', 'd']
lstr = [1,2,3,4]
t1 = Thread(target=task, args=[lstn, lstr])
t1.start()
t1.join()

print("Thread execution finished")

