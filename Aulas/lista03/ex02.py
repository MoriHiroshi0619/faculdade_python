texto = input("digite um texto: ")

negrito_italico = "\033[1;3m"

print(f"Texto original = {texto} \nTexto em negrito = {negrito_italico}{texto}")