def hello():
    print('ola mundo')

def calcular_preco_aluguel(km_percorridos, dias_alugados, veiculo_pequeno=True):
    preco_por_dia = 60 if veiculo_pequeno else 80
    preco_por_km = 0.15 if veiculo_pequeno else 0.20

    preco_dias = preco_por_dia * dias_alugados
    preco_km = preco_por_km * km_percorridos
    preco_total = preco_dias + preco_km
    return preco_total

def calcular_bonus_do_escravo(dias_de_meta_batida = 0):

    if dias_de_meta_batida > 32 and dias_de_meta_batida <= 40:
        dif = dias_de_meta_batida - 32 
        
    elif dias_de_meta_batida > 40 and dias_de_meta_batida <= 48:
        dif = 8 * 325 + (( dias_de_meta_batida - 40 ) * 550 )
        
    elif dias_de_meta_batida > 48:
        dif = 8 * 325 + 8 * 550 + (dias_de_meta_batida - 48) * 600
    else:
        dif = 0
        
    return dif
  
