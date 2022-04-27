import pandas
import numpy
from matplotlib import pyplot

ts0 = pandas.Series(numpy.random.randn(1000))

ts0 = ts0.cumsum()
print(ts0)
ts0.plot()

pyplot.savefig("wykres0.png")
pyplot.show()

kraje = {
    "Kraj" : ["Belgia", "Indie", "Brazylia", "Polska"],
    "Stolica" : ["Bruksela", "New Delphi", "Brasilia", "Warszawa"],
    "Populacja" : [11190846, 1303171035, 207347528, 38675467],
    "Kontynent" : ["Europa", "Azja", "Ameryka Południowa", "Europa"]}

data = pandas.DataFrame(kraje)
print(data)

grupa = data.groupby("Kontynent").agg({"Populacja": ["sum"]})
# grupa.plot(kind="bar", xlabel="Kontynent", ylabel="Populacja (mld)", rot=0, title="Populacja na kontynentach")
wykres = grupa.plot.bar()
wykres.set_xlabel("Kontyenty")
wykres.set_ylabel("Populacja (mld)")
wykres.tick_params(axis='x', labelrotation=0)
wykres.legend()
pyplot.savefig("wykres1.png")
pyplot.show()

data = pandas.read_csv("dane.csv", header=0, sep=";", decimal=".")
print(data)
grupa = data.groupby("Imię i nazwisko").agg({"Wartość zamówienia" : ["sum"]})
print(grupa)

grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=16, figsize=(5,5), legend=False)
pyplot.savefig("wykres2.png")
pyplot.show()

data = pandas.DataFrame(ts0)
data["Średnia krocząca"] = data.rolling(window=50).mean()
data.plot()
pyplot.legend(["Wartości", "Średnia krocząca"])
pyplot.savefig("wykres3.png")
pyplot.show()