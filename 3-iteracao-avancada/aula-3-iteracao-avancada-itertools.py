import itertools

seq1 = (1, 2, 3)
seq2 = ["a", "b", "c", "c"]

print("itertools.chain")
print(f"seq1: {seq1}")
print(f"seq2: {seq2}")
for elemento in itertools.chain(seq1, seq2):
    print(elemento)

print("\nitertools.zip_longest")
nomes = ["Juliano", "Laura", "Roberto", "Guilherme"]
idades = [30, 24, 19, 47]
cpfs = ["xxx", "yyy", "zzz"]
emails = ["abc@empresa.com", "xyz@empresa.com"]

print(f"nomes: {nomes}")
print(f"idades: {idades}")
print(f"cpfs: {cpfs}")
print(f"emails: {emails}")

for elemento in itertools.zip_longest(nomes, idades, cpfs, emails):
    print(elemento)

print("\nitertools.zip_longest com fillvalue = \"***\"")
for elemento in itertools.zip_longest(nomes, idades, cpfs, emails, fillvalue = "***"):
    print(elemento)

print("\nitertools.product")
comidas = ["churrasco", "pizza", "sushi"]
bebidas = ("refrigerante", "água")

print(f"comidas: {comidas}")
print(f"bebidas: {bebidas}")

for prato in itertools.product(comidas, bebidas):
    print(prato)

print("\nitertools.combinations")
nomes = ["Juliano", "Laura", "Roberto", "Guilherme"]

print(f"nomes: {nomes}")

for combinacao in itertools.combinations(nomes, 2):
    print(combinacao)

print("\nitertools.permutations")
for combinacao in itertools.permutations(nomes, 2):
    print(combinacao)

print("\nitertools.cycle - não tem fim, produz resultados \"eternamente\" - necessário mecanismo para parar a iteração")
print(f"cores: azul, amarelo")
print("incluído stop depois de 5 execuções")
i = 0
for cor in itertools.cycle(["azul", "amarelo"]):
    print(cor)
    input()
    i += 1
    if i == 5:
        break