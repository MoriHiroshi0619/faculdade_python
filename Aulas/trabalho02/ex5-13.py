ano = int(input('ano: '))

if((ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)):
  print('é bissexto')
else:
  print('num é bissexto')