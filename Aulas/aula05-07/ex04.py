from random import randint

print('Mega-Sena')

sorteados = []
while len(sorteados) < 6:
    sorteado = randint(1, 60)
    if sorteado not in sorteados:
        sorteados.append(sorteado)

sorteados.sort()
print(sorteados)
