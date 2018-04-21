def enterign_numbers():
    string = raw_input("Enter 6 numbers in the range from 1 to 49, divide the number by spaces: ")
    string = string.strip(" ")
    string = string.split()
    numbers = []

    for i in string:
        if i.isdigit():
            numbers.append(int(i))
        else:
            print "The value entered \'",i,"\' is not a number!"
    if len(numbers) != 6:
        print("Incorect value, there should be 6 numbers!")
        answer = raw_input("Do you want to enter numbers again (Y or N): ")
        if answer == "Y" or answer == "y":
            enterign_numbers()
        elif answer == "N" or answer == "n":
            print("End of the program!\nSee you")
    else:
        if len(list(set(numbers))) != len(numbers):
            print("Numbers can not be repeated!")
        elif max(numbers) > 49:
            print("Wrong range of numbers, too large numbers!")
        elif min(numbers) < 1:
            print("Wrong range of numbers, too small numbers!")
        else:
            print("Acceptation of entered values.")
            print(numbers)
    return numbers