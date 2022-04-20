import numpy
import pandas

s1 = pandas.Series([1, 3, 5.5, numpy.nan, 'a'])
print(s1)

s2 = pandas.Series([10, 12, 8, 14], index=['a','b','c','d'])
print(s2)

dane = {
    "Kraj" : ["Belgia", "Indie", "Brazylia"],
    "Stolica" : ["Bruksela", "New Delphi", "Brasilia"],
    "Populacja" : [11190846, 1303171035, 207347528]}

df = pandas.DataFrame(dane)
print(df)

daty = pandas.date_range('20220420', periods=5)
print(daty)

df2 = pandas.DataFrame(numpy.random.randn(5, 4), index=daty, columns=list('ABCD'))
print(df2)

iris = pandas.read_csv("iris.csv", header=0, sep=',', decimal='.')
print(iris)

iris.to_csv("nowy.csv", index=False)

xlsx = pandas.ExcelFile("wyniki.xlsx")
df3 = pandas.read_excel(xlsx, header=0)
print(df3)

df3.to_excel('nowy.xlsx', sheet_name="Arkusz 1", index=False)
print("============")
print(s2['a'])
print(s2.a)
print(df["Stolica"])
print(df.iloc[[2], [0]])
print(df.loc[[1], ["Kraj"]])
print(df.at[0, "Kraj"])
print("Kraj: " + df.Kraj)
print(iris.sample(5))
print(iris.sample(frac=0.05))
print(iris.sample(10, replace=True))
print(df.head())
