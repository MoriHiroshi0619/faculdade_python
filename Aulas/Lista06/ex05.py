#Escreva um programa em Python para calcular o valor médio dos números em uma determinada tupla de tuplas.
#Tupla Original: ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
#Valor médio dos números da referida tupla de tuplas: [30,5, 34,25, 27,0, 23,25]

tuplas = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

somas = [0] * len(tuplas[0])

for tupla in tuplas:
    for i in range(len(tupla)):
        somas[i] += tupla[i]

num_tuplas = len(tuplas)

medias = [soma / num_tuplas for soma in somas]

print(f"Tupla Original: {tuplas}")
print(f"Média: {medias}")
