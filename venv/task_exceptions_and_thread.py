#tastk number 4 date: 2018-06-07

import threading
from time import gmtime, strftime, time, sleep
from datetime import datetime


def moduloFibonacci(n, delay, mod=7):
    return FibonacciRecursion(n) % mod

def FibonacciRecursion(n):
    result = 0
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    try:
        result = FibonacciRecursion(n-1) + FibonacciRecursion(n-2)
    except (RecursionError, OverflowError) as e:
        print("Logic error - maximum recursion!!!")
    return result

def Iteracion(counter, delay, iterations):
    for i in range(iterations):
        string_result = datetime.now().strftime('%Y-%m-%d') + ": " + str(counter) + "\n"
        file_Iteracion.write(string_result)
        counter += 1
        sleep(delay)

def FibonacciIterative(n, delay, iterations):
    for i in range(iterations):
        a,b = 0,1
        for i in range(i):
            a,b = b, a + b
        string_result = datetime.now().strftime('%Y-%m-%d') + ": " + str(a) + "\n"
        file_FibonacciIterative.write(string_result)
        sleep(delay)

def GoldenNumberFibonacci(n, delay, iterations):
    result = 0
    for i in range(iterations):
        try:
            result = FibonacciRecursion(n) / FibonacciRecursion(n - 1)
        except ZeroDivisionError:
            print("Logic error - diversion by zero!!!")
        string_result = datetime.now().strftime('%Y-%m-%d') + ": " + str(result) + "\n"
        file_GoldenNumberFibonacci.write(string_result)
        n += 1
        sleep(delay)

def ModuloFibonacci(n, delay, iterations, mod = 7):
    for i in range(iterations):
        string_result = datetime.now().strftime('%Y-%m-%d') + ": " + str(FibonacciRecursion(n) % mod) + "\n"
        file_ModuloFibonacci.write(string_result)
        n += 1
        sleep(delay)

def FractalFibonacci(n, delay, iterations):
    for i in range(iterations):
        string_result = datetime.now().strftime('%Y-%m-%d') + ": " + str(moduloFibonacci(n, 9) + moduloFibonacci(n - 1, 9)) + "\n"
        file_FractalFibonacci.write(string_result)
        n += 1
        sleep(delay)


#print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print("\nWelcome to Fibonacci numbers:)\n")
loop_condition = True
while loop_condition == True:
    print("\nPlease enter a number for what you want to do.\n")
    print("Enter 1 to start the program with default values.")
    print("enter 2 to select the delay value and the number of iterations.")
    print("Enter \"Q\" to quit.\n")
    main_input = input("What would you like to do? ")

    if main_input == "Q" or main_input == "q":
        loop_condition = False
        break
    elif main_input == "1":
        delay = 0.5
        iterations = 35
        print("Threads started at", datetime.now().strftime('%H:%M:%S'), "planned completion after 3 minutes)
        break
    else:
        print("Incorect value")

print("The program works on large numbers so the time is dependent on the speed of your computer")

try:
    file_Iteracion = open("file_Iteracion.txt", "a+")
    file_FibonacciIterative = open("file_FibonacciIterative.txt", "a+")
    file_GoldenNumberFibonacci = open("file_GoldenNumberFibonacci.txt", "a+")
    file_ModuloFibonacci = open("file_ModuloFibonacci.txt", "a+")
    file_FractalFibonacci = open("file_iFractalFibonacci.txt", "a+")
except FileExistError:
    print("Error - the file already exits")
else:
    print("Files for data have been created")


t1 = threading.Thread(name="Iteration", target=Iteracion, args =(1, delay, iterations,))
t2 = threading.Thread(name="Fibonacci", target=FibonacciIterative, args =(1, delay, iterations,))
t3 = threading.Thread(name="Golden number Fibonacci", target=GoldenNumberFibonacci, args =(3, delay, iterations,))
t4 = threading.Thread(name="Modulo Fibonacci", target=ModuloFibonacci, args =(1, delay, iterations,))
t5 = threading.Thread(name="Fractal Fibonacci", target=FractalFibonacci, args =(1, delay, iterations,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


