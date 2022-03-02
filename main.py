a = 4
b = 6
if a > b:
   print("Liczba a jest wieksza")
elif a < b:
   print("Liczba b jest wieksza")
else:
   print("Liczby sa rowne")

# ================================================================
    
a = input("Podaj liczbe: ")
print(a)
print(type(a))
a = int(a)
print(type(a))

# ================================================================

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

# ================================================================    
    
lista = ['a', 3, 4, 5.6]

for i in lista:
    print(i, end = ' ')
else:
    print("Wyswietlone zostaly elementy z listy")

# ================================================================    
    
licznik = 0
while licznik != 11:
    print(licznik, end = ' ')
    licznik += 1
else:
    print("Koniec petli")

# ================================================================
    
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
