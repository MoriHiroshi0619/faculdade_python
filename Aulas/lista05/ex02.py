def clonar_lista(lista):
    return list(lista)

original = [1, 2, 3, 4, 5]
copia = clonar_lista(original)

print("Lista original:", original)
print("Cópia da lista:", copia)
