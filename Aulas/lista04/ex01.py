import string

def letras_disponiveis(palpites):
    alfabeto = set(string.ascii_lowercase)
    letras_restantes = alfabeto - set(palpites)
    return sorted(letras_restantes)

def advinhou_palavra(palpites, palavra_secreta):
    for letra in palavra_secreta:
        if letra not in palpites:
            return False
    return True

def exibir_palavra(palpites, palavra_secreta):
    exibicao = ''
    for letra in palavra_secreta:
        if letra in palpites:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

palavra_secreta = 'hiroshi'


palpites = []

while not advinhou_palavra(palpites, palavra_secreta):
    print("\njogo da Forca")
    print(f"[alavra: {exibir_palavra(palpites, palavra_secreta)}")
    print(f"letras disponíveis: {' | '.join(letras_disponiveis(palpites))}")

    palpite = input("digite uma letra: ").lower()

    if palpite in string.ascii_lowercase and len(palpite) == 1 and palpite not in palpites:
        palpites.append(palpite)
    else:
        print("entrada inválida ou letra já usada. \ntente novamente.")
        input("pressione Enter para continuar...")

print("adivinhou a palavra:", palavra_secreta)

#tentei mandar um os system('clear') pra limpar o console, mas tava dando pau