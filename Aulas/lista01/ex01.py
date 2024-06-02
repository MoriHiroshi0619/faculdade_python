num = int(input("Digite o número base: "))
comprimento = int(input("Digite o comprimento da lista de múltiplos: "))
multiplos = []
for i in range(comprimento):
    multiplos.append(num * (i + 1))
print("Lista de múltiplos de", num, "com comprimento", comprimento, ":")
print(multiplos)

