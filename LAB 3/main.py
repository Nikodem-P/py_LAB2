a = []

for x in range(10):
    a.append(x**2)
print(a)

a2 = [x**2 for x in range(10)]
print(a)

# ==================================

b =[]

for x in range(6):
    b.append(3**x)
print(b)

b2 = [3**x for x in range(6)]
print(b2)

# ==================================

c = []
for x in a:
    if x % 2 == 1:
        c.append(x)
print(c)

c2 = [x for x in a if x % 2 == 1]
print(c2)

