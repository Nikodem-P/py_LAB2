import math
# Zadanie 1
file = open("tekst.txt", "r", encoding="UTF-8")
file.read(63)
znaki = file.read(42)
# print(znaki)
male = 0
for i in znaki:
    if i.islower():
        male += 1
if male > 0:
    print("Liczba malych liter: %(x)d" % {"x": male})
else:
    print("Brak malych liter.")
file.close()

# Zadanie 2
def funkcja(arg):
    nowa_lista = [x for x in arg if not(str(x).isalpha())]
    max = nowa_lista[0]
    min = nowa_lista[0]
    for i in nowa_lista:
        if i > max:
            max = i
        if i < min:
            min = i
    return nowa_lista, min, max

print(funkcja(["a", 3, 4.54, "g", 8, -19.5, 41.5, "fbsdjk", 8, 5486]))

# Zadanie 3
try:
    a = int(input("Wprowadz liczbe calkowita a = "))
    b = int(input("Wprowadz liczbe calkowita b = "))
    if (math.sin(a)**2 + math.cos(b)**2) == 1:
        file = open("zadanie3.txt", "w+")
        file.writelines("jedynka trygonometryczna zachodzi")
        file.close()
        # print("ok1")
    else:
        file = open("zadanie3.txt", "w")
        file.writelines("jedynka trygonometryczna nie zachodzi")
        file.close()
        # print("ok2")
except ValueError:
        file = open("zadanie3.txt", "w")
        file.writelines("bledne dane")
        file.close()
        # print("blad")

# Zadanie 4

lista_calkowite = [1, 9, 2, 2, 6, 4, 5, 6, 3, 5, 4]
lista_calkowite2 = [x for x in lista_calkowite if x > lista_calkowite[len(lista_calkowite)-1]]
print(lista_calkowite2)

# Zadanie 5
wynik = round((math.e**3 + (math.log(math.cos(36)**2 + math.pi))**(1/5)), 2)
print(wynik)

# Nikodem Przybyszewski 3io
