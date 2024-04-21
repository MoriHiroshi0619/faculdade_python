numero = int(input("Digite um número inteiro para começar a buscar os múltiplos de 3: "))
contador = 0
print("Os 10 primeiros múltiplos de 3 a partir de", numero, "são:")
for i in range(numero, numero + 30):
    if i % 3 == 0:
        print(i)
        contador += 1
        if contador == 10:
            break