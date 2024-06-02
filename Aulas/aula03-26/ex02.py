print('Abrindo elevador')
total = 0
while True:
    peso = input('Digite o seu peso: ');
    if not peso:
        break
    else:
        total += int(peso)
        if total > 500:
            total -= int(peso)
            print(f"Elevador fechado...\nPeso suportado: {total}")
            break
        elif total == 500:
            break
            print(f"Elevador fechado...\nPeso suportado: {total}")