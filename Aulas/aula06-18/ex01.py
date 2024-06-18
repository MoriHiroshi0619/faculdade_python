expressao = 5.5

def verifica_expressao(expressao):
    if type(expressao) is not str:
        return "Expressao tem que ser string"
    lista = list(expressao)
    pilha = []

    for x in lista:
        if x == "(":
            pilha.append('(')
        elif x == ")":
            if not pilha:
                return "incorreto"
            pilha.pop()

    if not pilha:
        return "correto"
    else:
        return "nao correto"


print(verifica_expressao(expressao))