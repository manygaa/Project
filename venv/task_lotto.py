#task lotto 2018-04-16
import random
import time


def avoiding_repetion(x):
    temp = [x]

def choice_numbers():
    x = raw_input("Enter 6 numbers in the range from 1 to 49, divide the number by spaces: ")
    return x
def conversion(x):
    for i in list_string:
        x.append(int(i))
    return x



print("The Lotto game, the probability of winning is 1 to 13 983 816!")
string = choice_numbers()
list_string = string.split(" ")

numbers = []
i = 0
numbers = conversion(list_string)
for j in len(numbers):
    if type(numbers[i]) == int and numbers[i] >= 1 and numbers[i] <= 49:
        if j <= 6:
            answer = raw_input("Too many numbers, accept the first 6 or do You want to enter new numbers (\"Y\" or \"N\"")
            if answer == 'Y' or answer == 'y':
                break
            elif answer == 'N' or answer == 'n':
                choice_numbers()
                j = 0
            else:
                print("Incoret value")
    else:
        numbers[i] = raw_input("Incorrect value in position ", i, " enter a new one: ")
print(numbers)

random.seed(time.time())



