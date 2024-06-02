quantia_saque = int(input("Digite o valor do saque: "))

qtd_50 = 0
qtd_20 = 0
qtd_10 = 0
qtd_5 = 0
qtd_1 = 0

while quantia_saque > 0:
    if quantia_saque >= 50:
        qtd_50 += 1
        quantia_saque -= 50
    elif quantia_saque >= 20:
        qtd_20 += 1
        quantia_saque -= 20
    elif quantia_saque >= 10:
        qtd_10 += 1
        quantia_saque -= 10
    elif quantia_saque >= 5:
        qtd_5 += 1
        quantia_saque -= 5
    else:
        qtd_1 += 1
        quantia_saque -= 1

print("Quantidade de notas de R$ 50,00:", qtd_50)
print("Quantidade de notas de R$ 20,00:", qtd_20)
print("Quantidade de notas de R$ 10,00:", qtd_10)
print("Quantidade de notas de R$ 5,00:", qtd_5)
print("Quantidade de notas de R$ 1,00:", qtd_1)