from pakiet import *
napis = 'dzis jest piatek'
litery.wyswietl(napis)
print(litery.ile_liter(napis))
print(dodawanie.dodawanie(3, 4))

plik = open('tekst.txt', 'r')
znaki = plik.read(10)
linia = plik.readline()
wiersze = plik.readlines()
plik.close()
print(znaki)
print(linia)
print(wiersze)

import sys
print("podaj napis:")
dane = sys.stdin.readline()

plik = open("dane.txt", "w+")
plik.write(dane)
plik.close()

lista = []
for i in range(6):
    lista.append(i)

plik = open("dane.txt", "a+")
plik.writelines(str(lista))
plik.close()

with open("tekst.txt", "r") as plik:
    for linia in plik:
        print(linia, end='')

class PierwszaKlasa:
    """Pierwsza klasa python"""
    atrybut = 5323
    def pierwsza_metoda(self):
        return "pierwsza metoda klasy"

obiekt = PierwszaKlasa()
print(obiekt)
print(obiekt.atrybut)
obiekt.tekst = "sihf"
print(obiekt.tekst)
# obiekt2 = PierwszaKlasa()
# print(obiekt2.tekst)
print(obiekt.pierwsza_metoda())

class Ksztalty:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = "To jest ksztalt."

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, tekst):
        self.opis = tekst

    def skalowanie(self, czynnik):
        self.x *= czynnik
        self.y *= czynnik


prostokat = Ksztalty(3,5)
print(prostokat.pole())
print(prostokat.obwod())
print(prostokat.opis)
prostokat.dodaj_opis("To jest prostokat.")
print(prostokat.opis)
prostokat.skalowanie(2)
print(prostokat.pole())
print(prostokat.obwod())
