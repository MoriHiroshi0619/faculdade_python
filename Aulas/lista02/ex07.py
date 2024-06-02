sequencia = input("Digite a sequência de números inteiros separados por espaço: ").split()

segmentos = 0

numero_anterior = None

for numero in sequencia:
    numero = int(numero)
    
    if numero != numero_anterior:
        segmentos += 1
    
    numero_anterior = numero

print(f"A sequencia possui {segmentos} segmentos de numeros iguais.")
