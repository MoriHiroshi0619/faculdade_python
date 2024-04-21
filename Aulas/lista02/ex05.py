numero_binario = input("Digite o numero binario: ")

numero_decimal = 0

for indice, digito in enumerate(reversed(numero_binario)):
    digito = int(digito)
    
    numero_decimal += digito * (2 ** indice)

print(f"O numero binario {numero_binario} em decimal é: {numero_decimal}")
