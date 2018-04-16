import random
import time

L = ['K', 'P', 'N']

random.seed(time.time())
x =random.randint(0, 2)

wybor = input('podaj co wybierasz: ')
PK=0;
PU=0;


while wybor != "Q":
    if wybor == L[x]:
        print('Remis')
    elif wybor == "K" and L[x] == "N":
        print("wygrywa użytkownik")
        PU = PU + 1
        print("Punkty użytkownika", PU)
    elif wybor == "N" and L[x] == 'K':
        print("wygrywa komputer")
        PK = PK + 1
        print("Punkty komputera", PK)
    elif wybor == "P" and L[x] == 'K':
        print("wygrywa użytkownik")
        PU = PU + 1
        print("Punkty użytkownika", PU)
    elif wybor == "K" and L[x] == 'P':
        print("wygrywa komputer")
        PK = PK + 1
        print("Punkty komputera", PK)
    elif wybor == "N" and L[x] == 'P':
        print("wygrywa użytkownik")
        PU = PU + 1
        print("Punkty użytkownika", PU)
    elif wybor == "P" and L[x] == 'N':
        print("wygrywa komputer")
        PK = PK + 1
        print("Punkty komputera", PK)
    else:
        print("Błędna wartość!")
    x = random.randint(0, 2)
    wybor = input('podaj co wybierasz: ')




