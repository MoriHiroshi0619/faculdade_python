deposito_inicial = float(input("Digite o valor do deposito inicial: "))
taxa_juros = float(input("Digite a taxa de juros: "))

saldo = deposito_inicial

ganho_total = 0

print("\nSaldo da poupança mes a mes:")
for mes in range(1, 25):
    saldo *= (1 + taxa_juros)
    ganho_mes = saldo - deposito_inicial  
    ganho_total += ganho_mes  
    print(f"Mês {mes}: Saldo = R${saldo:.2f}, Ganho com juros = R${ganho_mes:.2f}")

print("\nGanho total com juros ao longo dos 24 meses:", f"R${ganho_total:.2f}")
