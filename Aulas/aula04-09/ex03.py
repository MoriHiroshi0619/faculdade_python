from random import randrange, randint

sorteio = []

for _ in range(6):
    sorteio.append(randrange(60))

sorteio.sort()
print(sorteio)
