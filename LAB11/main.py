import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


# plt.plot([1, 2, 3, 4])
# plt.ylabel('jakies liczby')
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# plt.axis([0, 6, 0, 20])
# plt.show()

# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r', t, t**2, 'g', t, t**3, 'b')
# plt.legend(labels=['liniowa', 'kwadratowa', 'sześcienna'])
# plt.show()

# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label="liniowa")
# plt.plot(x, x**2, label="kwadratowa")
# plt.plot(x, x**3, label="sześcienna")
# plt.xlabel('etykieta x')
# plt.ylabel("etykieta y")
# plt.title("Tytuł wykresu")
# plt.legend()
# plt.savefig('wykres_matplot.png')
# plt.show()
# im1 = Image.open('wykres_matplot.png')
# im1 = im1.convert('RGB')
# im1.save('wykres_matplot.jpg')
# plt.show()

# x = np.arange(0, 10, 0.1)
# y = np.sin(x)
# plt.plot(x, y, label="sin(x)")
#
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.title("Wykres sin(x)")
# plt.legend()
# plt.show()

# data = {'a' : np.arange(50),
#         'c' : np.random.randint(0, 50, 50),
#         'd' : np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]}, d={data['d'][0]}")
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('wartość a')
# plt.ylabel('wartość b')
# plt.show()

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, '-')
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

x = np.random.randn(10000)
plt.hist(x, bins=50, facecolor='b', alpha=0.75, density=True)
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
plt.grid()
plt.show()