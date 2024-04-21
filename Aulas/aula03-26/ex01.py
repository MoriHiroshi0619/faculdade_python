print('Iniciando nova venda')
total = 0
while True:
    preco = input('Digite o preço do produto: ');
    if not preco:
        
        break
    else:
        total += int(preco)
print('total da venda:', total)