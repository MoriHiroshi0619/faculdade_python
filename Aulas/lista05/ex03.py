def tem_elemento_comum(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

lista_a = [1, 2, 3, 4, 5]
lista_b = [5, 6, 7, 8, 9]


print(tem_elemento_comum(lista_a, lista_b))
