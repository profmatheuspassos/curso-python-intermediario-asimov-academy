valores = list(range(10))
print(f"Valores: {valores}")
print("Análise tradicional com for")
maioresQue5 = []
for valor in valores:
    if valor > 5:
        maioresQue5.append(valor)
print(maioresQue5)
print("Compreensão de listas")
novaListaMaiorQue5 = [
    valor # RESULTADO
    for valor in valores # para cada ELEMENTO em SEQUÊNCIA
    if valor > 5 # se CONDIÇÃO
]
print(novaListaMaiorQue5)
print("Compreensão de listas + 2")
novaListaMaiorQue5Mais2 = [
    valor + 2 # RESULTADO
    for valor in valores # para cada ELEMENTO em SEQUÊNCIA
    if valor > 5 # se CONDIÇÃO
]
print(novaListaMaiorQue5Mais2)
print("Compreensão de listas com função = (valor ** 2) + 2")
def somar2AoQuadrado(valor):
    return (valor ** 2) + 2
novaListaMaiorQue5AoQuadradoMais2 = [
    somar2AoQuadrado(valor) # RESULTADO
    for valor in valores # para cada ELEMENTO em SEQUÊNCIA
    if valor > 5 # se CONDIÇÃO
]
print(novaListaMaiorQue5AoQuadradoMais2)