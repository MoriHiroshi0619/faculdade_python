import functions

numero = int(input('digite um numero natural maior que 10:'))

if functions.isFeliz(numero):
    print('eh felix')
else:
    print('não eh feliz')