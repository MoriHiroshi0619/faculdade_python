def imprimir_impares(lista):
    for num in lista:
        if num % 2 != 0:
            print(num)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
imprimir_impares(lista_numeros)
