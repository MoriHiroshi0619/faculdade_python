num = int(input('numero: '))
soma_divisores = 0

for i in range(1, num):
    if(num % i == 0):
        soma_divisores += i

if(soma_divisores == num):
    print(f"{num} é um numero perfeito.")
else:
    print(f"{num} não é um numero perfeito.")