valores = list(range(10))
print(f"Valores: {valores}")
print("Para transformar em conjunto, basta acrescentar { e } no início e no final:")
print("conjuntoValores = {valor for valor in valores if valor > 5}")
conjuntoValores = {
    valor
    for valor in valores
    if valor > 5
}
print(conjuntoValores)

print("\n")

print("Para dicionários é um pouco diferente:")
print("dicValores = {valor: valor + 2 for valor in valores if valor > 5}")
dicValores = {
    valor: valor + 2
    for valor in valores
    if valor > 5
}
print(dicValores)

print("\n")

print("Valores com produtos em dólar")
valoresDolares = {
    "leite": 0.78,
    "soja": 4.60,
    "maçã": 0.35
}
print(f"Valores em dólares: {valoresDolares}.")
print("Convertendo para real...")
fatorConversao = 4.95
valoresReais = {
    chave: round(valor * fatorConversao, 2)
    for chave, valor in valoresDolares.items()
}
print("Fórmula: \"valoresReais = {chave: round(valor * fatorConversao, 2) for chave, valor in valoresDolares.items()}\"")
print(f"Valores em reais: {valoresReais}.")