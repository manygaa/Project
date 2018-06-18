#tastk number 3 date: 2018-06-07

import threading
from time import gmtime, strftime, time, sleep
from datetime import datetime
import sys

#Recursive functions needed for a function from a task.
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

#5 functions to the task
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

#Simpe menu
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
        print("See you:)")
        sys.exit(0)
    elif main_input == "1":
        delay = 0.5
        iterations = 35
        timeout = 180
        print("\nThreads started at", datetime.now().strftime('%H:%M:%S'), "planned completion after 3 minutes")
        break
    elif main_input == "2":
        main_input_2 = input("Enter 3 values (iterations, delay(sec), waiting time for a thread(sec)) separated by spaces: ")
        main_input_2 = main_input_2.strip(" ")
        main_input_2 = main_input_2.split()
        numbers = []
        for i in main_input_2:
            if i.isdigit():
                numbers.append(int(i))
            else:
                print("Incorect value")
        if len(numbers) != 3:
            print("Incorrect value, there should be 3 numbers!")
        else:
            iterations = numbers[0]
            delay = numbers[1]
            timeout = numbers[2]
            print("\nThreads started at", datetime.now().strftime('%H:%M:%S'), "program execution time unknown.")
            break
    else:
        print("Incorect value")

print("The program works on large numbers so the time is dependent on the speed of your computer.")

#Creating files
try:
    file_Iteracion = open("file_Iteracion.txt", "a+")
    file_FibonacciIterative = open("file_FibonacciIterative.txt", "a+")
    file_GoldenNumberFibonacci = open("file_GoldenNumberFibonacci.txt", "a+")
    file_ModuloFibonacci = open("file_ModuloFibonacci.txt", "a+")
    file_FractalFibonacci = open("file_iFractalFibonacci.txt", "a+")
except FileExistError:
    print("\nError - creating files")
else:
    print("\nSuccessful creation of files.")

#Creating threads
try:
    t1 = threading.Thread(name="Iteration", target=Iteracion, args =(1, delay, iterations,))
    t2 = threading.Thread(name="Fibonacci", target=FibonacciIterative, args =(1, delay, iterations,))
    t3 = threading.Thread(name="Golden number Fibonacci", target=GoldenNumberFibonacci, args =(3, delay, iterations,))
    t4 = threading.Thread(name="Modulo Fibonacci", target=ModuloFibonacci, args =(1, delay, iterations,))
    t5 = threading.Thread(name="Fractal Fibonacci", target=FractalFibonacci, args =(1, delay, iterations,))
except Exception:
    print("\nError in connecting threads!!!")
else:
    print("\nSuccessful connecting threads.")


#Start threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join(timeout)
t2.join(timeout)
t3.join(timeout)
t4.join(timeout)
t5.join(timeout)

#Closing files after completing threads
if not t1.isAlive() and not t2.isAlive() and not t2.isAlive() and not t3.isAlive() and not t4.isAlive() and not t5.isAlive():
    file_Iteracion.close()
    file_FibonacciIterative.close()
    file_GoldenNumberFibonacci.close()
    file_ModuloFibonacci.close()
    file_FractalFibonacci.close()
    print("\nAll threads finished, closing files.")
else:
    print("\nError threads during execution, unable to properly close files!!!")

print("See you:)")



