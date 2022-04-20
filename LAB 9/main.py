import numpy
import pandas
import openpyxl

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
