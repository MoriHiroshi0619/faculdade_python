lado1 = int(input('lado1: '))
lado2 = int(input('lado2: '))
lado3 = int(input('lado3: '))

if(((lado1+lado2)>lado3)and((lado1+lado3)>lado2)and((lado3+lado2)>lado1)):
  print('forma')
else:
  print('não forma')