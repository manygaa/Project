import random
import time


random.seed(time.time())

x =random.randint(0, 9)

print(x)

s = ["Adam", "Marek", "Jacek", "Ewelina", "Krzysztyf", "Katarzyna", "Elwira", "Aleksandra", "Kasia", "Małgosia"]

print(s[x])
