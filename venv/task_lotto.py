# task lotto 2018-04-16
import random
import time
import function_lotto
#!/usr/bin/python

print("The Lotto game, the probability of winning is 1 to 13 983 816!")
string = raw_input("Enter 6 numbers in the range from 1 to 49, divide the number by spaces: ")
string = string.strip(" ")
string = string.split(" ")
numbers = []

if len(string) != 6:
    print("Incorect value, there should be 6 numbers!")
else:
    for i in string:
        numbers.append(int(i))
    if len(list(set(numbers))) != len(numbers):
        print("Numbers can not be repeated!")
    elif numbers[i] <= 0 and numbers[i] >= 50:
        print("Wrong range of numbers!")
    else:
        print("Error!!!")
print(numbers)









