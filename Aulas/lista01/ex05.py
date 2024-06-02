numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = 0

negativo = False
if numero2 < 0:
    negativo = True
    numero2 = -numero2

for _ in range(numero2):
    resultado += numero1

if negativo:
    resultado = -resultado

print("O resultado da multiplicação é:", resultado)
