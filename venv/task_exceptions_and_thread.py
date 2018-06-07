#tastk number 4 date: 2018-06-07

import threading
import time


def Iteracion(counter):
    counter += 1
    return counter

def Fibonacci(n):
    if(n == 0):
        return 1
    if(n == 1):
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

def GoldenNumberFibonacci(n):
    return Fibonacci(n) / Fibonacci(n-1)

def ModuloFibonacci(n, mod = 7):
    return Fibonacci(n) % mod

def FractalFibonacci(n):
    return ModuloFibonacci(n, 7) + ModuloFibonacci(n-1, 7)

print(Fibonacci(10))
print(GoldenNumberFibonacci(10))
print(ModuloFibonacci(13))
print(FractalFibonacci(13))

t1 = threading.Thread(name="Iteration", target=Iteracion, args =(0))
t2 = threading.Thread(name="Fibonacci", target=Fibonacci, args =(0))
t3 = threading.Thread(name="Golden number Fibonacci", GoldenNumberFibonacci, args =(0))
t4 = threading.Thread(name="Modulo Fibonacci", target=ModuloFibonacci, args =(0))
t5 = threading.Thread(name="Fractal Fibonacci", target=FractalFibonacci, args =(0))


