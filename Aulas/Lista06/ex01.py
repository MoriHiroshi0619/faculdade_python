#Escreva um programa Python para verificar se existe um elemento dentro de uma tupla.

def verificar_elemento(tupla, elemento):
    if elemento in tupla:
        print(f"{elemento} está presente na tupla.")
    else:
        print(f"{elemento} não está presente na tupla.")


tupla = (1, 2, 3, 4, 5)

elemento = 3

verificar_elemento(tupla, elemento)

elemento = 6

verificar_elemento(tupla, elemento)