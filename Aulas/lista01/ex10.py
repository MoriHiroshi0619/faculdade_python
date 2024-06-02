divida_inicial = float(input("Digite o valor inicial da divida: "))
juro_mensal = float(input("Digite o juro mensal: "))
valor_pago_mensal = float(input("Digite o valor mensal que sera pago: "))

total_pago = 0
total_juros_pago = 0

num_meses = 0

while divida_inicial > 0:
    juros_mes = divida_inicial * juro_mensal
    total_juros_pago += juros_mes
    total_pago_mes = valor_pago_mensal + juros_mes
    if divida_inicial < total_pago_mes:
        total_pago_mes = divida_inicial
    total_pago += total_pago_mes
    divida_inicial -= total_pago_mes
    num_meses += 1

print("Numero de meses para pagar a ddvida:", num_meses)
print("Total pago:", total_pago)
print("Total de juros pago:", total_juros_pago)
