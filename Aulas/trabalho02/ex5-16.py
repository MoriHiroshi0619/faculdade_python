idade = int(input("digite a idade do nadador: "))

if idade < 5:
    print("idade invalida para competição.")
elif 5 <= idade <= 7:
    print("classificação: infantil A")
elif 8 <= idade <= 10:
    print("classificação: infantil B")
elif 11 <= idade <= 14:
    print("classificação: juvenil A")
elif 15 <= idade <= 17:
    print("classificação: juvenil B")
else:
    print("classificação: adultos")