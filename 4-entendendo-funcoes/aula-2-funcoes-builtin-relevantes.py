# isinstance
print("Função isinstance - retorna o tipo da variável")
print("valor = 2")
valor = 2
if isinstance(valor, int): # ou if isinstance(valor, (int, float))
    print("Valor é int")
else:
    print("Não é int")

print("\n")

print("Funções any e all")
booleanos = [True, False, True]
print(all(booleanos))
print(any(booleanos))

print("\n")

print("Função map")
def somarDois(num):
    return num + 2

numeros = [3, 6, 10]
mapa = map(somarDois, numeros)
print(numeros)
print("mapa = map(somarDois, numeros)")
print(list(mapa))

print("\n")

print("Função filter")
def meuFiltro(n):
    return n > 5

filtro = filter(meuFiltro, numeros)
print(numeros)
print("filtro = filter(meuFiltro, numeros)")
print(list(filtro))