Intiger =[1, 2, 3, 4, 5]
Float=[3.1, 45.1, 6.1, 11.5, 1,2]
Stringi=["jeden", "dwa", "trzy", "czter", "pieć"]
Mix=["jeden", 2, 4.1]

print(Intiger[0:5])
print(Float[0:5])
print(Stringi[0:5])
print(Mix[0:3])

Intiger.extend([8, 15, 20, 11, 12])
print(Intiger[0:10])

Float.extend([8.1, 15.1, 20.2, 30.1, 2.1])
print(Float[0:10])

Stringi.extend(["szesc", "siedem", "osiem", "dziewiec", "dziesiec"])
print(Stringi[0:10])

Mix.extend([8.1, 15.1, 20.2, 11.1, 3])
print(Mix[0:8])
Intiger.sort()
print(Intiger[0:10])
Float.sort()
print(Float[0:10])
Float.sort()
Stringi.sort()
print(Stringi[0:10])
Intiger.reverse()
Float.reverse()
Stringi.reverse()
Mix.reverse()
print(Intiger[0:10])
print(Float[0:10])
print(Stringi[0:10])
print(Mix[0:8])

Intiger.pop(3)
Float.pop(3)
Stringi.pop(3)
Mix.pop(3)
print(Intiger[0:10])
print(Float[0:10])
print(Stringi[0:10])
print(Mix[0:8])





