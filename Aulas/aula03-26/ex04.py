from math import factorial
x = 2
serie = 0
for i in range(20):
    termo = x ** i / factorial(i)
    serie += termo
    print(i+1, termo, serie)