def lista_com_maior_soma(listas):
    maior_soma = float('-inf')
    lista_maior_soma = None

    for lista in listas:
        soma = sum(lista)

        if soma > maior_soma:
            maior_soma = soma
            lista_maior_soma = lista

    return lista_maior_soma

listas = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

resultado = lista_com_maior_soma(listas)

print("Lista com maior soma:", resultado)
