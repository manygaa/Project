import threading
import time

def print_time(delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("name: " + threading.current_thread().getName() + " " + time.ctime(time.time()))

t11 = threading.Thread(target=print_time,  args=(2,))
t22 = threading.Thread(name = "w1", target=print_time,  args=(1,))


t11.start()
t22.start()

