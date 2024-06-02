#Escreva um programa em Python para verificar se um elemento está presente em uma tupla de tuplas.
#Tupla original: (('Vermelho', 'Branco', 'Azul'), ('Verde', 'Rosa', 'Roxo'), ('Laranja', 'Amarelo', 'Limão')))
#Verificando se o elemento 'Branco' está na referida tupla de tuplas = Verdadeiro


tupla_original = (('Vermelho', 'Branco', 'Azul'),
                  ('Verde', 'Rosa', 'Roxo'),
                  ('Laranja', 'Amarelo', 'Limão'))

elemento = 'Branco'

encontrado = False
for tupla in tupla_original:
    if elemento in tupla:
        encontrado = True
        break

if encontrado:
    print(f"'{elemento}' está presente")
else:
    print(f"'{elemento}' não esta presente")
