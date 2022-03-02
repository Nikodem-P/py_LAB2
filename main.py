a = 4
b = 6
if a > b:
   print("Liczba a jest wieksza")
elif a < b:
   print("Liczba b jest wieksza")
else:
   print("Liczby sa rowne")

a = input("Podaj liczbe: ")
print(a)
print(type(a))
a = int(a)
print(type(a))

a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))
d = int(input("Podaj liczbe d: "))

if (a > b) & (c > d):
    print("Liczba a > b i c > d")
else:
    print("Liczba a < b lub c < d")

for i in range(0, 7, 1):
    print(i, end = ' ')

lista = ['a', 3, 4, 5.6]

for i in lista:
    print(i, end = ' ')
else:
    print("Wyswietlone zostaly elementy z listy")

licznik = 0
while licznik != 11:
    print(licznik, end = ' ')
    licznik += 1
else:
    print("Koniec petli")

lista = [4, 6, 2, 5, 3, 9, 8, 7]
a = int(input("Podaj liczbe: "))
licznik = 0
while licznik != len(lista):
    if a - lista[licznik] == 0:
        print("liczba " + str(a) + " - " + str(lista[licznik]) + " = 0")
        break
    else:
        licznik += 1
else:
    print("Zadna z wartosci z listy nie dala odpowiedniego wyniku.")

lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3]
suma = []
for i in lista1:
    for j in lista2:
        wynik = i + j
        suma.append(wynik)
    print(suma)

a = input("Wartosc a: ")
b = input("Wartosc b: ")
try:
    a = int(a)
    b = int(b)
    wynik = a / b
    print(wynik)
except ZeroDivisionError:
    print("Nie dzieli sie przez 0")
except ValueError:
    print("Nie wczytano liczby calkowitej")

lista = [1,0,1,0,1,0,1,0,1,0]
try:
    a = int(input("Podaj nowa liczbe: "))
    lista.append(a)
    lista.insert(0,a)
    print(lista)
except ValueError:
    print("Niepoprawna wartosc")

lista.sort()
print(lista)

lista.reverse()
print(lista)

print("Usunieta wartosc na indeksie 0: " + str(lista.pop(0)))
print(lista)

student = {
    "imie" : "Jan",
    "nazwisko" : "Kowalski",
    "wydzial" : "wmii",
    "nrindeksu" : "123456"
}

print("Student: " + student["imie"] + " " + student["nazwisko"])
print("Wydzial i nr indeksu: " + student["wydzial"] + " " + student["nrindeksu"])

student.update({"pesel" : "12345678901"})

print("PESEL: " + student["pesel"])


