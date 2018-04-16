import random
import time

L = ['K', 'P', 'N']

random.seed(time.time())
x =random.randint(0, 2)

wybor = raw_input('podaj co wybierasz: ')
PK=0;
PU=0;


while wybor != "Q":
    if wybor == L[x]:
        print('Remis')
    elif wybor == "K" and L[x] == "N":
        print("wygrywa uzytkownik")
        PU = PU + 1
        print("Punkty uzytkownika", PU)
    elif wybor == "N" and L[x] == 'K':
        print("wygrywa komputer")
        PK = PK + 1
        print("Punkty komputera", PK)
    elif wybor == "P" and L[x] == 'K':
        print("wygrywa uzytkownik")
        PU = PU + 1
        print("Punkty uzytkownika", PU)
    elif wybor == "K" and L[x] == 'P':
        print("wygrywa komputer")
        PK = PK + 1
        print("Punkty komputera", PK)
    elif wybor == "N" and L[x] == 'P':
        print("wygrywa uzytkownik")
        PU = PU + 1
        print("Punkty uzytkownika", PU)
    elif wybor == "P" and L[x] == 'N':
        print("wygrywa komputer")
        PK = PK + 1
        print("Punkty komputera", PK)
    else:
        print("Bledna wartosc!")
    x = random.randint(0, 2)
    wybor = raw_input('podaj co wybierasz: ')




