# Escreva um programa que leia dois inteiros representando um mês e um dia
# e imprima a estação do ano desse mês e dia.

import functions

dia = int(input('digite o dia: '))
mes = int(input('digite o mes: '))

print(functions.getEstacaoDoAno(mes,dia))