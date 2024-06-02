import functions

numero = int(input('digite um numero: '))

if functions.isPrimo(numero):
    print(f"{numero} é primo.")
else:
    proximo = functions.prox_primo(numero)
    print(f"O proximo primo depois de {numero} é {proximo}.")
