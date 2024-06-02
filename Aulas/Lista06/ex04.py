#Escreva um programa em Python para calcular o produto, multiplicando todos os números de uma determinada tupla.
#Tupla Original: (4, 3, 2, 2, -1, 18)
#Produto - multiplicando todos os números da dita tupla: -864

from functools import reduce

tupla = (4, 3, 2, 2, -1, 18)

def multiplicar(x, y):
    return x * y

produto = reduce(multiplicar, tupla)

print(f"Tupla Original: {tupla}")
print(f"Produto: {produto}")
