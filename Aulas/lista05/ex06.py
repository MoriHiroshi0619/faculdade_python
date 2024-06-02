lista_base = ['p', 'q']
n = 5

lista_concatenada = []

for i in range(1, n + 1):
    for item in lista_base:
        lista_concatenada.append(item + str(i))

print("Lista concatenada:", lista_concatenada)
