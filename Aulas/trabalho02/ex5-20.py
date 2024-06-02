dia = int(input("digite o dia: "))
mes = int(input("digite o mes: "))
ano = int(input("digite o ano: "))
quantidade_dias = int(input("digite a quantidade de dias pra somar: "))

if dia < 31 and mes < 12:
  while quantidade_dias > 0:
      if mes in {1, 3, 5, 7, 8, 10, 12}:
          if dia < 31:
              dia += 1
          elif dia == 31 and mes != 12:
              dia = 1
              mes += 1
          else:
              dia = 1
              mes = 1
              ano += 1
      elif mes == 2:
          if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):  # Ano bissexto
              if dia < 29:
                  dia += 1
              elif dia == 29:
                  dia = 1
                  mes += 1
          else:
              if dia < 28:
                  dia += 1
              elif dia == 28:
                  dia = 1
                  mes += 1
      else:
          if dia < 30:
              dia += 1
          elif dia == 30:
              dia = 1
              mes += 1

      quantidade_dias -= 1
  print("data somada:", dia, "/", mes, "/", ano)
else:
  print("digitou inputs invalidos")