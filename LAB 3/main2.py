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


print(rownanie_kwadratowe(6, 1, 3))
print(rownanie_kwadratowe(1, 2, 1))
print(rownanie_kwadratowe(1, 4, 1))

# ====================================
