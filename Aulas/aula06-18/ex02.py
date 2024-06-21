palavra = "c ovo"

def verifica_palindromo(palavra):
    if type(palavra) is not str:
        return "Expressao tem que ser string"
    if not palavra:
        return "digite uma palavra"

    lista = list(palavra)
    listaAux = []
    palavraAux = ""
    for x in palavra:
        letra = lista.pop()
        listaAux.append(letra)
        palavraAux += letra

    if palavraAux == palavra:
        return "EH palindromo"
    else:
        return "Não palidromo"

def teste(palavra):
    if type(palavra) is not str:
        return "Expressao tem que ser string"
    if not palavra:
        return "digite uma palavra"
    lista = list(palavra)
    lista2 = list(palavra)
    pilha = []
    for x in palavra:
        pilha.append(lista.pop())

    if pilha == lista2:
        return "EH palindromo"
    else:
        return "Não eh palindromo"

print(verifica_palindromo(palavra))
print(teste(palavra))