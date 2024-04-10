# Função enumerate

nomes = ['Juliano', 'José', 'Lucas', 'Luiza']
print("Função enumerate()")
print("Sem enumerate()")
for n in range(len(nomes)):
    nome = nomes[n]
    print(f"Índice {n} --> nome: {nome}")

print("Com enumerate()")
for i, nome in enumerate(nomes):
    print(f'Índice {i} -> Nome: {nome}')

# Função sorted

conjunto = {1, 2, 3, 4}
ordenados = sorted(conjunto)
ordenadosReverso = sorted(conjunto, reverse = True)
print("\nFunção sorted()")
print(f"Conjunto original: {conjunto}")
print(f"Conjunto ordenado: {ordenados} - a função sorted() retorna uma lista")
print(f"Conjunto ordenado reverso: {ordenadosReverso}")

# Função reversed

print("\nFunção reversed() - só funciona se o objeto for \"inversível\" - por exemplo, não funciona com conjuntos")
for i in reversed(range(10)):
    print(i)

# Função zip

print("\nFunção zip() - iteração automática entre listas diferentes - ela para na lista de menor tamanho (se for o caso)")
nomes = ['Juliano', 'José', 'Lucas', 'Luiza']
idades = [30, 24, 19, 47]
for elemento in zip(nomes, idades):
    print(elemento)