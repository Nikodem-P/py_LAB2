# Python list comprehension
a = []

for x in range(10):
    a.append(x**2)
print(a)

# Skrócona forma
a2 = [x**2 for x in range(10)]
print(a)

# ==================================

b =[]

for x in range(6):
    b.append(3**x)
print(b)

# Skrócona forma
b2 = [3**x for x in range(6)]
print(b2)

# ==================================

c = []
for x in a:
    if x % 2 == 1:
        c.append(x)
print(c)

# Skrócona forma
c2 = [x for x in a if x % 2 == 1]
print(c2)

# ==================================

lista = []
for a in [1, 2, 3]:
    for b in [4, 5, 6]:
        lista.append((a,b))
print(lista)

# Skrócona forma
lista2 = [(a,b) for a in [1,2,3] for b in [4,5,6]]
print(lista2)

# ==================================

slownik = {
    "PZU": "Panstwowy Zaklad Ubezpieczen",
    "ZUS": "Zaklad Upezpieczen Spolecznych",
    "PKO": "Panstwowa Kasa Oszczednosci"
}

slownik_odwrocony = {}

for key, value in slownik.items():
    slownik_odwrocony[value] = key

print(slownik)
print(slownik_odwrocony)

slownik2 = {value: key for key, value in slownik.items()}
print(slownik2)
