

try:
    import modulek

except ImportError:
    print("Moduł nie istnieje")


try:
    file = open("plikDoOdczytu.txt", "r+")

except  PermissionError:
    print("Plik jest w trybie do ocztyu")


lista = [1, 2, 3, 55]

try:
    x = lista[65]

except IndexError:
    print("Jesteś poza zakresem tablicy")