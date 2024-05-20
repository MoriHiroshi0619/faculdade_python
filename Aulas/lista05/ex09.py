def mover_zeros_para_final(lista):
    numeros_sem_zeros = []
    zeros_count = 0

    for num in lista:
        if num != 0:
            numeros_sem_zeros.append(num)
        else:
            zeros_count += 1

    numeros_sem_zeros.extend([0] * zeros_count)

    return numeros_sem_zeros

lista_original = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

lista_resultante = mover_zeros_para_final(lista_original)

print("Lista original:", lista_original)
print("Mova todos os dígitos zero para o final da lista de números:", lista_resultante)
