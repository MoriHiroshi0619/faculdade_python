numero_decimal = int(input("Digite o numero decimal: "))

binario = []

while numero_decimal > 0:
    binario.append(numero_decimal % 2)
    numero_decimal //= 2

binario.reverse()

numero_binario = ''.join(map(str, binario))

print(f"O numero decimal {numero_decimal} em binario é: {numero_binario}")
