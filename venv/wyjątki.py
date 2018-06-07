import threading
import time

def print_time(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("name: " + name + " " + time.ctime(time.time()))

t1 = threading.Thread(target=print_time,  args=("watekA", 2))
t2 = threading.Thread(target=print_time,  args=("watekB", 1))
t3 = threading.Thread(target=print_time,  args=("watekC", 5))

t1.start()
t2.start()
t3.start()

print_time("lala", 1)