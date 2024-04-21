numero = input('digite o numero: ')
numero = list(numero)
numero.reverse()
numeroInverte = ''
for num in numero:
    numeroInverte += num
print(numeroInverte)