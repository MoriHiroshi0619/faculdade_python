from math import factorial
CASAS_DECIMAIS = 15
PRECISAO = 10**-CASAS_DECIMAIS
x = 2
serie_anterior = 1.0
serie_atual = 3.0
i = 1
while(abs(serie_anterior-serie_atual) >= PRECISAO):
    i += 1
    termo = x ** i / factorial(i)
    serie_anterior = serie_atual
    serie_atual += termo
    print(i, termo, serie_atual)
print('Valor arrredondado com {0} casas decimais: {1}'.format(CASAS_DECIMAIS, round(serie_atual, CASAS_DECIMAIS)))