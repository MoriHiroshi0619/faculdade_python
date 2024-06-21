def fila_atendimento(fila, tipo_atendimento, cliente = None):
    if tipo_atendimento != "a" and tipo_atendimento != "p" and tipo_atendimento != "c":
        print("Opção inválida")

    if tipo_atendimento == 'c':
        if cliente != None:
            fila.append(cliente)

    if tipo_atendimento == 'a':
        if fila:
            cliente_antedido = fila.pop(0)
            print(f"{cliente_antedido} atendido!")
        else:
            print("fila vazia")

    if tipo_atendimento == 'p':
        print("Imprimindo fila de atendimento")
        if not fila:
            print("Fila de atendimento VAZIA")
        else:
            for x in fila:
                print(f"{x} | ", end="")
            print()


fila = []
while True:
    opcao = input("Escolha uma opção: ")
    if opcao == "exit":
        break
    if opcao == "c":
        nome = input("Digite o nome do cliente: ")
        fila_atendimento(fila, opcao, nome)

    fila_atendimento(fila, opcao)

