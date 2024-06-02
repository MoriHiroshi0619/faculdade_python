def calcular_diferenca(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)

    diff1 = list(set1 - set2)
    diff2 = list(set2 - set1)

    return diff1, diff2

Cor1 = ["vermelho", "laranja", "verde", "azul", "branco"]
Cor2 = ["preto", "amarelo", "verde", "azul"]

diff1, diff2 = calcular_diferenca(Cor1, Cor2)

print("Cor1 - Cor2:", diff1)
print("Cor2 - Cor1:", diff2)
