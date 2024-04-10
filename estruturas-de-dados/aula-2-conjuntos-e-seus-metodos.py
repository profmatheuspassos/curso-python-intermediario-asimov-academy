import timeit

A = {1, 2, 3, 4}
print("\nConjunto A e Conjunto B")
print(A)
print(type(A))
B = set({3, 4, 5, 6})
print(B)
print(type(B))

# Principal característica de conjuntos (set): eles sempre têm valores únicos
print("\nPrincipal característica de conjuntos (set): eles sempre têm valores únicos")
C = {1, 2, 1, 2, 2, 1, 2, 1}
print(C)
C.add(3)
print(C)
C.add(3)
print(C)

# Para identificar os itens únicos de uma lista é possível convertê-la para um conjunto
print("\nPara identificar os itens únicos de uma lista é possível convertê-la para um conjunto")
numeros = [1, 2, 3, 2, 1, 6, 4, 5, 3, 2, 1]
numerosUnicos= list(set(numeros))
print(numeros)
print(numerosUnicos)

# Conjuntos não têm ordem
print("\nConjuntos não têm ordem")
D = {10, "Python", 1.0, False}

# Se houvesse algo como print(A[0]) o código daria erro
for elemento in D:
    print(elemento)

# Elementos dentro de conjuntos são imutáveis
print("\nElementos dentro de conjuntos são imutáveis")
# E = {1, 2, 3, [4, 5, 6]}
# print(E) Este código vai dar erro porque o item "lista" dentro deste conjunto é mutável. Para corrigir esse erro seria possível substituir a lista por uma tupla, que é mutável
E = {1, 2, 3, (4, 5, 6)}
print(E)

# Métodos de conjuntos
print("\nMétodos de conjuntos")
print("\nunion")
F = A.union(B)
print(F)
print(A | B)

print("\nintersection")
G = A.intersection(B)
print(G)
print(A & B)

print("\ndifference")
H = A.difference(B)
print(H)
print(A - B)
print(B - A)

print("\nsymmetric_difference")
I = A.symmetric_difference(B)
print(I)
print((A - B) | (B - A))

# Procurar se um elemento está dentro de lista ou conjunto: em conjuntos a procura é muito mais rápida
print("\nTempo de procura de elemento em lista e em conjunto")
numLista = list(range(1_000))  # Lista com 1000 elementos
numConj = set(range(1_000))  # Conjunto com 1000 elementos

# Código para encontrar o número '500' na lista
codigoLista = '500 in numLista'
# Código para encontrar o número '500' no conjunto
codigoConjunto = '500 in numConj'
# Medindo o tempo para encontrar '500' na lista
tempoLista = timeit.timeit(codigoLista, globals=globals(), number=10000)
# Medindo o tempo para encontrar '500' no conjunto
tempoConjunto = timeit.timeit(codigoConjunto, globals=globals(), number=10000)

print(f"Tempo para encontrar o número 500 na lista......: {tempoLista} segundos")
print(f"Tempo para encontrar o número 500 no conjunto...: {tempoConjunto} segundos")