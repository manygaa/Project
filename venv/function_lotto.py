import random
import time
import sys

def enterign_numbers():
    string = raw_input("\nEnter 6 numbers in the range from 1 to 49, divide the number by spaces: ")
    string = string.strip(" ")
    string = string.split()
    numbers = []
    for i in string:
        if i.isdigit():
            numbers.append(int(i))
        else:
            print "The value entered \'",i,"\' is not a number!"
    if len(numbers) != 6:
        print("Incorrect value, there should be 6 numbers!")
        return wrong_data_menu()
    else:
        if len(list(set(numbers))) != len(numbers):
            print("Numbers can not be repeated!")
            return wrong_data_menu()
        elif max(numbers) > 49:
            print "Wrong range of numbers, too large numbers:", "\'", max(numbers) ,"\'"
            return wrong_data_menu()
        elif min(numbers) < 1:
            print "Wrong range of numbers, too small numbers:", "\'", min(numbers), "\'"
            return wrong_data_menu()
    return numbers

def Lottery_numbers():
    random.seed(time.time())
    lottery_numbers = []
    for i in range(6):
        lottery_numbers.append(random.randint(1, 49))
    if len(list(set(lottery_numbers))) != 6:
        return Lottery_numbers()
    return lottery_numbers

def draw_animation(lottery_numbers):
    time.sleep(1)
    print("\nDraw!!!\nKeep your finger crossed:)\nThe block is released, we draw 6 numbers:")
    time.sleep(3)
    for i in lottery_numbers:
        print i,
        time.sleep(3)
    return 0

def winning_animation(hit_numbers):
    time.sleep(2)
    print "\n\nYou have chosen",len(hit_numbers), "numbers correctly"
    time.sleep(2)
    if len(hit_numbers) <= 2:
        print("Unfortunately you won nothing, try again.")
    elif len(hit_numbers) == 3:
        print("Congratulations! Your win is 24 PLN")
    elif len(hit_numbers) == 4:
        print("Congratulations! Your win is 134 PLN")
    elif len(hit_numbers) == 5:
        print("Congratulations! Your win is 4 933 PLN")
    else:
        print("Congratulations! Your win is 1 000 000 PLN")
    return 0

def when_I_win(numbers):
    counter = 1
    hit_numbers = []
    while len(hit_numbers) != 6:
        lottery_numbers = Lottery_numbers()
        hit_numbers = [i for i in numbers if i in lottery_numbers]
        counter += 1
    return counter

def final_menu(hit_numbers, numbers):
    if len(hit_numbers) != 6:
        print("Do you want to play again? Maybe you want to check at which draw would you win the main prize?")
        answer = raw_input(
            "Enter P to play again:\nEnter C to check (this may take a while)\nEnter Q to finish the program: ")
        if answer == "C" or answer == "c" or answer == "Check" or answer == "check" or answer == "CHECK":
            print "The main win would be after ", when_I_win(numbers), "draws."
        elif answer == "Q" or answer == "q" or answer == "Quit" or answer == "quit" or answer == "QUIT":
            print("End of the program!\nSee you")
            sys.exit(0)
        elif answer == "P" or answer == "p" or answer == "Play" or answer == "play" or answer == "PLAY":
            play_again = 1
            return play_again
        else:
            print("Incorrect value!")
            final_menu(hit_numbers, numbers)
    else:
        print ("Congratulations, you won the main prize")
    return 0

def welcome_menu():
    answer = raw_input("You want to enter numbers or choose at random (enter E or R): ")
    if answer == "E" or answer == "e" or answer == "enter" or answer == "ENTER" or answer == "Enter":
        numbers = enterign_numbers()
        print "Your coupon ", numbers
    elif answer == "R" or answer == "r" or answer == "random" or answer == "Random" or answer == "Random":
        numbers = Lottery_numbers()
        print "Your coupon ", numbers
    else:
        print("Incorrect value!")
        return welcome_menu()
    return numbers

def wrong_data_menu():
    answer = raw_input("Do you want to enter numbers again (Y or N): ")
    if answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes" or answer == "YES":
        return enterign_numbers()
    elif answer == "N" or answer == "n" or answer == "no" or answer == "No" or answer == "NO":
        print("End of the program!\nSee you")
        sys.exit(0)
    else:
        print("Incorrect value!")
        return wrong_data_menu()
    return 0