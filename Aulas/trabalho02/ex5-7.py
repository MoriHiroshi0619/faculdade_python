mediaAltura = 0
mA = 0
mediaIdade = 0
mI = 0
for i in range(5):
  idade = int(input(f"[{i}]idade: "))
  altura = int(input(f"[{i}]altura: "))
  if(altura < 170):
    mediaIdade += idade
    mI = mI + 1

  if(idade > 20):
    mediaAltura += altura
    mA = mA + 1


if(mA != 0):
  mediaAltura = mediaAltura / mA
  print(f"altura media dos com mais de 20 anos: {mediaAltura}")
elif(mA == 0):
  print('ninguem acima de 20 anos')
else:
  print(f"{5 - mA} pessoas abaixo de 20 anos ")

if(mI != 0):
  mediaIdade = mediaIdade / mI
  print(f"idade media dos com altua inferior a 170: {mediaIdade}")
elif(mI == 0):
  print('ninguem abaixo de 170cm')
else:
  print(f"{5 - mI} pessoas acima de 170cm")