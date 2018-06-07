import threading
import time

def deamonTread():
    print("Starting")
    time.sleep(5)
    print("Exiting")

def nonDeamonTread():
    print("Starting")
    time.sleep(2)
    print("Exiting2")

d = threading.Thread(name="deamonThread", target=deamonTread, daemon = True)
t = threading.Thread(name="nonDeamonThread", target=nonDeamonTread, daemon = True)

x = threading.enumerate()
print(x)

d.start()
t.start()
#d.join()
#t.join()

main_thread = threading.main_thread()

x = threading.enumerate()
print(x)
for th in threading.enumerate():
    if th is main_thread:
        continue
    print("join" + main_thread.getName())
    th.join()

x = threading.enumerate()
print(x)