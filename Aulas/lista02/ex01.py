x = int(input("Digite o valor de x: "))
n = int(input("Digite o valor de n: "))

resultado = 1

if n > 0:
    for _ in range(n):
        resultado *= x ** (1 / n)
else:
    print("Digite um numero natural.")

print(f"A potencia {x}^(1/{n}) é aproximadamente: {resultado}")