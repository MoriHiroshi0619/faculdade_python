n = int(input("Digite a quantidade de numeros na sequencia: "))
sequencia = []

for i in range(n):
    numero = int(input(f"Digite o {i+1}º numero: "))
    sequencia.append(numero)

maior = sequencia[0]
menor = sequencia[0]

for numero in sequencia:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("Maior número:", maior)
print("Menor número:", menor)
