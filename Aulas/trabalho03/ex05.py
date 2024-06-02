salario = 2000
aumento_salarial = 0.05
divida = 100
taxa_juros = 0.15
mes = 10
ano = 2016

while divida <= salario:
    if mes == 3:
        salario *= (1 + aumento_salarial)
    
    divida *= (1 + taxa_juros)
    
    mes += 1
    
    if mes > 12:
        mes = 1
        ano += 1

print(f"A dívida de Pedro com o cartão de crédito será superior ao seu salário no mês {mes} de {ano}.")
