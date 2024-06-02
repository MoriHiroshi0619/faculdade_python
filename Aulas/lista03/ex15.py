import functions
tamanho = int(input("Digite o tamanho da grade quadrada (n): "))
total_quadrados = functions.numero_quadrados(tamanho)
print(f"O numero total de quadrados em uma grade quadrada de tamanho {tamanho} * {tamanho} eh {total_quadrados}.")