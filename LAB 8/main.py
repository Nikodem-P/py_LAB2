import numpy

# Zadanie 1
matrix1 = numpy.arange(3)
matrix2 = numpy.arange(3)
print(matrix1 * matrix2)
print('===============')

# Zadanie 2
matrix3 = numpy.arange(9).reshape(3, 3)
print(matrix3)
print('Wartosci maksymalne w kolumnach:')
print(matrix3.min(axis=0))
print('Wartosci maksymalne w wierszach:')
print(matrix3.min(axis=1))
print('Wartosci minimalne w kolumnach:')
print(matrix3.max(axis=0))
print('Wartosci minimalne w wierszach:')
print(matrix3.max(axis=1))
print('===============')

# Zadanie 3
print(matrix1.dot(matrix2))
print('===============')

# Zadanie 4
matrix4 = numpy.arange(3, dtype='int64')
matrix5 = numpy.array([[4.6, 7.9, 2.3]])
print(matrix4 * matrix5)
print('===============')

# Zadanie 5
matrix6 = numpy.arange(6).reshape(2, 3)
a = numpy.sin(matrix6)
print(a)
print('===============')

# Zadanie 6
matrix7 = numpy.arange(10, 22, 2).reshape(2, 3)
b = numpy.cos(matrix7)
print(b)
print('===============')

# Zadanie 7
print(a + b)

# Zadanie 8
matrix8 = numpy.arange(9).reshape(3,3)
for i in matrix8:
    print(i)
    
# Zadanie 9
matrix9 = 
