import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ZADANIE 1

x = np.arange(-3, 3.2, 0.2)
y = (x**2)+5

plt.plot(x, y, ls=":")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-3,3)
plt.yticks(np.arange(5, 17, 3))
plt.title("Wykres $x^2+5$")
plt.show()

# ZADANIE 2
x1 = np.arange(0, 10, 0.1)
x2 = np.arange(1, 6, 1)
y1 = np.sin(x1)
y2 = (x2+5)/2

fig, ax = plt.subplots(2, 2, )
ax[0, 0].plot(x1, y1, ls='dashdot', c='r', label='sin(x)+0.4')
ax[0, 0].legend(loc='lower left')
ax[0, 0].set_xlabel("x")
ax[0, 0].set_ylabel("sin(x) + 0.4")
ax[0, 0].set_title("Wykres sin(x)+0.4")

ax[1, 1].bar(x2, y2, label='f(x)=(x+5)/2')
ax[1, 1].legend(loc='upper left')
ax[1, 1].set_yticks(np.arange(1, 6, 1))
ax[1, 1].set_xticks(np.arange(1, 6, 1))
ax[1, 1].set_xlabel("x")
ax[1, 1].set_ylabel("wyniki funkcji")
ax[1, 1].set_title("Wykres słupowy funkcji")

fig.delaxes(ax[0, 1])
fig.delaxes(ax[1, 0])
plt.savefig("nikodem_przybyszewski_zad2.png")
plt.show()

# ZADANIE 3

data = pd.read_csv("cars.csv", sep=';', decimal='.')
cars = data[0:100]
cars_model_year = cars.groupby("Model year").count()
plt.pie(cars_model_year["Car name"], labels=cars_model_year.index, autopct='%d %%', textprops=dict(size=14))
plt.title("Number of cars by Model year")
plt.ylabel("Number of cars")
plt.show()

# ZADANIE 4

iris = pd.read_csv("iris.data", sep=',', decimal='.')
iris_setosa = iris[iris["class"] == "Iris-setosa"]
a = iris_setosa.iloc[:, 0].values
b = iris_setosa.iloc[:, 1].values
c = a/b

sns.set()
sns.scatterplot(x=a, y=b, hue=c, palette='magma')
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.title("Iris setosa")
plt.legend(title="Sepal length to width ratio")
plt.xlim(4, 6)
plt.ylim(2, 4.5)
plt.show()
