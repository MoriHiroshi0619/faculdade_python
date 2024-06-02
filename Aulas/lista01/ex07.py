dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
quociente = 0

resto = dividendo

while resto >= divisor:
    resto -= divisor
    quociente += 1

print("Quociente:", quociente)
print("Resto:", resto)