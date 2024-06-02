n = int(input("Digite o valor de n: "))
i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))

multiplos = []

numero_atual = 0

while len(multiplos) < n:
    if numero_atual % i == 0 or numero_atual % j == 0:
        multiplos.append(numero_atual)
    
    numero_atual += 1

print(f"Os {n} primeiros numeros multiplos de {i} ou {j} sao: {sorted(multiplos)}")

