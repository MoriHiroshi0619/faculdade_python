populacao_inicial = 1000000
populacao_atual = populacao_inicial
ano = 1600

print("Ano\tNascimentos\tMortes\t\tPopulação")

while populacao_atual >= 0.1 * populacao_inicial:
    nascimentos = round(populacao_atual * 0.01)
    mortes = round(populacao_atual * 0.06)
    populacao_atual = populacao_atual - mortes + nascimentos
    
    print(f"{ano}\t{nascimentos}\t\t{mortes}\t\t{populacao_atual}")
    
    ano += 1

print("A população total caiu para menos de 10% da população original.")