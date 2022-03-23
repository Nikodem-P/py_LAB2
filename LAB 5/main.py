class Kształty():
#definicja konstruktora
    def __init__(self, x, y):
#deklarujemy atrybuty
#self wskazuje że chodzi o zmienne własnie definiowanej klasy
        self.x = x
        self.y = y
        self.opis = "To jest klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik


#klasa która dziedziczy po klasie Kształty
class Kwadrat(Kształty):
    def __init__(self,x):
        self.x = x
        self.y = x
# i jeszcze klasa, która dziedziczy po klasie Kwadrat
# bedzie definiwoać figurę złożoną z 3 kwadratów w kształcie litery L
#  _
# | |_
# |_ _|


class KwadratLiteraL(Kwadrat):
    def obwod(self):
        return 8 * self.x

    def pole(self):
        return 3 * self.x * self.y

#inicjujemy klasę Kwadrat
kwadrat = Kwadrat(5)

#sprawdzenie metod z klasy bazowej
print(kwadrat.obwod())
print(kwadrat.pole())
kwadrat.dodaj_opis("Nasza figura to kwadrat")
print(kwadrat.opis)
kwadrat.skalowanie(0.3)
print(kwadrat.obwod())
print("")

#inicjujemy klasę KwadratLiteraL
litera_l = KwadratLiteraL(5)
print(litera_l.obwod())
print(litera_l.pole())
litera_l.dodaj_opis("Litera L")
print(litera_l.opis)
litera_l.skalowanie(0.5)
print(litera_l.obwod())

