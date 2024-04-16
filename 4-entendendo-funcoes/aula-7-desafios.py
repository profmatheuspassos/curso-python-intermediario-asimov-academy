# Desafio 1

print("Desafio 1 - original")

valores = [1, 2, 3, 5, 10]

quadradosMaioresQueTres = []
quadradosMaioresQueTres2 = []

for valor in valores:
    if valor > 3:
        quadrado = valor ** 2
        quadradosMaioresQueTres.append(quadrado)

print(quadradosMaioresQueTres)

print("Desafio 1 - solução com compreensão de lista")

# compreensao = [valor ** 2 for valor in valores if valor > 3]

print([valor ** 2 for valor in valores if valor > 3])

print("Desafio 1 - solução com funções map e filter")

# quadMaioresQueTres = list(map(lambda x: x ** 2, (filter(lambda x: x > 3, valores))))

# print(quadMaioresQueTres)

print(list(map(lambda x: x ** 2, (filter(lambda x: x > 3, valores)))))

print("\n")

print("Desafio 2 - primeira solução - função dentro de função")

def multiplicarPor(n):
    def multiplicador(x):
        return x * n
    return multiplicador

dobrar = multiplicarPor(2)
print(dobrar(3))
print(dobrar(10))

vezesCinco = multiplicarPor(5)
print(vezesCinco(3))
print(vezesCinco(10))

print("Desafio 2 - segunda solução - função lambda")

from functools import partial

dobrar2 = partial((lambda x, n: x * n), n = 2)
vezes5 = partial((lambda x, n: x * n), n = 5)

print(dobrar2(3))
print(dobrar2(10))
print(vezes5(3))
print(vezes5(10))
