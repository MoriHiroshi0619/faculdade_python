def verificar_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        return False

    contagem1 = {}
    contagem2 = {}

    for elemento in lista1:
        if elemento in contagem1:
            contagem1[elemento] += 1
        else:
            contagem1[elemento] = 1

    for elemento in lista2:
        if elemento in contagem2:
            contagem2[elemento] += 1
        else:
            contagem2[elemento] = 1

    return contagem1 == contagem2

lista1 = ['ola', 'mundo', 'php']
lista2 = ['mundo', 'php', 'ola']

print(f"Listas São iguais: {verificar_listas(lista1, lista2)}")
