import math


def rownanie_kwadratowe(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Brak rozwiazan")
        return -1
    elif delta == 0:
        print("Jedno rozwiazanie")
        x = (-b)/(2*a)
        return x
    else:
        print("Dwa rozwiazania")
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        return x1, x2

def czy_parzysta(aLiczba):
    if aLiczba % 2 == 0:
        print("Parzysta")
        return 1
    else:
        print("Nieparzysta")
        return 0

def dlugosc_odcinka(x1 = 0, y1 =0, x2 = 0, y2 = 0):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(rownanie_kwadratowe(6, 1, 3))
print(rownanie_kwadratowe(1, 2, 1))
print(rownanie_kwadratowe(1, 4, 1))
print("=======================")
czy_parzysta(2)
czy_parzysta(3)
print("=======================")
print(dlugosc_odcinka())
print(dlugosc_odcinka(1,2,2,2))
print(dlugosc_odcinka(2,2, y2 = 2, x2 = 1))
print(dlugosc_odcinka(y1 = 2, x1 = 5, y2 = 5, x2 = 3))
print(dlugosc_odcinka(1,1))
