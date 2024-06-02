n = int(input("Digite um número inteiro: "))
resultado = 1
for i in range(1, n + 1):
    fatorial = 1
    for j in range(1, i + 1):
        fatorial *= j
    resultado *= fatorial
print("O fatorial dos fatoriais de", n, "é:", resultado)