def is_vogal(letra) -> bool:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return True
    else:
        return False

def getEstacaoDoAno(mes, dia):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia < 21):
        return "verao"  # Verão: 21/12 a 20/03
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
        return "outono"  # Outono: 21/03 a 20/06
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 21):
        return "inverno"  # Inverno: 21/06 a 20/09
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        return "primavera"  # Primavera: 21/09 a 20/12
    else:
        return "data invalida"

def getSigno(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "gemeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "cancer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "leao"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "escorpiao"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "aquario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "peixes"
    else:
        return "data invalida"

def proximo_dia(dia, mes, ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return "data invalida"

    if dia == dias_por_mes[mes - 1]:
        mes += 1
        dia = 1
        if mes > 12:
            mes = 1
            ano += 1
    else:
        dia += 1

    return ano, mes, dia

def calcular_linha_triangulo_pascal(n):
    triangulo = []
    for linha in range(n):
        nova_linha = [1]  # O primeiro elemento de cada linha é sempre 1
        if linha > 0:
            ultima_linha = triangulo[-1]
            for i in range(len(ultima_linha) - 1):
                novo_valor = ultima_linha[i] + ultima_linha[i + 1]
                nova_linha.append(novo_valor)
            nova_linha.append(1)  # O último elemento de cada linha é sempre 1
        triangulo.append(nova_linha)
    return triangulo

def imprimir_triangulo_pascal(n):
    triangulo = calcular_linha_triangulo_pascal(n)
    for linha in triangulo:
        for numero in linha:
            print(numero, end=" ")
        print()

def isPrimo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def prox_primo(numero):
    while True:
        numero += 1
        if isPrimo(numero):
            return numero

def calcular_soma_quadrados(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito ** 2
        numero //= 10
    return soma

def isFeliz(numero):
    sequencia = set()  # Usamos um conjunto para verificar ciclos infinitos
    while numero != 1 and numero not in sequencia:
        sequencia.add(numero)
        numero = calcular_soma_quadrados(numero)
    return numero == 1

def contar_digitos(numero):
    if numero == 0:
        return 0
    return 1 + contar_digitos(numero // 10)

def soma_digitos(numero):
    if numero == 0:
        return 0
    return numero % 10 + soma_digitos(numero // 10)

def imprimir_pares(inicio, fim):
    if inicio > fim:
        return
    if inicio % 2 == 0:
        print(inicio, end=" ")
    imprimir_pares(inicio + 1, fim)
def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)

def numero_quadrados(n):
    if n == 0:
        return 0
    else:
        quadrados_anteriores = numero_quadrados(n - 1)
        quadrados_n = n * n
        return quadrados_anteriores + quadrados_n
