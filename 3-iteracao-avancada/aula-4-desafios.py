# Crie uma função que retorna os valores de duas listas de forma intercalada, mesmo quando as listas têm tamanho diferente. Por exemplo, dadas as listas:

L1 = [1, 2, 3]
L2 = ['a', 'b', 'c', 'd', 'e']

# A função deve retornar:

# [1, 'a', 2, 'b', 3, 'c', 'd', 'e']

import itertools as it

def listasIntercaladas(lista1, lista2):
    L3 = []
    for valor1, valor2 in it.zip_longest(lista1, lista2, fillvalue = None):
        # Se o valor não for None ele adiciona os valores de cada lista
        if valor1 is not None:
            L3.append(valor1)
        if valor2 is not None:
            L3.append(valor2)
    return L3

print("Desafio 1")
print(listasIntercaladas(L1, L2))

print("\n")

# Imagine que você tem um restaurante com os seguintes itens no seu menu:
comidas = {
    'Prato Feito': 24.90,
    'Salada': 21.90,
    'Strogonoff': 29.90,
    'Feijoada': 32.90,
}
bebidas = {
    'Água': 3.90,
    'Refrigerante': 5.90,
    'Suco': 7.90,
}

# Crie um novo dicionário chamado combos onde cada chave é uma tupla contendo (comida, bebida), e o seu respectivo valor é o preço daquela combinação de comida e bebida.

print("Desafio 2")

# Cria um dicionário vazio para os combos
combo = {}

for tuplas in it.product(comidas.items(), bebidas.items()): # Laço que percorre todas as combinações possíveis de itens de comidas e bebidas
    chaveCombo = tuple(tup[0] for tup in tuplas) # Cria uma tupla com os nomes dos itens (comida e bebida)
    precoCombo = sum(tup[1] for tup in tuplas) # Soma os preços dos itens (comida e bebida)
    combo[chaveCombo] = round(precoCombo, 2) # Adiciona a combinação e seu preço arredondado ao dicionário de combos

# Imprime o dicionário de combos
"""
print(combo)  # Mostra o dicionário de combos com as combinações e seus preços
"""
# Formata a saída de cada combo conforme especificado
for chave, valor in combo.items():
    nomeProdutos = ' e '.join(chave)  # Junta os nomes dos produtos com ' e '
    print(f"Combo: {nomeProdutos}")   # Imprime o nome do combo
    print(f"Valor: {valor:.2f}")       # Imprime o valor do combo formatado com duas casas decimais
    print()                            # Imprime uma linha em branco antes do próximo