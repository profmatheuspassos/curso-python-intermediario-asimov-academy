# Atribuir valores para variáveis específicas
print("Atribuir valores para variáveis específicas")
seq = (10, 20, 30)
a, b, c = seq
print(a)
print(b)
print(c)

print("\n")

# Desempacotando dicionários como chaves e valores ou como tuplas
print("Desempacotando dicionários como chaves e valores ou como tuplas")
dic = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3"
}
for chave, valor in dic.items():
    print(chave, valor)
for elemento in dic.items():
    print(elemento)

print("\n")

# Combinar método zip com enumerate
print("Combinar método zip com enumerate")
nomes = ["Juliano", "Laura", "Roberto", "Guilherme"]
idades = [30, 24, 19, 47]
for elemento in enumerate(zip(nomes, idades)):
    print(elemento)
for i, (nome, idade) in enumerate(zip(nomes, idades)):
    print(i, nome, idade)

print("\n")

# O desempacotamento deve ser com itens do mesmo tamanho
print("O desempacotamento deve ser com itens do mesmo tamanho")
print("a, b = [1, 2, 3] dará erro --> jogando três valores para duas variáveis")

print("\n")

# Pegar o valor do meio de uma lista
print("Pegar o valor do meio da lista")
minhaLista = [1, 2, 3, 4, 5]
primeiro, *meio, ultimo = minhaLista
print(minhaLista)
print(primeiro)
print(meio)
print(ultimo)

print("\n")

# Atribuir vários valores de uma vez só
print("Atribuir vários valores de uma vez só - asterisco sempre retorna uma lsita")
primeiro, *resto = (1, 2, 3, 4)
print(primeiro)
print(resto)
*resto, penultimo, ultimo = (1, 2, 3, 4)
print(resto)
print(penultimo)
print(ultimo)

print("\n")

# Uso de "_" como convenção para ignorar o conteúdo
print("Uso de \"_\" como convenção para ignorar o conteúdo")
primeiro, *_, ultimo = (1, 2, 3, 4)
print(primeiro)
print(_) # Imprimindo apenas para ver o conteúdo, mas a convenção é que isto será ignorado no script
print(ultimo)