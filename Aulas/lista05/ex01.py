def remover_duplicados(lista):
    lista_sem_duplicados = []

    for elemento in lista:
        if elemento not in lista_sem_duplicados:
            lista_sem_duplicados.append(elemento)

    return lista_sem_duplicados

lista_com_duplicados = [1, 2, 2, 3, 4, 4, 5]
lista_sem_duplicados = remover_duplicados(lista_com_duplicados)

print("lista original:", lista_com_duplicados)
print("lista sem duplicados:", lista_sem_duplicados)
