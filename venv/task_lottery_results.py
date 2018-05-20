#task Lotto 20.05.2018

#Simple class with a constructor
class ClassLottoResults:

    def __init__(self, Index, Number1, Number2, Number3, Number4, Number5, Number6):
        self.index = Index
        self.number1 = Number1
        self.number2 = Number2
        self.number3 = Number3
        self.number4 = Number4
        self.number5 = Number5
        self.number6 = Number6

    def __repr__(self):
        return str(self.number1) + " " + str(self.number2) + " " + str(self.number3) + " " + str(self.number4) + " " + \
               str(self.number5) + " " + str(self.number6)

#Method for statistics
    def lucky_number(self, lucky):
        counter = 0
        for i in n1:
            if lucky == i:
                counter += 1
        for i in n2:
            if lucky == i:
                counter += 1
        for i in n3:
            if lucky == i:
                counter += 1
        for i in n4:
            if lucky == i:
                counter += 1
        for i in n5:
            if lucky == i:
                counter += 1
        for i in n6:
            if lucky == i:
                counter += 1
        return counter

#Reading and closing the file
file = open("wyniki-lotto-sortowane.csv", "r+")
fileContent = file.readlines()
file.close()

#Converting data
fileContent[:] = [line.rstrip('\n') for line in fileContent]
fileContent.pop(0)
index = [i.split(';')[0] for i in fileContent]
day = [i.split(';')[1] for i in fileContent]
month = [i.split(';')[2] for i in fileContent]
year = [i.split(';')[3] for i in fileContent]
n1 = [i.split(';')[4] for i in fileContent]
n2 = [i.split(';')[5] for i in fileContent]
n3 = [i.split(';')[6] for i in fileContent]
n4 = [i.split(';')[7] for i in fileContent]
n5 = [i.split(';')[8] for i in fileContent]
n6 = [i.split(';')[9] for i in fileContent]
day = [str(item).zfill(2) for item in day]
month = [str(item).zfill(2) for item in month]

#Creating and assigning data to structures
lottoObject = ClassLottoResults
dictionary = {}
for i in range(len(index)):
    dictionary.update(
        {day[i] + "-" + month[i] + "-" + year[i]: lottoObject(index[i], n1[i], n2[i], n3[i], n4[i], n5[i], n6[i])})

#Simple menu
loop_condition = True
while loop_condition == True:
    print("\nPlease enter a number for what you want to do.\n")
    print("Enter 1 for display all draws.")
    print("Enter 2 for displaying a single draw.")
    print("Enter 3 to check how many times the number has been drawn.")
    print("Enter 4 to show statistics of numbers.")
    print("Enter \"Q\" to quit.\n")
    main_input = input("What would you like to do? ")

    if main_input == "Q" or main_input == "q":
        loop_condition = False
        break
    elif main_input == "1":
        for keys, values in dictionary.items():
            print("Data:", keys, "Drawn numbers:", values)
    elif main_input == "2":
        data = input("Enter the date (data format dd-mm-yyyy) of the draw: ")
        value = dictionary.get(data)
        if value == None:
            print("Incorect value")
        else:
            print("Draws on this day is: ", dictionary[data])
    elif main_input == "3":
        main_input2 = input("Enter the number to check: ")
        print("The given number", main_input2, "occureend in", ClassLottoResults.lucky_number(lottoObject, main_input2), "draws.")
    elif main_input == "4":
        max = 0
        min = ClassLottoResults.lucky_number(lottoObject, str(1))
        for i in range(1, 50):
            counter = ClassLottoResults.lucky_number(lottoObject, str(i))
            print("NUmber", i, "took part in", counter, "draws.")
            if counter > max:
                max = counter
                counter_max = i
            if counter < min:
                min = counter
                counter_min = i
        print("\nThe most frequenlty drawn number is:", counter_max)
        print("The least drawn number is:", counter_min)
    else:
        print("Incorect value")

print("See You:)")
