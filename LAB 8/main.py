import numpy

# Zadanie 1
matrix1 = numpy.array(3)
matrix2 = numpy.array(3)
print(matrix1 * matrix2)

# Zadanie 2
matrix3 = numpy.arange(9).reshape((3, 3))
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
