numero = int(input("Digite um número inteiro para ver sua tabuada: "))
for i in range(0, 10):
    resultado = numero * (i + 1)
    print(numero, "x", i + 1, "=", resultado)