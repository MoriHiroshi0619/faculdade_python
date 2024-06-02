primos_gemeos = []

for num in range(3, 1001):
    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and all((num + 2) % i != 0 for i in range(2, int((num + 2) ** 0.5) + 1)):
        primos_gemeos.append((num, num + 2))

print("Primso gemeos no intervalo [3, 1000]:")
for par in primos_gemeos:
    print(par)