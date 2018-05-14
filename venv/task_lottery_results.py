import string

class lottoResults:
    def __init__(self, Number, L1, L2, L3, L4, L5, L6):
        self.number = Number
        self.l1 = L1
        self.l2 = L2
        self.l3 = L3
        self.l4 = L4
        self.l5 = L5
        self.l6 = L6
    def __repr__(self):
        return str(self.l1) + " " + str(self.l2) + " " + str(self.l3) + " " + str(self.l4) + " " + str(self.l5) + " " + str(self.l6)


file = open("wyniki-lotto-sortowane.csv", "r+")
fileContent = file.readlines()
file.close()



fileContent[:] = [line.rstrip('\n') for line in fileContent]
fileContent.pop(0)
number = [i.split(';')[0] for i in fileContent]
day = [i.split(';')[1] for i in fileContent]
month = [i.split(';')[2] for i in fileContent]
year = [i.split(';')[3] for i in fileContent]
l1 = [i.split(';')[4] for i in fileContent]
l2 = [i.split(';')[5] for i in fileContent]
l3 = [i.split(';')[6] for i in fileContent]
l4 = [i.split(';')[7] for i in fileContent]
l5 = [i.split(';')[8] for i in fileContent]
l6 = [i.split(';')[9] for i in fileContent]
day = [str(item).zfill(2) for item in day]
month = [str(item).zfill(2) for item in month]

dictionary = {}
for i in range(len(number)):
    dictionary.update({day[i] + "-" + month[i] + "-" + year[i]: lottoResults(number[i], l1[i], l2[i], l3[i], l4[i], l5[i], l6[i])})

loop_condition = True
while loop_condition == True:
    print("\nWelcome to Lottery results!\n")
    print("\nPlease enter a number for what you want to do.\n")
    print("Enter 1 for display all draws.")
    print("Enter 2 for displaying a single draw.")
    print("Enter 3 for division.")
    print("Enter 4 for multiplication.")
    print("Enter \"Q\" to quit.\n")
    main_input = input("What would you like to do? ")

    if main_input == "Q" or main_input == "q":
        loop_condition = False
        break
    elif main_input == "1":
        for keys, values in dictionary.items():
            print("Data:", keys, "Drawn numbers:", values)
    elif main_input == "2":
        data = input("Enter the date (data format dd-mm-yyyy) of the draw: " )
        value = dictionary.get(data)
        if value == None:
            print("Incorect value")
        else:
            print(dictionary[data])

print("See You:)")

