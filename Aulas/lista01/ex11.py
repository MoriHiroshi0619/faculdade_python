quantidade_numeros = 0
soma = 0
while True:
    numero = int(input("Digite um numero inteiro: "))
    
    if numero == 0:
        break
    quantidade_numeros += 1
    soma += numero

if quantidade_numeros > 0:
    media = soma / quantidade_numeros
else:
    media = 0

print("\nQuantidade de numeros digitados:", quantidade_numeros)
print("Soma dos numeros digitados:", soma)
print("Media aritmetica dos numeros digitados:", media)
